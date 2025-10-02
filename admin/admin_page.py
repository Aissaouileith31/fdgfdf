import flet as ft
import sqlite3
import base64_string_icon_path
from base64_string_icon_path import icons
import sqlite3
hovering = False  # Global hover state variable
def admin_page(page: ft.Page):
    page.title = "Admin Page"
    
    def go_to_home(e):
        """Navigate back to home page"""
        from home import home
        page.controls.clear()
        home(page)
        page.update()
    def animate_buttons(e):
        """Handle button hover animations with scale effect"""
        global hovering  # Access global hover state variable
        if e.data == 'true' and not hovering:
            # Scale up button when mouse enters
            e.control.scale = 1.2
            hovering = True
        elif e.data == "false" and hovering:
            # Scale back to normal when mouse leaves
            e.control.scale = 1
            hovering = False
        page.update()
    def open_drawer(e):
        """Open the navigation drawer/sidebar"""
        page.drawer.open = True
        page.update()
    
    # =========================================================================
    # NAVIGATION DRAWER CONFIGURATION
    # =========================================================================
    page.drawer = ft.NavigationDrawer(
        bgcolor="#2F4F5F",  # Dark blue-gray background
        controls=[
            ft.ListTile(
                ft.Container(
                    content=ft.Column(
                        controls=[
                            # Home navigation button
                            ft.ElevatedButton(
                                bgcolor='#8A0000',  # Dark red background
                                color='white',  # White text
                                height=60,  # Fixed height
                                on_hover=animate_buttons,  # Hover animation
                                on_click=go_to_home,  # Navigation action
                                content=ft.Row(
                                    controls=[
                                        ft.Image(src_base64=icons[13], width=50, height=50),  # Home icon
                                        ft.Text('home', size=20, text_align=ft.TextAlign.CENTER)
                                    ]
                                )
                            ),
                            # About Us button
                            ft.ElevatedButton(
                                bgcolor='#8A0000', 
                                color="white", 
                                height=60, 
                                on_hover=animate_buttons,
                                content=ft.Row(
                                    controls=[
                                        ft.Image(src_base64=icons[0], width=50, height=50),  # About icon
                                        ft.Text('aboutus', size=20, text_align=ft.TextAlign.CENTER)
                                    ]
                                )
                            ),
                            # Feedback button
                            ft.ElevatedButton(
                                bgcolor='#8A0000', 
                                color="white", 
                                height=60, 
                                on_hover=animate_buttons,
                                content=ft.Row(
                                    controls=[
                                        ft.Image(src_base64=icons[0], width=50, height=50),  # Feedback icon
                                        ft.Text('give feedback', size=20, text_align=ft.TextAlign.CENTER)
                                    ]
                                )
                            ),
                        ],
                        scroll='auto'  # Enable scrolling if content overflows
                    )
                )
            )
        ]
    )

    # =========================================================================
    # APP BAR CONFIGURATION (Top Navigation Bar)
    # =========================================================================
    page.appbar = ft.AppBar(
        bgcolor='#2F4F5F',  # Match drawer background color
        title=ft.Text(
            'BAC DZ - lessons',  # Page title
            size=20, 
            weight=ft.FontWeight.BOLD, 
            text_align=ft.TextAlign.CENTER, 
            offset=ft.Offset(0.1, 0),  # Slight horizontal offset
            color='white'  # White text color
        ),
        leading=ft.ElevatedButton(  # Hamburger menu button
            '| | |',  # Menu icon
            on_click=open_drawer,  # Open drawer on click
            on_hover=animate_buttons,  # Hover animation
            color='black',  # Text color
            bgcolor='white',  # Background color
            height=40,  # Fixed height
            width=40,  # Fixed width
            offset=ft.Offset(0.2, 0)  # Positioning offset
        ),
        center_title=True  # Center the title
    )
 
    

    # Create the password input field
    input_password = ft.TextField(
        label="Enter Admin Password",
        password=True,
        can_reveal_password=True,
        width=300,
        filled=True
    )

    def check_password(e):
        input_password_value = input_password.value
        # Connect to the SQLite database
        conn = sqlite3.connect('admin/password.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM password WHERE id=1")
        result = cursor.fetchone()
        if result:
            stored_password = result[0]
            if input_password_value == stored_password:
                # Password is correct, navigate to admin functionalities
                page.controls.clear()
                from .admin_dashboard import admin_dashboard
                admin_dashboard(page)
                page.update()
            else:
                # Incorrect password
                input_password.error_text = "Incorrect password. Please try again."
                input_password.value = ""
                page.update()

    log_in = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Admin Page", size=30, weight="bold", color="white"),
                ft.Text("Welcome to the admin page. Here you can manage the application settings and user accounts.", size=20, color="white")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        alignment=ft.alignment.center,
        padding=20
    )

    # Add all components to the page
    page.add(
        log_in,
        ft.Container(content=input_password, alignment=ft.alignment.center),
        ft.Container(content=ft.ElevatedButton("Log In", on_click=check_password),
                     alignment=ft.alignment.center),
        ft.Container(content=ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#81C784',
                    on_hover=animate_buttons, on_click=go_to_home,
                    content=ft.Text('Back', size=20, text_align=ft.TextAlign.CENTER)),)
    )