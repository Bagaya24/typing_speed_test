import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as message
import math

win = tk.Tk()
win.geometry("1440x700")


text_level = {
    "Easy": """
Amid the hustle and bustle of city life, one can often find solace in a simple cup of coffee. It's more\n 
than justa beverage; it's a ritual that connects us to our inner peace amid chaos. Picture this A quaint\n
cafe tucked away on a cozy street corner, filled with the warm glow from vintage lighting and the soft\n 
hum of conversations. Here,people gather not just for their morning brew but also for moments that\n
matter to chat,catch up, or simply enjoy the present moment without distractions.\n""",
    "Medium": """
Imagine a bustling urban landscape where skyscrapers tower and streets are always abuzz with activity.Yet,\n 
in this concrete jungle, there exists an oasis – the café. These havens of tranquility stand as cultural\n
cornerstones that offer more than just refreshments; they serve as communal nexus points where life's\n 
complexities can momentarily be set aside for simple pleasures and human connection. These\n 
establishments range from small, family-owned operations to grandiose chains with their signature\n 
aromas wafting through the air. Each café has its own charm, but they share one universal trait: they\n 
provide an escape a brief respite from the relentless pace of city life. Patrons arrive seeking not\n 
only caffeine but also a space to unwind and engage with others in meaningful dialogue.It's here that\n 
ideas are exchanged, friendships forged over shared interests, and sometimes even love blossoms amidst\n 
the steam from freshly brewed espresso.Cafes often become cultural hubs where artistic expression thrives.\n
From local poets reciting verses to musicians tuning their instruments before an impromptu performance,\n
these venues foster creativity and community engagement.They are not just places to sip on a latte;\n 
they're sanctuaries that cater to the soul as much as they do to hunger or thirst. \n""",
    "Hard": """
Within the intricate tapestry of urban life lies an unexpected gem, a refuge from the relentless surge of\n 
time and technology – the cafe. This seemingly mundane institution transcends its role as a mere purveyor\n
of hot beverages to become a crucible for cultural synthesis and human connectivity.The multifaceted\n 
nature of these establishments is noteworthy, ranging from quaint nooks run by generations-long family\n
traditions to sprawling  chains with their meticulously crafted ambience designed to captivate the senses.\n
Regardless of size or style, each café weaves its unique narrative into the cityscape it inhabits, offering\n
a temporary reprieve from urbanity's unyielding cadence.Amidst this backdrop of perpetual motion, patrons\n 
seek solace and camaraderie in these communal spaces that breed interpersonal bonds over steaming cups of\n
coffee or tea. The café becomes a microcosm where individuals from disparate walks of life converge,\n 
engaging in rich dialogue and the exchange of ideas while savoring their chosen libations. Cafes serve\n
as epicenters for artistic expression, with walls adorned by local artists masterpieces or live performances\n
that resonate through open spaces, beckoning passersby to partake in this impromptu symphony of life and\n
creativity. Such establishments play a pivotal role in nurturing the arts and fostering an environment \n
where originality thrives amidst the cacophony of city sounds.These bastions of warmth and camaraderie also\n
provide platforms for philosophical discourse, intellectual debates,or simply contemplative silence amongst\n
like-minded individuals seeking respite from the digital deluge that characterizes modern existence. In \n
essence, cafés embody a haven where society's complexities are navigated through shared experiences and \n
profound human connections."""
}


# ----------fonction----------------- #

def compte_a_rebour(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count > 0:
        win.after(1000, compte_a_rebour,  count - 1)
        canvas.itemconfig(chrono_text, text=f"{count_min}: {count_sec}")
    else:
        message.showinfo("Finish", "The time is over")
        win.destroy()


def select_level(event):
    for label in container_contenu.winfo_children():
        label.destroy()
        n = 0
        h = 10
        w = 30
    for lettre in text_level[cmb_level.get()]:
        globals()[f"lb_text_challenge{n}"] = tk.Label(container_contenu,
                                                      text=lettre,
                                                      font=("Arial", 12, "normal"))
        if lettre == "\n":
            w = 15
            h += 14
        globals()[f"lb_text_challenge{n}"].place(x=w, y=h)
        w += globals()[f"lb_text_challenge{n}"].winfo_reqwidth()
        n += 1

    win.after(1000, compte_a_rebour, 60 * 5)


number_letter = 1


def color_the_letters(event):
    global number_letter
    try:
        if globals()[f"lb_text_challenge{number_letter}"].cget("text").lower() == event.keysym:
            globals()[f"lb_text_challenge{number_letter}"].config(fg="green")
        else:
            globals()[f"lb_text_challenge{number_letter}"].config(fg="red")
    except KeyError:
        message.showwarning("Finish", "No more letter")
        win.destroy()
    number_letter += 1


# ------------GUI--------------------- #
# -------------Menu------------------ #
container_menu = tk.Frame(win, width=500, height=40)
container_menu.grid(row=0, column=0)

lb_level = tk.Label(container_menu, text="Level: ")
lb_level.grid(row=0, column=0)

cmb_level = ttk.Combobox(container_menu, width=10)
cmb_level.bind('<<ComboboxSelected>>', select_level)
cmb_level['values'] = ("Easy", "Medium", "Hard")
cmb_level.grid(row=0, column=1, padx=10)

lb_chrono = tk.Label(container_menu, text="Chrono: ")
lb_chrono.grid(row=0, column=2)

canvas = tk.Canvas(container_menu, width=40, height=30)
chrono_text = canvas.create_text(20, 17, text="00:00")
canvas.grid(row=0, column=3)

# -------------contenu---------------- #
container_contenu = tk.Frame(win, width=1440, height=650)
container_contenu.grid(row=1, column=0)

lb_text_challenge = tk.Label(container_contenu,
                             text="Chose your Level's difficulties",
                             font=("Arial", 16, "normal"))
lb_text_challenge.place(x=0, y=0)

win.bind("<Key>", lambda event: color_the_letters(event))

win.mainloop()
