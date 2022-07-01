'''Import Modules'''
import pygame
import tkinter as tkr
import os

'''Create Window'''
player = tkr.Tk()

'''Edit Window'''
player.title("Audio Player")
player.geometry("500x500")

'''Playlist register'''
'''Sort this block on basis of value of variable label rest all will be same'''
os.chdir("/Users/jiteshaggarwal/Downloads/songs")
print(os.getcwd)
songlist=os.listdir()

'''Volume Input'''
VolumeLevel=tkr.Scale(player,from_=0.0,to_=1.0,orient=tkr.HORIZONTAL,resolution= 0.1)

'''Playlist input'''
playlist=tkr.Listbox(player,highlightcolor="blue",selectmode=tkr.SINGLE)
print(songlist) 
for item in songlist:
    pos=0
    playlist.insert(pos,item)
    pos+=1

'''Pygame Init'''
pygame.init()
pygame.mixer.init()

'''Action Event'''
def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(VolumeLevel.get())
    print(pygame.mixer.music.get_volume())
    print(VolumeLevel.get())
    
def Stop():
    pygame. mixer.music.stop()
    
    
def Pause():
    pygame. mixer.music.pause()
    
def UnPause():
    pygame. mixer.music.unpause()


'''Register Buttons'''
button1 = tkr.Button(player,width=5, height=3, text="PLAY", command=Play)
button2 = tkr.Button(player, width=5, height=3, text="STOP", command=Stop)
button3 = tkr.Button(player,width=5, height=3, text="PAUSE", command=Pause)
button4 = tkr.Button(player,width=5, height=3, text="UNPAUSE", command=UnPause)


'''Song Name'''
var=tkr.StringVar()
songtitle=tkr.Label(player,textvariable=var)


'''Place widgets'''
songtitle .pack()
button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
VolumeLevel.pack(fill="x")
playlist.pack(fill="both",expand="yes")

'''Activate'''
player.mainloop()


