#Purva Patel #100886734
#question 1
import tkinter as tk

class BlinkingText:
    def __init__(self, master):
        self.master = master
        self.master.title('Flashing text')
        self.canvas = tk.Canvas(self.master , width = 200, height = 100, bg = 'white')
        self.canvas.pack()
        self.text_item = self.canvas.create_text(100 , 50 , text = 'Stay Strong!' , fill = 'black')
        self.text_color = 'white'
        self.blink()

    def blink(self):
        if self.text_color == 'white':
            self.canvas.itemconfigure(self.text_item, fill='black')
            self.text_color = 'black'
        else:
            self.canvas.itemconfigure(self.text_item, fill='white')
            self.text_color = 'white'
        self.master.after(500, self.blink)

root_window = tk.Tk()
blinking_text = BlinkingText(root_window)
root_window.mainloop()
