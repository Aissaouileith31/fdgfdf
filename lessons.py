"""---the lessons page (Flet version)---"""

import flet as ft  # Import flet with alias ft for better namespace management
from base64_string_icon_path import icons  # Import base64 encoded icons

# Global variable to track hover state for button animations
hovering = False

def lessons(page):
    """
    Lessons page displaying various subject categories in an educational app
    This page shows subject cards with consistent styling and responsive layout
    """
    
    # Page configuration - minimal padding for full-width layout
    page.padding = 1
    def go_to_ar_bransh(e):
        import arabic.branch as arabic_module
        page.controls.clear()
        arabic_module.branch(page)
        page.update()
    def go_to_home(e):
        """Navigate back to the home page"""
        from home import home  # Import home page function
        page.controls.clear()  # Clear current page controls
        home(page)  # Load home page
        page.update()  # Refresh page display
    
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
        page.update()  # Apply animation changes

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
    
    # =========================================================================
    # SUBJECT FRAME DEFINITIONS (20 Subject Cards)
    # Each frame follows the same structure with different content and colors
    # =========================================================================

    # Frame 1: Arabic Subject
    first_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('Arabic', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#F57C00',
                    on_hover=animate_buttons,
                    on_click=go_to_ar_bransh,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[2], width=50, height=50),  # Arabic icon
                            ft.Text('Arabic', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Center content vertically
            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Center content horizontally
            ),
            border=ft.border.all(3, 'black'),  # Black border
            bgcolor="#FFB74D",  # Orange background
            padding=10,  # Internal padding
            width=300, height=400,  # Fixed dimensions
            alignment=ft.alignment.center,  # Center container content
            margin=ft.margin.only(top=20)  # Top margin only
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER  # Center the row
    )

    # Frame 2: Math Subject
    second_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('math', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#388E3C',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[18], width=50, height=50),  # Math icon
                            ft.Text('Math', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#81C784",  # Green background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Frame 3: Science Subject
    therd_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('science', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#BA68C8',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[21], width=60, height=60),  # Science icon
                            ft.Text('science', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#6A1B9A",  # Purple background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )
    
    # Frame 4: Physics Subject
    fourth_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('physics', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#F57C00',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[10], width=60, height=60),  # Physics icon
                            ft.Text('physics', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#FFB74D",  # Orange background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Frame 5: Islamic Education Subject
    fifth_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('islamic education', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#388E3C',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[15], width=60, height=60),  # Islamic icon
                            ft.Text('islamic', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#81C784",  # Green background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Frame 6: History & Geography Subject
    six_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('history & geo', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#BA68C8',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[12], width=60, height=60),  # History icon
                            ft.Text('history & geo', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#6A1B9A",  # Purple background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Frame 7: English Subject
    seven_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('english', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#F57C00',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[7], width=60, height=60),  # English icon
                            ft.Text('english', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#FFB74D",  # Orange background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Frame 8: French Subject
    eghit_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('french', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#388E3C',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[11], width=60, height=60),  # French icon
                            ft.Text('french', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            padding=10,
            bgcolor="#81C784",  # Green background
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Frame 9: Civil Engineering Subject
    nine_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('city eng', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#BA68C8',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[3], width=60, height=60),  # Civil engineering icon
                            ft.Text('city eng', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#6A1B9A",  # Purple background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Frame 10: Mechanical Engineering Subject
    ten_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('mechanical eng', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#F57C00',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[19], width=60, height=60),  # Mechanical engineering icon
                            ft.Text('mechanical eng', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#FFB74D",  # Orange background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Frame 11: Electrical Engineering Subject
    eleven_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('electric eng', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#388E3C',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[6], width=60, height=60),  # Electrical engineering icon
                            ft.Text('electric eng', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#81C784",  # Green background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Frame 12: Process Engineering Subject
    twelve_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('process eng', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#BA68C8',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[23], width=60, height=60),  # Process engineering icon
                            ft.Text('process eng', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#6A1B9A",  # Purple background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Frame 13: Economy Subject
    thertine_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('economy', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#F57C00',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[5], width=60, height=60),  # Economy icon
                            ft.Text('economy', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#FFB74D",  # Orange background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Frame 14: Economic & Management Subject
    fourtine_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('economic & management', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#388E3C',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[23], width=60, height=60),  # Management icon
                            ft.Text('management', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#81C784",  # Green background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Frame 15: Accounting Management Subject
    feftine_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('accounting management', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#BA68C8',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[20], width=60, height=60),  # Accounting icon
                            ft.Text('accounting', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#6A1B9A",  # Purple background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Frame 16: German Language Subject
    sixtine_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('germany lng', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#F57C00',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[23], width=60, height=60),  # German language icon
                            ft.Text('germany lng', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#FFB74D",  # Orange background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Frame 17: Italian Language Subject
    seventine_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('italy lng', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#388E3C',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[23], width=60, height=60),  # Italian language icon
                            ft.Text('italy lng', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#81C784",  # Green background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Frame 18: Spanish Language Subject
    eghtine_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('spain lng', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#BA68C8',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[23], width=60, height=60),  # Spanish language icon
                            ft.Text('spain lng', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#6A1B9A",  # Purple background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Frame 19: Amazigh Language Subject
    nintine_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('amazigh lng', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#F57C00',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[23], width=60, height=60),  # Amazigh language icon
                            ft.Text('amazigh lng', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#FFB74D",  # Orange background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # Frame 20: Art Subject
    tweni_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:', color='white', weight=ft.FontWeight.BOLD, size=33, text_align=ft.TextAlign.CENTER),
                ft.Text('art', color='white', size=31, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#388E3C',
                    on_hover=animate_buttons,
                    content=ft.Row(
                        controls=[
                            ft.Image(src_base64=icons[14], width=60, height=60),  # Art icon
                            ft.Text('art', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ]
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            border=ft.border.all(3, 'black'),
            bgcolor="#81C784",  # Green background
            padding=10,
            width=300, height=400,
            alignment=ft.alignment.center,
            margin=ft.margin.only(top=20)
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
    )

    # =========================================================================
    # RESPONSIVE LAYOUT HANDLER
    # =========================================================================
    def page_resize(e):
        """
        Handle page resize events for responsive design
        Adjusts layout based on screen width (mobile vs desktop)
        """
        # Clear existing controls before rebuilding layout
        page.controls.clear()
        
        if page.width < 600:
            # MOBILE LAYOUT: Stack all frames vertically in a single column
            page.controls.append(
                ft.Column(
                    controls=[
                        first_frame, second_frame, therd_frame, fourth_frame, fifth_frame,
                        six_frame, seven_frame, eghit_frame, nine_frame, ten_frame,
                        eleven_frame, twelve_frame, thertine_frame, fourtine_frame, 
                        feftine_frame, sixtine_frame, seventine_frame, eghtine_frame, 
                        nintine_frame, tweni_frame
                    ]
                )
            )
            # Add back button for mobile navigation
            page.add(
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#81C784',
                    on_hover=animate_buttons, on_click=go_to_home,
                    content=ft.Text('Back', size=20, text_align=ft.TextAlign.CENTER)
                )
            )
        else:
            # DESKTOP LAYOUT: Arrange frames in rows of two with spacing
            page.controls.append(ft.Row(controls=[first_frame, second_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[fourth_frame, therd_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[fifth_frame, six_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[seven_frame, eghit_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[nine_frame, ten_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[eleven_frame, twelve_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[thertine_frame, fourtine_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[feftine_frame, sixtine_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[seventine_frame, eghtine_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[nintine_frame, tweni_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            
            # Add back button for desktop navigation
            page.add(
                ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#81C784',
                    on_hover=animate_buttons, on_click=go_to_home,
                    content=ft.Text('Back', size=20, text_align=ft.TextAlign.CENTER)
                )
            )

        page.update()  # Apply layout changes

    # =========================================================================
    # INITIALIZATION
    # =========================================================================
    page.on_resize = page_resize  # Set resize event handler
    page_resize(None)  # Trigger initial layout setup
    page.update()  # Final page update