# Arduino CNC plotter
A simple but functional all-in-one GUI app to control an Arduino CNC plotter.

No more software needed to control your small CNC machinery!

## Why another Arduino CNC code?
I realized that on Web lots of powerfull codes were already developed, but all of them required more than
one software to be installed on the PC (Hey come on.. I just want a pen to move, nothing more complex..).

In order to avoid this, I preferred to deploy my own all-in-one software wich actually do the job excently.

## What's new here?
Written using only Python3, the app has lot of functions already integrated wich gaves the possibility to:
- Print images: EVERY type of image
- Draw and print: Arduino will reproduce your hand-draw
- Write and print: if your home-printer is broken, this is a good solution :)
- Configure your CNC paramethers directly from the app

Let's have a look to the main features..

### Print images
You want to have a touchable version of the image you got on your pc-screen? Just select that image, software will do the heavy-job, and Arduino will print it!

### Draw and print
You want to use your Arduino as an extenctions on your arm? No problem: take you muose or graphical-tablet, draw everything you want to on the board, and Arduino will reproduce 
perfectly your draw.

### Write and print
You want to try a new text editor? You got it! Write what you want, align where you want, choose the font you want, and print it!

images will follow..

## Just to know..
For building this software I utilized lots of Python libraries. The mains are:
- OpenCv2 + numpy + PIL: for image analisys and data/bit manipulation
- Tkinter: for the Graphical User Interface itself
- Serial: for data sending, passing throught COM port

Let me underline that this was my first time Python approach. Probably in the lines of code lot of errors can be found, and that the reason of next paragraph..

## Contribute to this project!
If you have a great idea that could improve the app, or you have suggestion, or you siply want to leave a comment, don't exitate! Here nobody is wrong and we are all here to
improve and make it better every day!

Have a nice coding day,
Tommaso
