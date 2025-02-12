from flet import *


def main(page: Page):
    page.window.width = 320
    page.window.height = 590
    page.bgcolor = colors.TRANSPARENT
    page.decoration = BoxDecoration(image=DecorationImage(
        src="images/back.jpg",
        fit= ImageFit.COVER
    )
    )
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.padding = 0
    page.fonts = {
        "Browser": "fonts/Browser.ttf",
        "beyonder": "fonts/beyonder.ttf"
    }
    page.update()

    h1 = Text(
        value='Mostadrif',
        size=34,
        font_family='Browser',
        color=Colors("white")
    )

    h2 = Text(
        value='whith Flet Python',
        size=8,
        color=colors.YELLOW,
        font_family='beyonder',
    )

    #img = Image(src="images/God.png", width=80, height=80)

    button = ElevatedButton(
        width=80,
        text='Button',
        color=colors.YELLOW,
        bgcolor=colors.WHITE12,
    )

    # Container central
    content_container = Container(
        width=200,
        height=300,
        border_radius=16,
        bgcolor=colors.WHITE12,
        blur=4,
        content=Column(
            controls=[h1, h2],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )
    )

    # Empiler les éléments sur l’image de fond
    page.add(
        Stack(
            controls=[
                

                # Conteneur principal
                Column(
                    controls=[
                        Container(content=content_container, alignment=alignment.center),
                        Container(content=button, alignment=alignment.bottom_center)
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    width=page.window.width,
                    height=page.window.height
                )
            ],
            width=page.window.width,
            height=page.window.height
        )
    )

if __name__ == '__main__':
    app(target=main, assets_dir="assets")
