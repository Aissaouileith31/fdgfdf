"""---the home page---"""
# Note: All frames in the app follow the same structure with different
# colors, text, and button functions
# Use the guide in lessons.py at line 65 for more information

import flet as ft
from base64_string_icon_path import icons

hovering = False

# These functions handle navigation to different pages
def home(page):
    """---Home main function---"""
    # Page configuration
    page.title = "BAC DZ - algeria futur"
    page.padding = 1
    page.bgcolor = "#2F4F7F"
    page.scroll = "auto"
    page.update()

    # Navigation functions
    def go_to_admin_page(e):
        """Navigate to admin page"""
        from admin.admin_page import admin_page
        page.controls.clear()
        admin_page(page)
        page.update()
    def go_to_add_page(e):
        """Navigate to add page"""
        from add_page import add_page
        page.controls.clear()
        add_page(page)
        page.update()
        
    def go_to_normal_subject(e):
        """Navigate to normal subject page"""
        from normal_subject import normal_subject
        page.controls.clear()
        normal_subject(page)
        page.update()

    def go_to_youtub_page(e):
        """Navigate to YouTube page"""
        from youtub import youtub
        page.controls.clear()
        youtub(page)
        page.update()

    def go_to_bac_subject_page(e):
        """Navigate to BAC subject page"""
        from bac_subject import bac_subject
        page.controls.clear()
        bac_subject(page)
        page.update()

    def go_to_lessons_page(e):
        """Navigate to lessons page"""
        from lessons import lessons
        page.controls.clear()
        lessons(page)
        page.update()
        
    def animate_buttons(e):
        """Animate buttons on hover"""
        global hovering
        if e.data == 'true' and not hovering:
            e.control.scale = 1.2
            hovering = True
        elif e.data == "false" and hovering:
            e.control.scale = 1
            hovering = False
        page.update()
        
    # HEADER SECTION
    def open_drawer(e):
        """Open navigation drawer"""
        page.drawer.open = True
        page.update()
        
    # Navigation drawer setup
    page.drawer = ft.NavigationDrawer(
        bgcolor="#2F4F7F",
        controls=[
            ft.ListTile(
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.ElevatedButton(
                                bgcolor='#8A0000',
                                color='white',
                                height=60,
                                on_hover=animate_buttons,
                                content=ft.Row(
                                    controls=[
                                        ft.Image(src_base64=icons[13], width=50, height=50),
                                        ft.Text('home', size=20, text_align=ft.TextAlign.CENTER)
                                    ]
                                )
                            ),
                            ft.ElevatedButton(
                                bgcolor='#8A0000',
                                color="white",
                                height=60,
                                on_hover=animate_buttons,
                                content=ft.Row(
                                    controls=[
                                        ft.Image(src_base64=icons[0], width=50, height=50),
                                        ft.Text('aboutus', size=20, text_align=ft.TextAlign.CENTER)
                                    ]
                                )
                            ),
                            ft.ElevatedButton(
                                bgcolor='#8A0000',
                                color="white",
                                height=60,
                                on_hover=animate_buttons,
                                content=ft.Row(
                                    controls=[
                                        ft.Image(src_base64=icons[0], width=50, height=50),
                                        ft.Text('give feedback', size=20, text_align=ft.TextAlign.CENTER)
                                    ]
                                )
                            ),
                            ft.ElevatedButton(
                                bgcolor='#8A0000',
                                color="white",
                                height=60,
                                on_hover=animate_buttons,
                                on_click=go_to_add_page,
                                content=ft.Row(
                                    controls=[
                                        ft.Image(src_base64=icons[0], width=50, height=50),
                                        ft.Text('Add', size=20, text_align=ft.TextAlign.CENTER)
                                    ]
                                )
                            ),

                            ft.ElevatedButton(
                                bgcolor='#8A0000',
                                color='white',
                                height=60,
                                on_hover=animate_buttons,
                                on_click=go_to_admin_page,
                                content=ft.Row(
                                    controls=[
                                        ft.Image(src_base64=icons[13], width=50, height=50),
                                        ft.Text('admin', size=20, text_align=ft.TextAlign.CENTER)
                                    ]
                                )
                            )
                        ],
                        scroll='auto'
                    )
                )
            )
        ]
    )

    # App bar setup
    page.appbar = ft.AppBar(
        bgcolor='#2F4F5F',
        title=ft.Text('BAC DZ - algeria futur', size=20, weight='bold', text_align=ft.TextAlign.CENTER, 
                     offset=ft.Offset(0.1, 0), color='white'),
        leading=ft.ElevatedButton('| | |', on_click=open_drawer, on_hover=animate_buttons, color='black', 
                                 bgcolor='white', width=40, height=40, offset=ft.Offset(0.2, 0)),
        center_title=True)

    # First frame - Lessons and summaries
    first_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries', color='white', weight='bold', size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('we offer a complete and well-structured lessons for all BAC subject', 
                       color='white', size=20, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200, height=60, color='white', bgcolor='#2F4F2F', on_hover=animate_buttons, 
                                 on_click=go_to_lessons_page, 
                                 content=ft.Container(content=ft.Stack([ft.Image(src_base64=icons[17], width=50, height=50, 
                                                                                top=5, left=0), 
                                                                       ft.Text('lessons and summaries', size=20, 
                                                                              text_align=ft.TextAlign.CENTER, 
                                                                              offset=ft.Offset(0.1, 0))])))
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor='#4CAF51',
            padding=10,
            width=300,
            height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Second frame - YouTube channel
    second_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('youtube channel', color='white', weight='bold', size=33),
                ft.Text('all what you need from channel for all subject', 
                       color='white', size=20, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200, height=60, color='white', bgcolor='#CC0000', on_hover=animate_buttons, 
                                 on_click=go_to_youtub_page, 
                                 content=ft.Container(content=ft.Stack([ft.Image(src_base64=icons[24], width=60, height=60, 
                                                                                top=0, left=0), 
                                                                       ft.Text('youtube          channel', size=20, 
                                                                              text_align=ft.TextAlign.CENTER, 
                                                                              offset=ft.Offset(0.1, 0))])), 
                                 offset=ft.Offset(0, 0.6))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor='#FF3737',
            padding=10,
            width=300,
            height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Third frame - Previous BAC subjects
    therd_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('previous BAC subject ', color='black', weight='bold', size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('We offer all past BAC tests for more training', 
                       color='black', size=20, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200, height=60, color='white', bgcolor='#999900', on_hover=animate_buttons, 
                                 on_click=go_to_bac_subject_page, 
                                 content=ft.Container(content=ft.Stack([ft.Image(src_base64=icons[23], width=60, height=60, 
                                                                                top=0, left=0), 
                                                                       ft.Text('BAC                           subject', size=20, 
                                                                              text_align=ft.TextAlign.CENTER, 
                                                                              offset=ft.Offset(0.1, 0))])))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor='#CCCC66',
            padding=10,
            width=300,
            height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Fourth frame - School year subjects
    fourth_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('subject of the school year', color='black', weight='bold', size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('we also offer the school year subjects', 
                       color='black', size=20, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200, height=60, color='white', bgcolor='#7A288A', on_hover=animate_buttons, 
                                 on_click=go_to_normal_subject, 
                                 content=ft.Container(content=ft.Stack([ft.Image(src_base64=icons[23], width=60, height=60, 
                                                                                top=0, left=0), 
                                                                       ft.Text('school year                           subject', size=20, 
                                                                              text_align=ft.TextAlign.CENTER, 
                                                                              offset=ft.Offset(0.1, 0))])))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor='#C7B8EA',
            padding=10,
            width=300,
            height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Fifth frame - Ask AI
    fifth_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('Ask AI', color='white', weight='bold', size=33),
                ft.Text('if you are confused ask AI for more information', 
                       color='white', size=20, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200, height=60, color='white', bgcolor='#032B44', on_hover=animate_buttons, 
                                 content=ft.Container(content=ft.Stack([ft.Image(src_base64=icons[1], width=50, height=50, 
                                                                                top=0, left=0), 
                                                                       ft.Text('ask                             AI', size=20, 
                                                                              text_align=ft.TextAlign.CENTER, 
                                                                              offset=ft.Offset(0.1, 0))])))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor='#2F4F9F',
            padding=10,
            width=300,
            height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Sixth frame - Zoom courses (Coming soon)
    six_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('ZOOM cours ', color='white', weight='bold', size=33),
                ft.Text('COMMING SOON', color='white', size=20, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(text='COMMING SOON', width=200, height=60, color='white', bgcolor='#8A0000', 
                                 style=ft.ButtonStyle(text_style=ft.TextStyle(size=20)))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            padding=10,
            width=300,
            height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Responsive layout function
    def page_resize(e):
        """Adjust layout based on screen size"""
        if page.width < 600:
            # Mobile layout - single column
            page.controls.append(ft.Column(controls=[first_frame, second_frame, therd_frame, fourth_frame, fifth_frame]))
        else:
            # Desktop layout - rows
            page.controls.append(ft.Row(controls=[first_frame, second_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[therd_frame, fourth_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[fifth_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
        page.update()

    # Set up resize handler and initial layout
    page.on_resize = page_resize
    page_resize(None)