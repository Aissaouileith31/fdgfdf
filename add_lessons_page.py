import sqlite3
import flet as ft  # Import flet with alias ft
from base64_string_icon_path import icons

# Global variable for hover animation state
hovering = False

def add_lessons(page):
    """
    Page for adding Arabic lesson links to the database
    """
    
    def go_to_home(e):
        """Navigate back to home page"""
        from home import home
        page.controls.clear()  # Clear current page controls
        home(page)  # Load home page
        page.update()  # Update the page
    
    # Page configuration
    page.title = "Link App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 300

    def animate_buttons(e):
        """Animate buttons on hover effect"""
        global hovering
        if e.data == 'true' and not hovering:
            # Scale up when hovering starts
            e.control.scale = 1.2
            hovering = True
        elif e.data == "false" and hovering:
            # Scale back to normal when hovering ends
            e.control.scale = 1
            hovering = False
        page.update()  # Update page to reflect changes

    def open_drawer(e):
        """Open navigation drawer"""
        page.drawer.open = True
        page.update()

    # Define navigation drawer with menu options
    page.drawer = ft.NavigationDrawer(
        bgcolor="#2F4F5F",  # Dark blue-gray background
        controls=[
            ft.ListTile(
                ft.Container(
                    content=ft.Column(
                        controls=[
                            # Home button
                            ft.ElevatedButton(
                                bgcolor="#8A0000",  # Dark red background
                                color="white",  # White text
                                height=60,
                                on_hover=animate_buttons,  # Hover animation
                                on_click=go_to_home,  # Navigation action
                                content=ft.Row(
                                    controls=[
                                        ft.Image(src_base64=icons[13], width=50, height=50),  # Home icon
                                        ft.Text("home", size=20, text_align=ft.TextAlign.CENTER),
                                    ]
                                ),
                            ),
                            # About Us button
                            ft.ElevatedButton(
                                bgcolor="#8A0000",
                                color="white",
                                height=60,
                                on_hover=animate_buttons,
                                content=ft.Row(
                                    controls=[
                                        ft.Image(src_base64=icons[0], width=50, height=50),  # About icon
                                        ft.Text("about us", size=20, text_align=ft.TextAlign.CENTER),
                                    ]
                                ),
                            ),
                            # Feedback button
                            ft.ElevatedButton(
                                bgcolor="#8A0000",
                                color="white",
                                height=60,
                                on_hover=animate_buttons,
                                content=ft.Row(
                                    controls=[
                                        ft.Image(src_base64=icons[0], width=50, height=50),  # Feedback icon
                                        ft.Text("give feedback", size=20, text_align=ft.TextAlign.CENTER),
                                    ]
                                ),
                            ),
                        ],
                        scroll="auto",  # Enable scrolling if content overflows
                    )
                )
            )
        ],
    )

    # AppBar configuration
    page.appbar = ft.AppBar(
        bgcolor="#2F4F5F",  # Match drawer background
        title=ft.Text(
            "BAC DZ - lessons",
            size=20,
            weight="bold",
            text_align=ft.TextAlign.CENTER,
            offset=ft.Offset(0.1, 0),  # Slight horizontal offset
            color="white",
        ),
        leading=ft.ElevatedButton(  # Hamburger menu button
            "| | |",
            on_click=open_drawer,  # Open drawer on click
            on_hover=animate_buttons,
            color="black",
            bgcolor="white",
            height=40,
            width=40,
            offset=ft.Offset(0.2, 0),
        ),
        center_title=True,  # Center the title
    )

    # Variable to store dropdown selection
    dropdown_value = None

    # Page header text
    title_text = ft.Text(
        "Add Arabic Lesson Link",
        size=22,
        weight="bold",
        color="blue"
    )

    # Input field for Google Drive link
    link_field = ft.TextField(
        hint_text="Paste the Google Drive link here",
        width=350,
        filled=True  # Filled background
    )

    def dropdown_change(e):
        """Handle dropdown selection changes"""
        nonlocal dropdown_value
        dropdown_value = e.control.value  # Store selected value

    def publish(e):
        """Publish the link to the database"""
        link = link_field.value.strip()  # Get and clean link input
        
        # Validate link input
        if not link:
            # Show error message if link is empty
            page.controls.append(ft.Text("⚠️ Please enter a link.", color="red"))
            page.update()
            return
        if "drive.google.com" not in link:
            # Show error if link is not a Google Drive link
            page.controls.append(ft.Text("❌ Invalid link. Please enter a valid Google Drive link.", color="red"))
            page.update()
            return
        
        # Process based on subject selection
        if dropdown_value == 'arabic':
            if options_group.value == 'sience_brensh':
                # Save to science branch database
                try:
                    arabic_db_path = 'arabic/lessons/arabic_lessons_sience/arabic_lessons.db'
                    conn = sqlite3.connect(arabic_db_path)
                    cursor = conn.cursor()
                    # Insert link into database
                    cursor.execute('INSERT INTO arabic_lessons (link) VALUES (?)', (link,))
                    conn.commit()  # Save changes
                    conn.close()  # Close connection

                    link_field.value = ''  # Clear input field
                    # Show success message
                    page.controls.append(ft.Text("✅ Link added successfully!", color="green"))
                except Exception as ex:
                    # Show error message
                    page.controls.append(ft.Text(f"❌ Error: {str(ex)}", color="red"))
                    page.update()

            elif options_group.value == "authe_lenguege":
                # Save to other language database
                try:
                    arabic_db_path = r'arabic/lessons/arabic_lessons_auther_lenguege/arabic_lessons.db'
                    conn = sqlite3.connect(arabic_db_path)
                    cursor = conn.cursor()
                    cursor.execute('INSERT INTO arabic_lessons (link) VALUES (?)', (link,))
                    conn.commit()
                    conn.close()

                    link_field.value = ''
                    page.controls.append(ft.Text("✅ Link added successfully!", color="green"))
                except Exception as ex:
                    page.controls.append(ft.Text(f"❌ Error: {str(ex)}", color="red"))
                    page.update()
            elif options_group.value == "philosophy_literatur":
                # Save to philosophy & literature database
                try:
                    arabic_db_path = r'arabic/lessons/arabic_lessons_adab_falsafa/arabic_lessons.db'
                    conn = sqlite3.connect(arabic_db_path)
                    cursor = conn.cursor()
                    cursor.execute('INSERT INTO arabic_lessons (link) VALUES (?)', (link,))
                    conn.commit()
                    conn.close()

                    link_field.value = ''
                    page.controls.append(ft.Text("✅ Link added successfully!", color="green"))
                except Exception as ex:
                    page.controls.append(ft.Text(f"❌ Error: {str(ex)}", color="red"))
                    page.update()

    # Submit button
    submit_button = ft.ElevatedButton(
        text="Publish",
        on_click=publish,  # Call publish function on click
        bgcolor="blue",
        color="white"
    )

    # Radio group for branch selection
    options_group = ft.RadioGroup(
        content=ft.Column(
            [
                # Science branch option
                ft.Row([ft.Radio(value="sience_brensh", label="Science branch", fill_color="white", label_style=ft.TextStyle(color="white"))], 
                       alignment=ft.MainAxisAlignment.CENTER),
                # Philosophy & Literature option
                ft.Row([ft.Radio(value="philosophy_literatur", label="Philosophy & Literature", fill_color="white", label_style=ft.TextStyle(color="white"))], 
                       alignment=ft.MainAxisAlignment.CENTER),
                # Other language option
                ft.Row([ft.Radio(value="authe_lenguege", label="Other language", fill_color="white", label_style=ft.TextStyle(color="white"))], 
                       alignment=ft.MainAxisAlignment.CENTER),
            ],
            spacing=10,  # Space between options
        )
    )

    # Subject dropdown selection
    subject = ft.Dropdown(
        label='Choose the subject',
        color="white",
        width=200,
        bgcolor="white",
        label_style=ft.TextStyle(color="white"),  # Added white label color
        options=[
            ft.dropdown.Option('arabic'),
            ft.dropdown.Option('math'),
            ft.dropdown.Option('since'),
            ft.dropdown.Option('phyzic'),
            ft.dropdown.Option('history & geo'),
            ft.dropdown.Option('eslamic ed'),
            ft.dropdown.Option('electric eng'),
            ft.dropdown.Option('mecanic eng'),
            ft.dropdown.Option('civil eng'),
            ft.dropdown.Option('prosess eng'),
            ft.dropdown.Option('english'),
            ft.dropdown.Option('frensh'),
            ft.dropdown.Option('economy'),
            ft.dropdown.Option('law'),
            ft.dropdown.Option('econommic & managemaent'),
            ft.dropdown.Option('acounting '),
            ft.dropdown.Option('germany'),
            ft.dropdown.Option('spanish'),
            ft.dropdown.Option('italy'),
            ft.dropdown.Option('art'),
            ft.dropdown.Option('amazigh')
        ],
        on_change=dropdown_change  # Handle selection changes
    )

    # Set page controls (main content)
    page.controls = [
        ft.Container(
            content=ft.Column(
                [
                    title_text,      # Page title
                    link_field,      # Link input field
                    subject,         # Subject dropdown
                    ft.Text('Choose branch', size=22,color='white', text_align=ft.TextAlign.CENTER),  # Branch selection label
                    options_group,   # Branch radio buttons
                    submit_button,   # Publish button
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Center vertically
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Center horizontally
                spacing=20,  # Space between elements
            ),
            alignment=ft.alignment.center,  # Center container content
        )
    ]
    page.update()  # Apply changes to the page