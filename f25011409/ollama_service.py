"""Expose the local Ollama model through a small HTTP service.

Run Ollama first, then start this file. The service accepts both the native
Ollama chat shape and the OpenAI-compatible chat-completions shape.
"""

import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.request import Request, urlopen


OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")
MODEL = os.getenv("OLLAMA_MODEL", "qwen2:1.5b")
HOST = os.getenv("SERVICE_HOST", "127.0.0.1")
PORT = int(os.getenv("SERVICE_PORT", "8000"))


def ollama_chat(messages):
    payload = json.dumps({"model": MODEL, "messages": messages, "stream": False}).encode()
    request = Request(
        f"{OLLAMA_URL}/api/chat",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=120) as response:
        result = json.load(response)
    return result["message"]["content"]


class Handler(BaseHTTPRequestHandler):
    def _send(self, status, body):
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/health":
            self._send(200, {"status": "ok", "model": MODEL})
        else:
            self._send(404, {"error": "not found"})

    def do_POST(self):
        if self.path not in ("/api/chat", "/v1/chat/completions"):
            self._send(404, {"error": "not found"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            body = json.loads(self.rfile.read(length))
            answer = ollama_chat(body.get("messages", []))
            if self.path.startswith("/v1/"):
                self._send(200, {"id": "ollama-local", "object": "chat.completion", "choices": [{"index": 0, "message": {"role": "assistant", "content": answer}, "finish_reason": "stop"}]})
            else:
                self._send(200, {"model": MODEL, "message": {"role": "assistant", "content": answer}, "done": True})
        except Exception as exc:
            self._send(502, {"error": str(exc)})


if __name__ == "__main__":
    print(f"Serving {MODEL} at http://{HOST}:{PORT}")
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
