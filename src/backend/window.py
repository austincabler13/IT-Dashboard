import pathlib
import webview
from api import API

def create():
    print("Creating IT Dashboard window...")
    api = API()
    
    backend_folder = pathlib.Path(__file__).resolve().parent
    frontend_folder = backend_folder.parent / "frontend"
    webview.create_window("IT Dashboard", js_api=api, url=str(frontend_folder / "index.html"), width=800, height=600)
    webview.start()