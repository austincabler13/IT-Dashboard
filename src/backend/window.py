import pathlib
import sys

import webview

from api import API


def get_frontend_folder():
    if getattr(sys, "frozen", False):
        base_path = pathlib.Path(getattr(sys, "_MEIPASS"))
    else:
        base_path = pathlib.Path(__file__).resolve().parent.parent

    return base_path / "frontend"


def create():
    print("Creating IT Dashboard window...")

    api = API()
    frontend_folder = get_frontend_folder()
    index_file = frontend_folder / "index.html"

    webview.create_window(
        "IT Dashboard",
        js_api=api,
        url=str(index_file),
        width=800,
        height=600
    )

    webview.start(gui="edgechromium")