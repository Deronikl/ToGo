import flet as ft
import sqlite3

def main(page: ft.Page):
    page.title = "registration"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    if __name__ == "__main__":
        page.window_maximized = True
        page.window_width = 720
        page.window_height = 480

    def register(e):
        db = sqlite3.connect('it.proger')
        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            login TEXT,
            pass TEXT
        )""")
        cur.execute(f"INSERT INTO users VALUES(NULL, '{user_login.value}', '{user_pass.value}')")
        
        db.commit()
        db.close()

        user_login.value = ''
        user_pass.value = ''
        btn_reg.text = 'Добавлено'
        page.route = "/interest"
        page.update()

    def validate(e):
        if all([user_login.value, user_pass.value]):
            btn_reg.disabled = False
            btn_auth.disabled = False
        else:
            btn_reg.disabled = True
            btn_auth.disabled = True
        page.update()


    def auth_user(e):
        db = sqlite3.connect('it.proger')
        cur = db.cursor()
        cur.execute(f"SELECT * FROM users WHERE login = '{user_login.value}' AND pass = '{user_pass.value}'")
        if cur.fetchone() != None:
            user_login.value = ''
            user_pass.value = ''
            btn_auth.text = 'Авторизовано'
            page.route = "/profile"
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text('Неверно введенные данные!'))
            page.snack_bar.open = True
            page.update()

        db.commit()
        db.close()

        
    user_login = ft.TextField(label='Логин', width=200, on_change=validate)
    user_pass = ft.TextField(label='Пароль', password=True, width=200, on_change=validate)
    btn_reg = ft.OutlinedButton(text='Добавить', width=200, on_click=register, disabled=True)
    btn_auth = ft.OutlinedButton(text='Авторизовать', width=200, on_click=auth_user, disabled=True)

    panel_register = ft.Row(
        [
            ft.Column(
                [
                    ft.Text('Регистрация'),
                    user_login,
                    user_pass,
                    btn_reg
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER

    )

    panel_auth = ft.Row(
        [
            ft.Column(
                [
                    ft.Text('Авторизация'),
                    user_login,
                    user_pass,
                    btn_auth
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    def navigate(e):
        index = page.navigation_bar.selected_index
        page.clean()

        if index == 0: page.add(panel_register)
        if index == 1: page.add(panel_auth)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.VERIFIED_USER, label="Регистрация"),
            ft.NavigationDestination(icon=ft.icons.VERIFIED_USER_OUTLINED, label="Авторизация"),
        ], on_change=navigate
    )

    page.add(panel_register)

if __name__ == "__main__":
    ft.app(target=main)
