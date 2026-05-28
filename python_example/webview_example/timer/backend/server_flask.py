from threading import Thread
import socket
from datetime import datetime
from flask import Flask
from werkzeug.serving import make_server

WEEKDAYS=["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

def getClockPayload():
    now = datetime.now()
    return {
        "time": now.strftime("%H:%M:%S"),
        "date": f"{now.year}년 {now.month}월 {now.day}일 {WEEKDAYS[now.weekday()]}"
    }
        
    

def getFreePort():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return int(s.getsockname()[1])


class ClockApiServer:
    def __init__(self, frontend_dir):
        self.port = getFreePort()
        self.app = Flask(__name__, static_folder=str(frontend_dir), static_url_path="")
        self._server = make_server("127.0.0.1", self.port, self.app)
        self._thread = Thread(target=self._server.serve_forever, daemon=True)
        self.app.add_url_rule("/", "index", lambda: self.app.send_static_file("index.html"))
        self.app.add_url_rule("/api/clock", "clock", getClockPayload)
    
    @property
    def base_url(self):
        return f"http://127.0.0.1:{self.port}"
        
    def start(self):
        self._thread.start()
        
        
    def stop(self):
        self._server.shutdown()
        self._server.server_close()
        
        
