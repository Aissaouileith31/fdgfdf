import flet as ft
import sqlite3 as sq
from base64_string_icon_path import icons

def arabic_lessons(page):
    def go_back(e):
        page.controls.clear()
        from arabic.branch import branch
        branch(page)
        page.update()
    def go_to_home(e):
        from home import home
        page.controls.clear()
        home(page)
        page.update()
    
    def animate_buttons(e):
        # Use page's client_storage instead of global variable
        hovering = page.client_storage.get("hovering") or False
        
        if e.data == 'true' and not hovering:
            e.control.scale = 1.2
            page.client_storage.set("hovering", True)
        elif e.data == "false" and hovering:
            e.control.scale = 1
            page.client_storage.set("hovering", False)
        page.update()

    def open_drawer(e):
        page.drawer.open = True
        page.update()

    # Define drawer
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
                            ),
                            ft.ElevatedButton(
                                bgcolor="#8A0000",
                                color="white",
                                height=60,
                                on_hover=animate_buttons,
                                content=ft.Row(
                                    controls=[
                                        ft.Image(src_base64=icons[0], width=50, height=50),
                                        ft.Text("About Us", size=20, text_align=ft.TextAlign.CENTER),
                                    ]
                                ),
                            ),
                            ft.ElevatedButton(
                                bgcolor="#8A0000",
                                color="white",
                                height=60,
                                on_hover=animate_buttons,
                                content=ft.Row(
                                    controls=[
                                        ft.Image(src_base64=icons[0], width=50, height=50),
                                        ft.Text("Give Feedback", size=20, text_align=ft.TextAlign.CENTER),
                                    ]
                                ),
                            ),
                        ],
                        scroll="auto",
                    )
                )
            )
        ],
    )

    # AppBar
    page.appbar = ft.AppBar(
        bgcolor="#2F4F5F",
        title=ft.Text(
            "BAC DZ - Lessons",
            size=20,
            weight="bold",
            text_align=ft.TextAlign.CENTER,
            offset=ft.Offset(0.1, 0),
            color="white",
        ),
        leading=ft.ElevatedButton(
            "| | |",
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

    # Clear existing controls
    page.controls.clear()
    
    # Create a column to hold lesson buttons
    lessons_column = ft.Column(
        scroll="auto",
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )
    
    # Add lessons column to page
    page.controls.append(ft.Container(
        content=lessons_column,
        expand=True,
        padding=20
    ))

    # Database operations with error handling
    try:
        arabic_db_path = r'arabic/lessons/arabic_lessons_adab_falsafa/arabic_lessons.db'
        conn = sq.connect(arabic_db_path)
        cursor = conn.cursor()

        cursor.execute('SELECT link FROM arabic_lessons')
        links = cursor.fetchall()
        
        for i, link in enumerate(links, 1):
            lesson_button = ft.ElevatedButton(
                expand=True,
                width=400,
                height=80,
                color='white',
                bgcolor='#2F4F2F',
                on_hover=animate_buttons,
                on_click=lambda e, link=link[0]: page.launch_url(link),
                content=ft.Container(
                    content=ft.Stack([
                        ft.Image(src_base64=icons[17], width=50, height=50, top=15, left=10),
                        ft.Text(
                            f'Lesson in Arabic N°{i}',
                            size=20,
                            text_align=ft.TextAlign.CENTER,
                            left=70,
                            top=25
                        )
                    ])
                )
            )
            
            lessons_column.controls.append(
                ft.Container(
                    content=lesson_button,
                    alignment=ft.alignment.center,
                    margin=5
                )
            )
            
    except sq.Error as e:
        # Add error message if database fails
        lessons_column.controls.append(
            ft.Text(f"Error loading lessons: {str(e)}", color="red", size=16)
        )
    finally:
        # Ensure connection is closed
        if 'conn' in locals():
            conn.close()

    page.add(
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#81C784',
                    on_hover=animate_buttons, on_click=go_back,
                    content=ft.Text('Back', size=20, text_align=ft.TextAlign.CENTER)
                )
            )

    page.update()