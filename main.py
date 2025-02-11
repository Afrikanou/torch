from flet import* 

def main(page:Page):
    page.bgcolor = '#db99ff'
    page.scroll = 'auto'
    page.window.width = 340
    page.window.height = 640
    page.window.top = 1
    page.window.left = 200
    page.theme_mode = ThemeMode.LIGHT
    page.fonts = {
        "Browser": "fonts/Browser.ttf",
        "Against": "fonts/against.ttf",
        "Bird": "fonts/bird.ttf"}
    
    
    
    page.add(
        AppBar(
            title=Text('    '),
            color='white',
            bgcolor='#800080',
            actions=[
                IconButton(icons.SETTINGS,on_click=...)
            ]
        ),
        Row([
            Text('\nFlash Light',size=34,color='#1e105c',font_family='Browser')
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            Image(src='images/torch.png',width=160,height=300)
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            Text('',size=20)
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            ElevatedButton(
                "ON",
                width=100,
                icon=icons.PLAY_ARROW,
                style=ButtonStyle(
                    bgcolor='#800080',
                    color='#ffffff',
                    padding=15,
                    shape=ContinuousRectangleBorder(radius=100)
                ),on_click=...
            ),
            
            Text('  ',size=50),
            ElevatedButton(
                "OFF",
                width=100,
                icon=icons.PLAY_DISABLED,
                style=ButtonStyle(
                    bgcolor='#800080',
                    color='#ffffff',
                    padding=15,
                    shape=ContinuousRectangleBorder(radius=100)
                ),on_click=...
            )
        ],alignment=MainAxisAlignment.CENTER)

    )
    


    page.update()


app(main, assets_dir="assets")
