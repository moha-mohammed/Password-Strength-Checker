import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import checker  # import your password checker

kivy.require("2.3.1")


class PasswordApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.input = TextInput(
            hint_text="Enter your password",
            multiline=False,
            password=True,
            size_hint=(1, 0.2),
        )
        layout.add_widget(self.input)

        check_button = Button(
            text="Check Strength",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 0.8, 1),
        )
        check_button.bind(on_press=self.check_strength)
        layout.add_widget(check_button)

        self.result_label = Label(
            text="",
            size_hint=(1, 0.2),
            color=(1, 1, 1, 1),  # default white
        )
        layout.add_widget(self.result_label)

        return layout

    def check_strength(self, instance):
        password = self.input.text
        if password.strip() == "":
            self.result_label.text = "Please enter a password ❗"
            self.result_label.color = (1, 0, 0, 1)  # red
        else:
            strength = checker.check_strength(password)
            self.result_label.text = f"Strength: {strength}"

            # Color by strength
            if strength == "Weak":
                self.result_label.color = (1, 0, 0, 1)  # Red
            elif strength == "Medium":
                self.result_label.color = (1, 1, 0, 1)  # Yellow
            else:  # Strong
                self.result_label.color = (0, 1, 0, 1)  # Green


if __name__ == "__main__":
    PasswordApp().run()
