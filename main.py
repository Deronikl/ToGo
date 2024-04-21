import flet as ft
import accounts as ac
import intresting as intr
import profile_det as pro

def main(page: ft.Page):
    def route_change(e: ft.RouteChangeEvent):
        page.clean()
        if page.route == "/accounts":
            ac.main(page)
        if page.route == "/interest":
            intr.main(page)
        if page.route == "/profile":
            pro.main(page)

    page.window_maximized =True
    page.window_width = 720
    page.window_height = 480
    page.on_route_change = route_change
    ac.main(page)


ft.app(target=main)