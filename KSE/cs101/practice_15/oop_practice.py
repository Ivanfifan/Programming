class Button:
    def __init__(self,if_push, name):
        self.name = None
        self.if_push = if_push
        if if_push:
            self.color_LED = 'Red'
        else:
            self.color_LED = 'Blank'
        self.color = 'Silver'
        
    def action(self, name):
        self.name = name
        
    def get_name(self):
        if self.name == 1:
            return
        elif self.name == 'call':
            return 'Calling to service'

class Lift:
    def __init__(self):
        self.where_am_i = 0
    def position(self,where_am_i):
        self.where_am_i = where_am_i

button1 = Button(True, 1)
button2 = Button(False, 2)
button_call = Button(True, 'call')

print(button1.color_LED == button2.color_LED)