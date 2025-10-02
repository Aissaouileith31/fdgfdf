import sqlite3
import flet as ft  # Import flet with alias ft
from base64_string_icon_path import icons

# Global variable for hover animation state
hovering = False

def add_page(page):
    """
    Main page for publishing subjects and lessons
    """
    
    # Page configuration
    page.title = "publish subject"
    page.update
    
    def go_to_home(e):
        """Navigate back to home page"""
        from home import home
        page.controls.clear()
        home(page)
        page.update()
    
    def go_to_add_lessons(e):
        """Navigate to add lessons page"""
        from add_lessons_page import add_lessons
        page.controls.clear()
        add_lessons(page)
        page.update()
    
    def animate_buttons(e):
        """Animate buttons on hover effect"""
        global hovering
        if e.data == 'true' and not hovering:
            e.control.scale = 1.2  # Scale up on hover
            hovering = True
        elif e.data == "false" and hovering:
            e.control.scale = 1  # Scale back to normal
            hovering = False
        page.update()

    def open_drawer(e):
        """Open navigation drawer"""
        page.drawer.open = True
        page.update()
    
    # Navigation drawer configuration
    page.drawer = ft.NavigationDrawer(
        bgcolor="#2F4F7F",  # Dark blue background
        controls=[ft.ListTile(ft.Container(content=ft.Column(controls=[
            # Home button
            ft.ElevatedButton(
                bgcolor='#8A0000', color='white', height=60, 
                on_hover=animate_buttons, on_click=go_to_home,
                content=ft.Row(controls=[
                    ft.Image(src_base64=icons[13], width=50, height=50),  # Home icon
                    ft.Text('home', size=20, text_align=ft.TextAlign.CENTER)
                ])
            ),
            # About Us button
            ft.ElevatedButton(
                bgcolor='#8A0000', color="white", height=60, 
                on_hover=animate_buttons,
                content=ft.Row(controls=[
                    ft.Image(src_base64=icons[0], width=50, height=50),  # About icon
                    ft.Text('aboutus', size=20, text_align=ft.TextAlign.CENTER)
                ])
            ),
            # Feedback button
            ft.ElevatedButton(
                bgcolor='#8A0000', color="white", height=60, 
                on_hover=animate_buttons,
                content=ft.Row(controls=[
                    ft.Image(src_base64=icons[0], width=50, height=50),  # Feedback icon
                    ft.Text('give feedback', size=20, text_align=ft.TextAlign.CENTER)
                ])
            ),
            # Add button
            ft.ElevatedButton(
                bgcolor='#8A0000', color="white", height=60, 
                on_hover=animate_buttons,
                content=ft.Row(controls=[
                    ft.Image(src_base64=icons[0], width=50, height=50),  # Add icon
                    ft.Text('Add', size=20, text_align=ft.TextAlign.CENTER)
                ])
            ),
            ],
            scroll='auto'  # Enable scrolling
        )))
        ])
    

    # AppBar configuration
    page.appbar = ft.AppBar(
        bgcolor='#2F4F5F',  # Dark blue-gray background
        title=ft.Text(
            'BAC DZ - algeria futur', 
            size=20, weight='bold', 
            text_align=ft.TextAlign.CENTER, 
            offset=ft.Offset(0.1,0), 
            color='white'
        ),
        leading=ft.ElevatedButton(  # Hamburger menu button
            '| | |', 
            on_click=open_drawer, 
            on_hover=animate_buttons, 
            color='black', 
            bgcolor='white', 
            width=40, 
            height=40, 
            offset=ft.Offset(0.2,0)
        ),
        center_title=True  # Center the title
    )

    # First frame container - Lessons and Summaries
    first_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('add lessons and summaries', color='white', weight='bold', size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('publish your lessons to other students', color='white', size=20, text_align=ft.TextAlign.CENTER),
                # Add lessons button
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#2F4F2F',
                    on_hover=animate_buttons, on_click=go_to_add_lessons,
                    content=ft.Container(content=ft.Stack([
                        ft.Image(src_base64=icons[17], width=50, height=50, top=5, left=0),  # Lessons icon
                        ft.Text('add lessons and summaries', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0.1,0))
                    ]))
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Center vertically
            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Center horizontally
            ),
            border=ft.border.all(3, 'black'),  # Black border
            bgcolor='#4CAF51',  # Green background
            padding=10,  # Internal padding
            width=300, height=400,  # Fixed dimensions
            alignment=ft.alignment.center,  # Center content
            margin=ft.margin.only(top=20)  # Top margin
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER  # Center the row
    )

    # Second frame container - Add Subject
    second_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('add subject', color='white', weight='bold', size=33),
                ft.Text('you can also publish subject to other students', color='white', size=20, text_align=ft.TextAlign.CENTER),
                # Add subject button
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#CC0000',
                    on_hover=animate_buttons,
                    content=ft.Container(content=ft.Stack([
                        ft.Image(src_base64=icons[24], width=60, height=60, top=0, left=0),  # Subject icon
                        ft.Text('add subject', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0.1,0))
                    ])), 
                    offset=ft.Offset(0,0.6)  # Vertical offset
                )],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),  # Black border
            bgcolor='#FF3737',  # Red background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)  # Top margin
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    def page_resize(e):
        """Handle page resize for responsive layout"""
        if page.width < 600:
            # Mobile layout: stack frames vertically
            page.controls.append(ft.Column(controls=[first_frame, second_frame]))
        else:
            # Desktop layout: place frames side by side
            page.controls.append(ft.Row(controls=[first_frame, second_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
        page.update()
    
    # Set resize handler and initialize layout
    page.on_resize = page_resize
    page_resize(None)  # Initial layout setup