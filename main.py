from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class Calculator(App):
    def build(self):
        widget_root = BoxLayout(orientation="vertical")
        label_op = Label(size_hint_y=0.75, font_size=51)
        
        symbol_button = ('1', '2', '3', '+',
                         '4', '5', '6', '*',
                         '7', '8', '9', '.',
                         '0', '/', '-', '=')
        
        grid_button = GridLayout(cols=4, size_hint_y=2)
        
        for symbol in symbol_button:
            btn = Button(text=symbol)
            btn.bind(on_press=self.text_print_button)  # Bind correctly
            grid_button.add_widget(btn)

        button_clear = Button(text="CE", size_hint_y=None, height=100)
        button_clear.bind(on_press=self.label_clear)  # Bind correctly

        grid_button.children[0].bind(on_press=self.result)  # Bind the result button

        widget_root.add_widget(label_op)
        widget_root.add_widget(grid_button)
        widget_root.add_widget(button_clear)
        
        return widget_root

    def text_print_button(self, instance):
        label_op = self.root.children[2]  # Get the label from root (3rd child)
        label_op.text += instance.text

    def result(self, instance):
        label_op = self.root.children[2]  # Get the label from root
        try:
            label_op.text = str(eval(label_op.text))
        except Exception as e:
            label_op.text = "Error"  # Display error message

    def label_clear(self, instance):
        label_op = self.root.children[2]  # Get the label from root
        label_op.text = ""

if __name__ == '__main__':
    Calculator().run()
