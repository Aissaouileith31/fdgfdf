import flet as ft
import sqlite3

def admin_dashboard(page):
    page.title = "Admin Dashboard"
    page.window_width = 800
    page.window_height = 600
    page.window_resizable = False

    # Example content for the admin dashboard
    dashboard_content = ft.Column(
        controls=[
            ft.Text("Welcome to the Admin Dashboard", size=30, weight="bold"),
            ft.Text("Here you can manage users, settings, and view reports.", size=20),
            # Add more admin functionalities here
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    page.add(dashboard_content)
    page.update()