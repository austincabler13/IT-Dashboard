import pathlib
import webview

def create():
    print("Creating IT Dashboard window...")\
    
    backend_folder = pathlib.Path(__file__).parent
    frontend_folder = backend_folder.parent / "frontend"
    webview.create_window("IT Dashboard", str(frontend_folder / "index.html"), width=800, height=600)
    webview.start()