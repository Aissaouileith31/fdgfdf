import flet as ft
from base64_string_icon_path import icons
hovering = False

def branch(page):
    def go_back(e):
        from lessons import lessons
        page.controls.clear()
        lessons(page)
        page.update()
    def go_to_home(e):
        from home import home
        page.controls.clear()
        home(page)
        page.update()
    def go_to_lessons_falsafa(e):
        import arabic.lessons.arabic_lessons_adab_falsafa.arabic_lessons as arabic_module
        page.controls.clear()
        arabic_module.arabic_lessons(page)
        page.update()
    def go_to_ar_lessons_sience(e):
        import arabic.lessons.arabic_lessons_sience.arabic_lessons as arabic_module
        page.controls.clear()
        arabic_module.arabic_lessons(page)
        page.update()

    def go_to_ar_lessons_oth_lng(e):
        import arabic.lessons.arabic_lessons_auther_lenguege.arabic_lessons as arabic_module
        page.controls.clear()
        arabic_module.arabic_lessons(page)
        page.update()


    def animate_buttons(e):
        global hovering
        if e.data == 'true' and not hovering:
            e.control.scale = 1.2
            hovering = True
        elif e.data == "false" and hovering:
            e.control.scale = 1
            hovering = False
        e.control.update()  # Fixed: update the control instead of page

    def open_drawer(e):
        # Fixed: Initialize drawer properly before opening
        if not hasattr(page, 'drawer') or page.drawer is None:
            page.drawer = ft.NavigationDrawer(
                bgcolor="#2F4F5F",
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
                                        on_click=go_to_home,  # Fixed: added on_click
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
                                ],
                                scroll='auto'
                            )
                        )
                    )
                ]
            )
        page.drawer.open = True
        page.update()

    page.appbar = ft.AppBar(
        bgcolor='#2F4F5F',
        title=ft.Text(
            'BAC DZ - lessons',
            size=20,
            weight='bold',
            text_align=ft.TextAlign.CENTER,
            offset=ft.Offset(0.1, 0),
            color='white'
        ),
        leading=ft.ElevatedButton(
            '| | |',
            on_click=open_drawer,
            on_hover=animate_buttons,
            color='black',
            bgcolor='white',
            height=40,
            width=40,
            offset=ft.Offset(0.2, 0)
        ),
        center_title=True
    )

    # ----- Frames (cards) -----
    first_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text("sience brench", color='white', size=33 , weight='bold', text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200,
                    height=60,
                    color='white',
                    bgcolor='#2F4F2F',
                    on_hover=animate_buttons,
                    on_click=go_to_ar_lessons_sience,
                    content=ft.Container(
                        content=ft.Stack([
                            ft.Text('sience brench', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ])
                    )
                )
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
    ], alignment=ft.MainAxisAlignment.CENTER)

    second_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('philosophy literatur ', color='white', weight='bold', size=33,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200,
                    height=60,
                    color='white',
                    bgcolor='#CC0000',
                    on_hover=animate_buttons,
                    on_click=go_to_lessons_falsafa,
                    content=ft.Container(
                        content=ft.Stack([
                            ft.Text('philosophy literatur ', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ])
                    )
                )  # Fixed: removed duplicate offset parameter
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
    ], alignment=ft.MainAxisAlignment.CENTER)

    therd_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('ahther lengueg', color='black', weight='bold', size=33, text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(
                    width=200,
                    height=60,
                    color='white',
                    bgcolor='#999900',
                    on_hover=animate_buttons,
                    on_click=go_to_ar_lessons_oth_lng,
                    content=ft.Container(
                        content=ft.Stack([
                            ft.Text('ahther lengueg', size=20, text_align=ft.TextAlign.CENTER, offset=ft.Offset(0, 0))
                        ])
                    )
                )
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
    ], alignment=ft.MainAxisAlignment.CENTER)

    back_button = ft.ElevatedButton(
                    width=200, height=60, color='white', bgcolor='#81C784',
                    on_hover=animate_buttons, on_click=go_back,
                    content=ft.Text('Back', size=20, text_align=ft.TextAlign.CENTER)
                )

    # ----- Responsive Layout -----
    def page_resize(e):  # Fixed: typo in function name
        page.controls.clear()

        if page.width < 600:
            # Mobile: 1 per row
            page.controls.append(
                ft.Column(
                    controls=[first_frame, second_frame, therd_frame],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20
                ),
                
            )
        else:
            # PC: 2 per row, then 1 per row
            page.controls.append(
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[first_frame, second_frame],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=50
                        ),
                        ft.Row(
                            controls=[therd_frame],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    spacing=40,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
            )
        page.add(back_button)
        page.update()

    page.on_resize = page_resize  # Fixed: use correct function name
    page_resize(None)  # Fixed: use correct function name