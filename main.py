import flet as ft
from home import home

def main(page):
    home(page)

try:
    ft.app(target=main, assets_dir="assets")
except Exception as e:
    print("Error:", e)