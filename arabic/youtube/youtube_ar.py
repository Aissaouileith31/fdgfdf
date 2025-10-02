import flet as ft
import sqlite3 as sq
from base64_string_icon_path import icons

hovering = False  # Variable to control hover state

def arabic_youtube(page):
    def go_back(e):
        page.controls.clear()
        from youtub import youtub
        youtub(page)
        page.update()
    # Function to go back to home page
    def go_to_home(e):
        from home import home
        page.controls.clear()
        home(page)
        page.update()

    # Function to animate buttons on hover
    def animate_buttons(e):
        global hovering
        if e.data == "true" and not hovering:
            e.control.scale = 1.2   # Enlarge button on hover
            hovering = True
        elif e.data == "false" and hovering:
            e.control.scale = 1     # Restore original size
            hovering = False
            page.update()

    # Function to open navigation drawer
    def open_drawer(e):
        page.drawer.open = True
        page.update()

    # Drawer (side navigation menu)
    page.drawer = ft.NavigationDrawer(
        bgcolor="#2F4F5F",
        controls=[
            ft.ListTile(
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.ElevatedButton(
                                bgcolor="#8A0000",
                                color="white",
                                height=60,
                                on_hover=animate_buttons,
                                on_click=go_to_home,
                                content=ft.Row(
                                    controls=[
                                        ft.Image(src_base64=icons[13], width=50, height=50),
                                        ft.Text("Home", size=20, text_align=ft.TextAlign.CENTER),
                                    ]
                                ),
                            )
                        ],
                        scroll="auto",
                    )
                )
            )
        ],
    )

    # AppBar (top bar)
    page.appbar = ft.AppBar(
        bgcolor="#2F4F5F",
        title=ft.Text(
            "BAC DZ - Arabic Lessons",   # App title
            size=20,
            weight="bold",
            text_align=ft.TextAlign.CENTER,
            offset=ft.Offset(0.1, 0),
            color="white",
        ),
        leading=ft.ElevatedButton(
            "| | |",                     # Button to open drawer
            on_click=open_drawer,
            on_hover=animate_buttons,
            color="black",
            bgcolor="white",
            height=40,
            width=40,
            offset=ft.Offset(0.2, 0),
        ),
        center_title=True,
    )

    # Database connection
    arabic_db_path = r"arabic\youtube\youtube_ar_db.db"
    conn = sq.connect(arabic_db_path)
    cursor = conn.cursor()

    # Fetch lessons data
    cursor.execute("SELECT link, cahnel_name FROM arabic_lessons")
    info = cursor.fetchall()

    # Display lessons
    for link, cahnel_name in info:  # Match order from SELECT
        # Function to open lesson link in browser
        def open_link(e, url=link):
            page.launch_url(url)

        page.add(
            ft.Row(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                # Show teacher name
                                ft.Text(
                                    f"Teacher {cahnel_name} :",
                                    color="white",
                                    weight="bold",
                                    size=25,
                                    text_align=ft.TextAlign.CENTER
                                ),
                                # Static subject label
                                ft.Text(
                                    "Arabic",
                                    color="white",
                                    size=20,
                                    text_align=ft.TextAlign.CENTER
                                ),
                                # Button to open lesson
                                ft.ElevatedButton(
                                    width=200,
                                    height=60,
                                    color="white",
                                    bgcolor="#F57C00",
                                    on_hover=animate_buttons,
                                    on_click=open_link,  # Opens link in browser
                                    content=ft.Row(
                                        controls=[
                                            ft.Image(src_base64=icons[2], width=50, height=50),
                                            ft.Text("see channel", size=18, text_align=ft.TextAlign.CENTER),
                                        ]
                                    ),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        border=ft.border.all(3, "black"),
                        bgcolor="#FFB74D",
                        padding=10,
                        width=300,
                        height=300,
                        alignment=ft.alignment.center,
                        margin=ft.margin.only(top=20),
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

    page.add(ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#81C784',
                    on_hover=animate_buttons, on_click=go_back,
                    content=ft.Text('Back', size=20, text_align=ft.TextAlign.CENTER)
                )
    )

    page.update()
