import flet as ft
import sqlite3

conn = sqlite3.connect('interests_test.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS results             (name TEXT, interests TEXT)''')

def main(page: ft.Page):
    page.title = "Тест по интересам"    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    if __name__ == "__main__":
        page.window_maximized = True
        page.window_width = 720
        page.window_height = 480
    page.window_bgcolor = ft.colors.BLUE_GREY_100      
    page.padding = 20
    title = ft.Text("Выберите ваши интересы:", size=20, weight=ft.FontWeight.BOLD)
    name_field = ft.TextField(label="Интересы", hint_text="Например")
    interests = [        "Прогулки", "Спорт", "Музыка", "Кино", "Книги", "Путешествия",
        "Искусство", "Технологии", "Наука", "Кулинария", "Другое"    ]
    checkboxes = [ft.Checkbox(label=interest) for interest in interests]
    
    def save_results(e):
        name = name_field.value        
        selected_interests = ",".join([cb.label for cb in checkboxes if cb.value])
        # c.execute("INSERT INTO results VALUES (?, ?)", (name, selected_interests))     
        # conn.commit()
        name_field.value = ""        
        for cb in checkboxes:
            cb.value = False        
            page.snack_bar = ft.SnackBar(content=ft.Text("Результаты сохранены!"), open=True)
        
        page.route = "/accounts"
        page.update()
    save_button = ft.ElevatedButton("Сохранить", on_click=save_results, bgcolor=ft.colors.PURPLE_500)
    page.add(        
        ft.Column
        (
            [                title,
                name_field,
                ft.Column(checkboxes),                
                save_button
            ],            
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )    )

if __name__ == "__main__":
    ft.app(target=main)
    conn.close()
