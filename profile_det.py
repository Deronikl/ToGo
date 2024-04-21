import flet as ft
import window_map_with_search as mp
import product_list as pl

def main(page: ft.Page):
    page.title = "Flet app"
    page.theme_mode = 'dark'
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    if __name__=="__main__":
        page.window_maximized = True
        page.window_width = 720
        page.window_height = 480

    def cange_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'

        page.update()

    def open_map(e):
        mp.run()
    def open_cor(e):
        pl.run()

    btn_back = ft.IconButton(ft.icons.ARROW_BACK_IOS_NEW_OUTLINED, icon_color=ft.colors.PURPLE_300, icon_size=40, tooltip= "Вернуться")
    btn_chg = ft.IconButton(ft.icons.SUNNY, on_click=cange_theme, tooltip="Сменить тему")
    btn_map = ft.IconButton(ft.icons.MAP_OUTLINED,on_click=open_map, tooltip="К карте")
    btn_cor = ft.IconButton(ft.icons.SHOPPING_CART_ROUNDED,on_click=open_cor, tooltip='Корзина')
    #верхняя строка
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.icons.ARROW_BACK_IOS_NEW_OUTLINED, icon_size=40, tooltip= "Вернуться"),
        leading_width=40,
        title=ft.Text("Личный кабинет"),
        center_title=True,
        bgcolor= ft.colors.DEEP_PURPLE_400,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        text="Настройки", checked=False,
                    ),
                ]
            ),
            btn_cor,
            btn_map,
            btn_chg,
            ft.IconButton(ft.icons.NOTIFICATIONS_ON_OUTLINED, tooltip="Уведомления"),
            
        ],
    )

    #ава + ФИО без О
    page.add(
        ft.Row(
            [
                          
                ft.Column(
                    [
                        ft.Container(ft.IconButton(ft.icons.ACCOUNT_BOX, icon_size=200 )),
                    ],
                ),
                
            ], alignment=ft.MainAxisAlignment.CENTER
            
        ),
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Container(ft.Text('Дарья Багатюк', color=ft.colors.PURPLE_300, size = 40, weight=ft.FontWeight.W_500))
                    ], 
                ),
            ], alignment=ft.MainAxisAlignment.CENTER
        )
        
    )


    page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text('Друзья', theme_style=ft.TextThemeStyle.HEADLINE_LARGE, weight=ft.FontWeight.W_600),
                            ft.Row(
                                [
                                    ft.Text('Федька Пупкин', theme_style=ft.TextThemeStyle.TITLE_LARGE),
                                    ft.Icon(name=ft.icons.CIRCLE_SHARP, color=ft.colors.GREEN_ACCENT_700),
                                ],
                            ),
                            ft.Row(
                                [
                                    ft.Text('Федька Пупкин', theme_style=ft.TextThemeStyle.TITLE_LARGE),
                                    ft.Icon(name=ft.icons.CIRCLE_SHARP, color=ft.colors.GREEN_ACCENT_700),
                                ],
                            ),
                            ft.Row(
                                [
                                    ft.Text('Федька Пупкин', theme_style=ft.TextThemeStyle.TITLE_LARGE),
                                    ft.Icon(name=ft.icons.CIRCLE_SHARP, color=ft.colors.GREEN_ACCENT_700),
                                ],
                            ),
                            ft.Row(
                                [
                                    ft.Text('Федька Пупкин', theme_style=ft.TextThemeStyle.TITLE_LARGE),
                                    ft.Icon(name=ft.icons.CIRCLE_OUTLINED, color=ft.colors.GREEN_ACCENT_700),
                                ],
                            ),
                            ft.Row(
                                [
                                    ft.Text('Федька Пупкин', theme_style=ft.TextThemeStyle.TITLE_LARGE),
                                    ft.Icon(name=ft.icons.CIRCLE_OUTLINED, color=ft.colors.GREEN_ACCENT_700),
                                ],
                            ),
ft.IconButton(ft.icons.KEYBOARD_DOUBLE_ARROW_DOWN_OUTLINED, icon_color=ft.colors.BLACK, icon_size=50),
                        ],
                    ),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.DEEP_PURPLE_400,
                    width=300,
                    height=360,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable with Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text('Мои Интересы', theme_style=ft.TextThemeStyle.HEADLINE_LARGE, weight=ft.FontWeight.W_600),
                            ft.Row(
                                [
                                    ft.Icon(name=ft.icons.LOCAL_BAR_ROUNDED, color=ft.colors.RED_500),
                                    ft.Text('Бары', theme_style=ft.TextThemeStyle.TITLE_LARGE),
                                ],
                            ),
                            ft.Row(
                                [
                                    ft.Icon(name=ft.icons.DIRECTIONS_WALK_OUTLINED, color=ft.colors.YELLOW),
                                    ft.Text('Парки', theme_style=ft.TextThemeStyle.TITLE_LARGE),
                                ],
                            ),
                            ft.Row(
                                [
                                    ft.Icon(name=ft.icons.MIC_EXTERNAL_ON_ROUNDED, color=ft.colors.BLACK),
                                    ft.Text('Караоке', theme_style=ft.TextThemeStyle.TITLE_LARGE),
                                ],
                            ),
                        ],
                    ),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.DEEP_PURPLE_400,
                    width=300,
                    height=360,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable with Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text('Часто посещаемые места', theme_style=ft.TextThemeStyle.HEADLINE_SMALL, weight=ft.FontWeight.W_600),
                            ft.Row(
                                [
                                    ft.IconButton(ft.icons.MAP, icon_color=ft.colors.DEEP_ORANGE),
                                    ft.Text('Парк им.Горького', theme_style=ft.TextThemeStyle.TITLE_LARGE, weight=ft.FontWeight.W_400),
                                ],
                            ),
                            ft.Row(
                                [
                                    ft.IconButton(ft.icons.MAP, icon_color=ft.colors.DEEP_ORANGE),
                                    ft.Text('Бар "Альпака"', theme_style=ft.TextThemeStyle.TITLE_LARGE, weight=ft.FontWeight.W_400),
                                ],
                            ),
                            ft.Row(
                                [
                                    ft.IconButton(ft.icons.MAP, icon_color=ft.colors.DEEP_ORANGE),
                                    ft.Text('Караоке "7sky"', theme_style=ft.TextThemeStyle.TITLE_LARGE, weight=ft.FontWeight.W_400),
                                ],
                            ),
                        ],
                    ),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.DEEP_PURPLE_400,
                    width=300,
                    height=360,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable with Ink clicked!"),
                ),
            ], alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__=="__main__":
    ft.app(target=main)
