import flet as ft

def main(page:ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.SPACE_BETWEEN
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Button Types"
    page.window.width = 400
    page.window.height = 700
    page.fonts = {
        "Browser": "fonts/Browser.ttf"
    }
    page.appbar = ft.AppBar(
        bgcolor = "#034582",
        color = "#ffffff",
        center_title =True,
        title = ft.Text(value="Button Types")
    )

    page.add(
        ft.Column(
            controls=[
                ft.Container(padding=20),
                ft.Text("Hello Word",size=40,font_family="Browser",color="#ffffff"),
                ft.Container(padding=30),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(text="ElevatedButton",
                                          bgcolor="yellow",
                                          color="black"

                        ),
                        ft.IconButton(icon=ft.icons.DANGEROUS,
                              icon_color="blue400",
                              tooltip="Pause record",
                              icon_size=40),
                        ft.OutlinedButton(text="OutlinedButton",
    

                        )
                    ],alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                ft.Container(padding=20),
                
                ft.Row(
                    controls=[
                        ft.Icon(name='favorite',color=ft.colors.PINK,size=50),
                        ft.Icon(name='AUDIOTRACK',color=ft.colors.YELLOW,size=50),
                        ft.Icon(name='BEACH_ACCESS',color=ft.colors.ORANGE,size=50)
                    ],alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),ft.Container(padding=30),
                ft.Column(
                    controls=[
                        ft.TextField(label="Name",
                        hint_text = "Your Name",
                        width =280,
                        border_color = "yellow",
                        cursor_color = "yellow",
                        border_radius=ft.border_radius.all(20),
                        icon=ft.Icons.ACCESS_ALARM,
                        color=ft.Colors.PINK_300),
                        ft.Container(padding=10),
                        ft.TextField(label="Password",
                        hint_text = "Your password",
                        width =280,
                        border_color = "yellow",
                        cursor_color = "yellow",
                        password =True,
                        can_reveal_password =True,
                        border_radius=ft.border_radius.all(20),
                        icon=ft.Icons.ACCESS_ALARM,
                        color=ft.Colors.PINK_300),
                   ],alignment=ft.MainAxisAlignment.SPACE_AROUND,
                )
                
                
            ],alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        




        
    )
    page.update()
ft.app(target=main,assets_dir="assets")
