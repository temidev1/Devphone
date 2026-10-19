import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class DevPhoneLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Preview
        self.preview = Label(text="[Live Preview Area]", size_hint_y=0.4)
        self.add_widget(self.preview)

        # Editor
        self.editor = TextInput(
            text="<h1>Hello DevPhone!</h1>",
            size_hint_y=0.4,
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(0, 1, 0, 1)
        )
        self.add_widget(self.editor)

        # Run Button
        btn = Button(text="RUN CODE", size_hint_y=0.2)
        btn.bind(on_press=self.run_code)
        self.add_widget(btn)

    def run_code(self, instance):
        self.preview.text = f"Simulated Output:\n{self.editor.text}"

class DevPhoneApp(App):
    def build(self):
        return DevPhoneLayout()

if __name__ == '__main__':
    DevPhoneApp().run()
