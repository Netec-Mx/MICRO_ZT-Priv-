from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import socket
from datetime import datetime, timezone

HOST = "0.0.0.0"
PORT = 8080
DB_HOST = "database"
DB_PORT = 5432


class Handler(BaseHTTPRequestHandler):
    def _json(self, status_code: int, payload: dict) -> None:
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        now = datetime.now(timezone.utc).isoformat()

        if self.path in {"/", "/health"}:
            self._json(200, {
                "service": "finsecure-backend-api",
                "status": "ok",
                "timestamp_utc": now
            })
            return

        if self.path == "/db-check":
            try:
                with socket.create_connection((DB_HOST, DB_PORT), timeout=2):
                    self._json(200, {
                        "service": "finsecure-backend-api",
                        "database_connectivity": "reachable",
                        "destination": f"{DB_HOST}:{DB_PORT}",
                        "timestamp_utc": now
                    })
            except OSError as exc:
                self._json(503, {
                    "service": "finsecure-backend-api",
                    "database_connectivity": "unreachable",
                    "destination": f"{DB_HOST}:{DB_PORT}",
                    "error": str(exc),
                    "timestamp_utc": now
                })
            return

        self._json(404, {
            "error": "not_found",
            "path": self.path,
            "timestamp_utc": now
        })

    def log_message(self, fmt, *args):
        print(f"[backend] {self.address_string()} - {fmt % args}", flush=True)


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Handler)
    print(f"[backend] Listening on http://{HOST}:{PORT}", flush=True)
    server.serve_forever()