# Arduino CNC plotter
A simple but functional all-in-one GUI app to control an Arduino CNC plotter.

No more software needed to control your small CNC machinery!

## Why another Arduino CNC code?
I realized that on Web lots of powerfull codes were already developed, but all of them required more than
one software to be installed on the PC (Hey come on.. I just want a pen to move, nothing more complex..).

In order to avoid this, I preferred to deploy my own all-in-one software which actually do the job excently.

## What's new here?
Written using only Python3, the app has lot of functions already integrated which gaves the possibility to:
- Print images: EVERY type of image
- Draw and print: Arduino will reproduce your hand-draw
- Write and print: if your home-printer is broken, this is a good solution :)
- Configure your CNC paramethers directly from the app

Let's have a look to the main features..

### Print images
You want to have a touchable version of the image you got on your pc-screen? Just select that image, software will do the heavy-job, and Arduino will print it!

![Diapositiva1_min](https://user-images.githubusercontent.com/67842431/112904631-83538280-90e9-11eb-9cf6-623580a3d507.jpg)

### Draw and print
You want to use your Arduino as an extenctions on your arm? No problem: take your muose or graphical-tablet, draw everything you want to on the board, and Arduino will reproduce 
perfectly your draw.

![Diapositiva2_min](https://user-images.githubusercontent.com/67842431/112904708-9d8d6080-90e9-11eb-840c-dccc4cb9e8f3.jpg)

### Write and print
You want to try a new text editor? You got it! Write what you want, align where you want, choose the font you want, and print it!

![Diapositiva3_min](https://user-images.githubusercontent.com/67842431/112904718-a2521480-90e9-11eb-9d2a-34c375fb1a66.jpg)

Lots of other examples can be found at [my website](http://bocchio.altervista.org/Arduino_printer/index.html), but here's another one:
<img src="https://user-images.githubusercontent.com/67842431/112901097-9adc3c80-90e4-11eb-9527-207a1e6a146d.gif" width="1280"/>
<br>
<br>
## Just to know..
For building this software I utilized lots of Python libraries. The mains are:
- OpenCv + NumPy + PIL: for image analisys and data/bit manipulation
- Tkinter: for the Graphical User Interface itself
- Serial: for data sending, passing throught COM port

Let me underline that this was my first time Python approach. Probably in the lines of code lot of errors can be found, and that the reason of next paragraph..

## Contribute to this project!
If you have a great idea that could improve the app, or you have suggestion, or you simply want to leave a comment, don't exitate. Here nobody is wrong and we are all here to
improve and make it better every day!

Have a nice coding day,

Tommaso :panda_face:
