# importing libraries
from tkinter import *
from tkinter import filedialog
from tkinter import font, messagebox
from pygame import mixer
from pathlib import Path


# add many songs to the playlist of python mp3 player
def addsongs():
    # to open a file
    temp_song = filedialog.askopenfilenames(initialdir="Music/", title="Choose a song",
                                            filetypes=(("all Files", "*.*"), ("mp3 Files", "*.mp3"), ("wav Files", "*.wav")))
    # loop through every item in the list to insert in the listbox

    for s in temp_song:
        songs_list.insert(END, s)
        songs_list.select_set(0)
        Path(s).stem


def deletesong():
    try:
        curr_song = songs_list.curselection()
        songs_list.delete(curr_song[0])
    except IndexError:
        messagebox.showerror("Error", "Nothing to delete")
    except:
        messagebox.showerror("Error", "There is an error while deleting song.")


def Play():
    try:
        song = songs_list.get(ACTIVE)
        song = f'{song}'
        mixer.music.load(song)
        mixer.music.play()

    except:
        messagebox.showwarning("Empty list", "Empty list please add some songs to play.")
        addsongs()


# to pause the song
def Pause():
    mixer.music.pause()


# to stop the  song
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)


# to resume the song
def Resume():
    mixer.music.unpause()


# Function to navigate from the current song
def Previous():
    try:
        # to get the selected song index
        previous_one = songs_list.curselection()

        # to get the previous song index
        previous_one = previous_one[0] - 1
        # to get the previous song
        temp2 = songs_list.get(previous_one)
        temp2 = f'{temp2}'

        mixer.music.load(temp2)
        mixer.music.play()
        songs_list.selection_clear(0, END)
        # activate new song
        songs_list.activate(previous_one)
        # set the next song
        songs_list.selection_set(previous_one)

    except:
        messagebox.showwarning("Song not found", "No previous songs available.")


def Next():
    try:
        # to get the selected song index
        next_one = songs_list.curselection()
        # to get the next song index
        next_one = next_one[0] + 1
        # to get the next song
        temp = songs_list.get(next_one)
        temp = f'{temp}'
        mixer.music.load(temp)
        mixer.music.play()
        songs_list.selection_clear(0, END)
        # activate new song
        songs_list.activate(next_one)
        # set the next song
        songs_list.selection_set(next_one)

    except:
        messagebox.showwarning("Song not found", "Sorry this was last song from list")


# creating the root window
root = Tk()
root.geometry("+500+200")
root.title('Python MP3 Music player App ')

# Icon
root.iconbitmap(r'C:\\Users\\Abhay Sharma\\Documents\\clg\\python_clg\\pythonproject\\Python-MusicPlayer-master\\asset\\musicIcon.ico')
# initialize mixer
mixer.init()

# create a label to display image
disp_img = Label(root,bg="white", fg="black", font=('arial', 15), height=10, width=30)
disp_img.grid(row=0,column=0,columnspan=5)

# create the listbox to contain songs
songs_list = Listbox(root, selectmode=SINGLE, bg="white", fg="black", font=('arial', 15), height=10, width=30,
                    selectbackground="gray", selectforeground="black",relief=GROOVE)
songs_list.grid(row=0,column=5,columnspan=5)

#  create a slider for song
slider = Label(root,bg="white", fg="black", font=('arial', 15), height=1, width=54)
slider.grid(row=1,column=0,columnspan=9)


#  create a current song playing box
playing = Label(root,bg="white", fg="black", font=('arial', 15), height=1, width=30)
playing.grid(row=2,column=0,columnspan=5)


# font is defined which is to be used for the button font
defined_font = font.Font(family='Helvetica')

# play button
play_icon=PhotoImage('C:\\Users\\Abhay Sharma\\Desktop\\play.png')
play_button = Button(root, text='Play', width=6, command=Play)
play_button['font'] = defined_font
play_button.grid(row=2,column=5)

# pause button
pause_button = Button(root, text="Pause", width=6, command=Pause)
pause_button['font'] = defined_font
pause_button.grid(row=2,column=6)

# stop button
stop_button = Button(root, text="Stop", width=6, command=Stop)
stop_button['font'] = defined_font
stop_button.grid(row=1,column=9)

# resume button
Resume_button = Button(root, text="Resume", width=6, command=Resume)
Resume_button['font'] = defined_font
Resume_button.grid(row=2,column=7)

# previous button
previous_button = Button(root, text="Prev", width=6, command=Previous)
previous_button['font'] = defined_font
previous_button.grid(row=2,column=8)

# next button
next_button = Button(root, text="Next", width=6, command=Next)
next_button['font'] = defined_font
next_button.grid(row=2,column=9)

# menu
my_menu = Menu(root)
root.config(menu=my_menu)
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu", menu=add_song_menu)
add_song_menu.add_command(label="Add songs", command=addsongs)
add_song_menu.add_command(label="Delete song", command=deletesong)

mainloop()
