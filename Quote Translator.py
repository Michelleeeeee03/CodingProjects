import flet as ft

def main(page: ft.Page):
    page.title = "Quote Translator"

    original_quote = "Minions, tonight we steal the moon!"
    translations = {
        "English": "Minions, tonight we steal the moon!",
        "Spanish": "Minions, ¡esta noche robamos la luna!",
        "French": "Minions, ce soir nous volons la lune!"}

    quote_text = ft.Text(value=original_quote, width=400, text_align=ft.TextAlign.CENTER)


    def update_quote(e):
        selected_language = options.value
        if selected_language in translations:
            quote_text.value = translations[selected_language]
        page.update()

    
    options = ft.RadioGroup(
        content=ft.Column(
            controls=[
                ft.Radio(value="English", label="English"),
                ft.Radio(value="Spanish", label="Spanish"),
                ft.Radio(value="French", label="French")
                ]), on_change=update_quote)


    page.add(
        ft.Column(
            [quote_text, options],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER))

ft.app(target=main)