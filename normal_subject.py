import flet as ft
from base64_string_icon_path import icons

hovering = False

def normal_subject(page):
    page.padding = 1
    def go_to_home(e):
        from home import home
        page.controls.clear()
        home(page)
        page.update()
    def animate_buttons(e):
        global hovering
        if e.data == 'true' and not hovering:

            e.control.scale = 1.2
            hovering = True
        elif e.data == "false" and hovering:
            e.control.scale=1
            hovering = False
        page.update()

    def open_drawer(e):
        page.drawer.open = True
        page.update()
    page.drawer = ft.NavigationDrawer(
        bgcolor="#2F4F5F",
        controls=[ft.ListTile(ft.Container(content=ft.Column(controls=[
            ft.ElevatedButton(bgcolor='#8A0000',color='white',height=60,on_hover=animate_buttons,on_click=go_to_home,content=ft.Row(controls=[ft.Image(src_base64=icons[13],width=50,height=50),ft.Text('home',size=20,text_align=ft.TextAlign.CENTER)])),
            ft.ElevatedButton(bgcolor='#8A0000',color="white",height=60,on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[0],width=50,height=50),ft.Text('aboutus',size=20,text_align=ft.TextAlign.CENTER)])),
            ft.ElevatedButton(bgcolor='#8A0000',color="white",height=60,on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[0],width=50,height=50),ft.Text('give feedback',size=20,text_align=ft.TextAlign.CENTER)])),
            ],
            scroll='auto'))

            )])

    page.appbar = ft.AppBar(
        bgcolor='#2F4F5F',
        title=ft.Text('BAC DZ - lessons',size=20,weight='bold',text_align=ft.TextAlign.CENTER,offset=ft.Offset(0.1,0),color='white'),
        leading=ft.ElevatedButton('| | |',on_click=open_drawer,on_hover=animate_buttons,color='black',bgcolor='white',height=40,width=40,offset=ft.Offset(0.2,0)),
        center_title=True)

    first_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('Arabic',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#F57C00',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[2],width=50,height=50),ft.Text('Arabic',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#FFB74D",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    second_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('Math',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#388E3C',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[16],width=50,height=50),ft.Text('Math',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#81C784",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    therd_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('fizics',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#F57C00',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[10],width=60,height=60),ft.Text('fizics',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#FFB74D",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    fourth_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('islamic iducation',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#388E3C',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[15],width=60,height=60),ft.Text('islamic',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#81C784",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    fifth_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('history & geo',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#BA68C8',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[12],width=60,height=60),ft.Text('history & geo',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#6A1B9A",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    six_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('english',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#F57C00',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[7],width=60,height=60),ft.Text('english',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#FFB74D",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    seven_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('frensh',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#388E3C',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[11],width=60,height=60),ft.Text('frensh',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            padding=10,
            bgcolor="#81C784",
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    eghit_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('city eng',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#BA68C8',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[3],width=60,height=60),ft.Text('city eng',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#6A1B9A",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    nine_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('mecanic eng',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#F57C00',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[19],width=60,height=60),ft.Text('mecanic eng',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#FFB74D",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    ten_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('electic eng',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#388E3C',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[6],width=60,height=60),ft.Text('electic eng ',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#81C784",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    eleven_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('prosess eng',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#BA68C8',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[23],width=60,height=60),ft.Text('prosess eng',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#6A1B9A",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    twelve_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('economy',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#F57C00',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[5],width=60,height=60),ft.Text('economy',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#FFB74D",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    thertine_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('econommic & managemaent',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#388E3C',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[23],width=60,height=60),ft.Text('managemaent',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#81C784",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    fourtine_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('acounting managemaent',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#BA68C8',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[20],width=60,height=60),ft.Text('acounting',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#6A1B9A",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    feftine_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('germany lng',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#F57C00',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[23],width=60,height=60),ft.Text('germany lng',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#FFB74D",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    sixtine_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('italy lng',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#388E3C',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[23],width=60,height=60),ft.Text('italy lng',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#81C784",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    seventine_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('spaine lng',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#BA68C8',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[23],width=60,height=60),ft.Text('spaine lng',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#6A1B9A",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    eghtine_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('amazigh lng',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#F57C00',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[23],width=60,height=60),ft.Text('amazigh lng',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#FFB74D",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    nintine_frame = ft.Row([
        ft.Container(
            content=ft.Column([
                ft.Text('lessons and summaries in:',color='white',weight='bold',size=33,text_align=ft.TextAlign.CENTER),
                ft.Text('art',color='white',size=31,text_align=ft.TextAlign.CENTER),
                ft.ElevatedButton(width=200,height=60,color='white',bgcolor='#388E3C',on_hover=animate_buttons,content=ft.Row(controls=[ft.Image(src_base64=icons[14],width=60,height=60),ft.Text('art',size=20,text_align=ft.TextAlign.CENTER,offset=ft.Offset(0,0))]))


                ],
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER

                ),
            border=ft.border.all(3,'black'),
            bgcolor="#81C784",
            padding=10,
            width=300,
            height=400,
            alignment = ft.alignment.center,
            margin = ft.margin.only(top=20)
            )
        
            


        ],
        alignment= ft.MainAxisAlignment.CENTER
        )

    def page_resaize(e):
        page.controls.clear()
        if page.width < 600:
            page.controls.append(ft.Column(controls=[
                first_frame, second_frame, therd_frame, fourth_frame, fifth_frame, 
                six_frame, seven_frame, eghit_frame, nine_frame, ten_frame, 
                eleven_frame, twelve_frame, thertine_frame, fourtine_frame, 
                feftine_frame, sixtine_frame, seventine_frame, eghtine_frame, 
                nintine_frame
            ]))
            page.add(ft.ElevatedButton(
                width=200, height=60, color='white', bgcolor='#8A0000',
                on_hover=animate_buttons, on_click=go_to_home,
                content=ft.Text('Back', size=20, text_align=ft.TextAlign.CENTER)
            ))
        else:
            page.controls.append(ft.Row(controls=[first_frame, second_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[therd_frame, fourth_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[fifth_frame, six_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[seven_frame, eghit_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[nine_frame, ten_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[eleven_frame, twelve_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[thertine_frame, fourtine_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[feftine_frame, sixtine_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[seventine_frame, eghtine_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))
            page.controls.append(ft.Row(controls=[nintine_frame], alignment=ft.MainAxisAlignment.CENTER, spacing=100))

        page.update()

    page.on_resize = page_resaize
    page_resaize(None)
    page.update()