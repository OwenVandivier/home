import tkinter
import customtkinter
from tkinter import BOTTOM, messagebox
from tkinter.messagebox import showinfo

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        
        self.title("Switch")
        self.geometry("300x300")
        #self.iconbitmap("file_path_to_.ico")
        
        #Label 
        self.label = customtkinter.CTkLabel(self,
                                            text = "Switch")
        self.label.pack()
        
        self.entry = customtkinter.CTkEntry(self,
                                            height=25,
                                            width=170,
                                            fg_color="white",
                                            placeholder_text_color= "#1C94CF",
                                            text_color = "#1C94CF",
                                            placeholder_text= "Placeholder Text.")

        self.entry.pack(pady=5)        

        # Button
        self.button = customtkinter.CTkButton(self,
                                              text=("Button Text"),
                                              command=self.button_clicked)
        self.bind('<Return>', self.button_clicked)
        self.button.pack(pady=5)
        
        # Progress Bar
        self.progressBar = customtkinter.CTkProgressBar(self,
                                                        width = 300,
                                                        height = 25,
                                                        corner_radius=0,
                                                        progress_color= "green")
        self.progressBar.set(0)
        self.progressBar.pack(side=BOTTOM)
    
    # Button click action
    def button_clicked(self, event=None):
       pass
    
       
    def get_out(self):
        exit()

if __name__=='__main__':
    app = App()
    app.mainloop()