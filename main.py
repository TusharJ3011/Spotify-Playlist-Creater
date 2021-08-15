import tkinter
from tkinter import messagebox
import anime_intros
import global_100
import bolly_20

THEME_COLOR1 = "#22c95c"
THEME_COLOR2 = "#000000"
window = tkinter.Tk()
window.title("Spotify Playlist Creator")
window.config(padx=50, pady=50, bg=THEME_COLOR1)

icon_logo = tkinter.PhotoImage(file="logo.png")
window.iconphoto(False, icon_logo)


def create():
    user_choice = choice.get()
    if user_choice == "Select The Data ▼":
        messagebox.showerror(title="Error", message="Please select a playlist!")
        return
    create_button.config(state="disabled")
    print("Retrieving Song Titles...")
    if user_choice == "15 Best Anime Intros":
        anime_intros.get_titles()
    elif user_choice == "Global Hot 100":
        global_100.get_titles()
    elif user_choice == "Bollywood Top 20":
        bolly_20.get_titles()
    return


options = {"15 Best Anime Intros", "Global Hot 100", "Bollywood Top 20"}
choice = tkinter.StringVar()
choice.set("Select The Data ▼")
dropdown_menu = tkinter.OptionMenu(window, choice, *options)
dropdown_menu.config(bg=THEME_COLOR2, fg=THEME_COLOR1)
dropdown_menu["menu"].config(bg=THEME_COLOR2, fg=THEME_COLOR1)
dropdown_menu.grid(row=0, column=0, pady=(1, 10))

create_button = tkinter.Button(window, text="Create My Playlist", relief="ridge", command=create, bg=THEME_COLOR2,
                               fg=THEME_COLOR1)
create_button.grid(row=1, column=0, pady=(10, 1))
window.mainloop()
