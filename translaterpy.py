import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class TranslatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Çeviri Uygulaması")
        self.geometry("500x300")  # Uygulama boyutunu ayarla

        self.translator = Translator()

        self.language_codes = {
            'English': 'en',
            'Spanish': 'es',
            'French': 'fr',
            'German': 'de',
            'Italian': 'it',
            'Russian': 'ru',
            'Turkish': 'tr',
            'Portuguese': 'pt',
            'Japanese': 'ja',
            # Ek dil ve dil kodlarını buraya ekleyebilirsiniz
        }

        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text="Metin:")
        self.label.pack()

        self.entry = ttk.Entry(self, width=30)
        self.entry.pack()

        self.language_label = ttk.Label(self, text="Dil:")
        self.language_label.pack()

        self.language_combo = ttk.Combobox(self, values=list(self.language_codes.keys()))
        self.language_combo.pack()

        self.button = ttk.Button(self, text="Çevir", command=self.translate_text)
        self.button.pack()

        self.translated_label = ttk.Label(self, text="Çeviri:")
        self.translated_label.pack()

    def translate_text(self):
        text = self.entry.get()
        selected_language = self.language_combo.get()

        if text and selected_language:
            code = self.language_codes[selected_language]
            translation = self.translator.translate(text, dest=code)
            self.translated_label.configure(text=translation.text)
        else:
            self.translated_label.configure(text="Metin ve dil seçimi gereklidir.")

if __name__ == "__main__":
    app = TranslatorApp()
    app.mainloop()
