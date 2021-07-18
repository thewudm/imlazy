# Why?

I wrote this python program because I was getting late to classes a lot and the teachers in the class WhatsApp group always claaed me out for being late and asked me to come "quickly", without acknowledging any problems (if i had any) that i had. 

Hopefully, by using this I won't be late for classes again. 

# How does it work?

- An infinite for loop is running which carries out all the other processes
- First, this program checks which day it is and assigns the values of the subjects of each class and the timings.(Exits if it is a Sunday)
- Second, it checks if the current time (according to the computer) matches the time of any of the classes of that day. 
- Then, it opens google chrome and makes it fullscreen (so that it doesn't click any other app if chrome is not fullscreen) and goes to the google classroom tab (tab 3). (Note: the fullscreen feature only works for me because I use a tilong window manager called [yabai](https://github.com/koekeishiya/yabai"), for which I have a keybind that makes a particular app fullscreen. Check my [dots](https://github.com/thewudm/dots) to see the yabai and skhd script.)
- After this, the sidebar button is clicked and the program checks which class it is and clicks the respective subject classroom in the sidebar. 
- After entering the classroom for the subject, the program moves the cursor to the coordinates on the screen where the zoom link is posted.
- After the link is clicked, the program waits for the time to match the next class' time and repeats the process.
