from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFloatingActionButton, MDRectangleFlatIconButton





class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        icon_type = MDTextField(text="Enter here:", pos_hint={'center_x':0.5,'center_y':0.8},size_hint_x=None,width=200)
        icon_btn3 = MDRectangleFlatIconButton(text="Share",icon='share',pos_hint={'center_x': 0.5, 'center_y': 0.75})
        icon_btn = MDRectangleFlatIconButton(text="Java",icon='language-java', pos_hint={'center_x':0.5,'center_y':0.5})
        icon_btn1 = MDRectangleFlatIconButton(text = "Python",icon='language-python', pos_hint={'center_x': 0.5, 'center_y': 0.4})
        icon_btn2 = MDRectangleFlatIconButton(text = "PHP",icon='language-php', pos_hint={'center_x': 0.5, 'center_y': 0.6})
        c1 = MDFloatingActionButton(icon='telegram',pos_hint={'center_x': 0.1, 'center_y': 0.2})
        c2 = MDFloatingActionButton(icon='whatsapp',pos_hint={'center_x': 0.3, 'center_y': 0.2})
        c3 = MDFloatingActionButton(icon='facebook',pos_hint={'center_x': 0.5, 'center_y': 0.2})
        c4 = MDFloatingActionButton(icon='youtube',pos_hint={'center_x': 0.7, 'center_y': 0.2})
        c5 = MDFloatingActionButton(icon='twitter', pos_hint={'center_x': 0.9, 'center_y': 0.2})
        screen.add_widget(icon_btn)
        screen.add_widget(icon_btn1)
        screen.add_widget(icon_btn2)
        screen.add_widget(icon_btn3)
        screen.add_widget(icon_type)
        screen.add_widget(c1)
        screen.add_widget(c2)
        screen.add_widget(c3)
        screen.add_widget(c4)
        screen.add_widget(c5)

        return screen

MainApp().run()