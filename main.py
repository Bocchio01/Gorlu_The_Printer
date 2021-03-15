from PIL import ImageTk, Image, ImageGrab, EpsImagePlugin, ImageFont, ImageDraw
from tkinter import ttk, font
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
import tkinter as tk, numpy as np, webbrowser, serial, time, math, cv2, os

from languages import *

EpsImagePlugin.gs_windows_binary =  r'C:\\Program Files\\gs\\gs9.53.3\bin\\gswin64c'


# ------------------------------
# lang selected -> start app
def selectLang(lang_selected):
    # update all widgets's text with lang selected
    # translation in "gorlu_languages.py" file
    global lang
    lang = lang_selected

    tk.Label(lang_frame, text=loading_[lang], **text_config).grid()
    windows.update()

    text_widget = {info_name: 'info_name', info_text_1: 'info_text_1', info_text_2: 'info_text_2',
                   config_text_0: 'config_text_0', config_text_1: 'config_text_1', config_text_2: 'config_text_2', config_save_code: 'config_save_code',
                   calibration_setting_text_0: 'calibration_setting_text_0', calibration_setting_text_1: 'calibration_setting_text_1', calibration_setting_text_2: 'calibration_setting_text_2', calibration_setting_text_3: 'calibration_setting_text_3', calibration_setting_text_4: 'calibration_setting_text_4', calibration_setting_text_5: 'calibration_setting_text_5', calibration_setting_text_6: 'calibration_setting_text_6', calibration_setting_load: 'calibration_setting_load',
                   printimg_setting_text_0: 'printimg_setting_text_0', printimg_setting_selection: 'printimg_setting_selection', printimg_setting_text_1: 'printimg_setting_text_1', printimg_setting_filling: 'printimg_setting_filling', printimg_setting_go: 'printimg_setting_go',
                   printhand_setting_text_0: 'printhand_setting_text_0', printhand_setting_text_1: 'printhand_setting_text_1', printhand_setting_text_2: 'printhand_setting_text_2', printhand_setting_text_3: 'printhand_setting_text_3', printhand_setting_button_0: 'printhand_setting_button_0', printhand_setting_button_1: 'printhand_setting_button_1',
                   printtext_setting_text_0: 'printtext_setting_text_0', printtext_setting_text_1: 'printtext_setting_text_1', printtext_setting_text_2: 'printtext_setting_text_2', printtext_setting_text_3: 'printtext_setting_text_3', printtext_setting_text_4: 'printtext_setting_text_4', printtext_setting_text_5: 'printtext_setting_text_5', printtext_setting_button: 'printtext_setting_button'}
    for i in text_widget.keys():
        i.config(text=dictionary_[text_widget[i]][lang])

    calibration_setting_direction_X.config(value=(direction_[lang]))
    calibration_setting_direction_Y.config(value=(direction_[lang]))
    printtext_setting_align_o.config(value=align_o[lang])
    printtext_setting_align_v.config(value=align_v[lang])

    printtext_setting_align_o.set(align_o[lang][1])
    printtext_setting_align_v.set(align_v[lang][1])

    # search for installed font and display them as option for "printtext page"
    permitted_font = []
    for i in font.families():
        try:
            ImageFont.truetype(i, size=12)
            permitted_font.append(i)
        except:
            pass
    printtext_setting_character.config(value=permitted_font)
    printtext_setting_character.set(permitted_font[0])

    printimg_setting_quality.config(state='disabled')
    printimg_setting_filling.config(state='disabled')

    windows.title(windows_[lang])
    menubar.add_cascade(label=menu_[lang][0][0], menu=info_menu)
    menubar.add_cascade(label=menu_[lang][1][0], menu=config_menu)
    menubar.add_command(label=menu_[lang][2], command=lambda: openPage(2))
    menubar.add_command(label=menu_[lang][3], command=lambda: openPage(3))
    menubar.add_command(label=menu_[lang][4], command=lambda: openPage(4))
    menubar.add_command(label=menu_[lang][5], command=lambda: openPage(5))
    info_menu.add_command(label=menu_[lang][0][1], command=lambda: openPage(0))
    info_menu.add_separator()
    info_menu.add_command(label=menu_[lang][0][2], command=lambda: launchLink(0))
    info_menu.add_command(label=menu_[lang][0][3], command=lambda: launchLink(1))
    config_menu.add_command(label=menu_[lang][1][1], command=lambda: openPage(1))
    config_menu.add_separator()
    config_menu.add_command(label=menu_[lang][1][2], command=lambda: launchLink(2))

    windows.config(menu=menubar)
    lang_frame.destroy()
    loadData()
    openPage(0)


# windows generic references
def loadData():
    # read initial values from "sources\\data\\Printer_calibration.txt" to set them in "calibration page"
    # if file fails sets defaults values
    global setting_data
    setting_data = []
    try:
        setting_file = open(setting_file_, 'r')
        setting_file.readline()
        for i in range(4):
            line = setting_file.readline()
            setting_data.append(int(line[-4:-1]))
        setting_file.close()
    except:
        setting_data = [155, 129, 1, 1]
    servo_max.set(setting_data[0])
    servo_min.set(setting_data[1])
    calibration_setting_direction_X.set(
        direction_[lang][0] if setting_data[2] == 1 else direction_[lang][1])
    calibration_setting_direction_Y.set(
        direction_[lang][0] if setting_data[3] == 1 else direction_[lang][1])


def openPage(page):
    # forget all frames then pack the selected one
    page_dictionary = [info_frame, config_frame, calibration_frame, printimg_frame, printhand_frame, printtext_frame, lang_frame]
    for i in range(len(page_dictionary)):
        page_dictionary[i].pack_forget()
    pack_config = {'fill': tk.BOTH, 'expand': True}
    page_dictionary[page].pack(**pack_config)


def launchLink(link):
    # launch webbrower with the selected link
    link_dictionary = ['https://github.com/Bocchio01/Arduino_printer.git',
                       'https://bocchio.altervista.org/Arduino_printer/index.html',
                       'https://learn.adafruit.com/adafruit-motor-shield/library-install']
    webbrowser.open_new(link_dictionary[link])


# config references
def setConfig(event):
    # open serial with selected COM_port
    # if serial fails shows an error message
    global ser, calib_check
    calib_check = False
    try:
        ser.close()
    except:
        pass
    try:
        ser = serial.Serial(config_COM.get(), 9600, timeout=1)
        showinfo(title=setConfig_[lang][0], message=setConfig_[lang][1])
    except:
        showinfo(title=setConfig_[lang][0], message=setConfig_[lang][2])


def saveCode():
    # asks for filepath and saves Arduino's code
    filepath = asksaveasfilename(title=saveCode_[lang][0], initialfile=saveCode_[lang][1], defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, 'w') as output_file:
        output_file.write(config_arduino_code.get(1.0, tk.END))


# calibration references
def setCalibr(event):
    global calib_check
    # get data from "calibration page", saves them in "sources\\data\\Printer_calibration.txt"
    # by 'sendData()' loads on Arduino board servo position for pen up/down
    setting_data[0] = servo_max.get()
    setting_data[1] = servo_min.get()
    if ((setting_data[0] < 180) and (setting_data[1] < 180) and (setting_data[0] > 0) and (setting_data[1] > 0)):
        setting_data[2] = (1 if calibration_setting_direction_X.get() == direction_[lang][0] else -1)
        setting_data[3] = (1 if calibration_setting_direction_Y.get() == direction_[lang][0] else -1)
        setting_file = open(setting_file_, 'w')
        t = 0
        setting_file.write(setCalibr_[lang][0] + '\n')
        for i in range(4):
            t = (t + 2 if i == 2 else t + 1)
            setting_file.write(dictionary_['calibration_setting_text_' + str(t)][lang] + '\t  ' + str(setting_data[i]) + '\n')
        setting_file.close()
        try:
            ser.open()
        except:
            try:
                ser.close()
                ser.open()
            except:
                showinfo(title=error_msg[lang][0], message=error_msg[lang][1])
                return

        time.sleep(2)
        ser.write((str(setting_data[0]) + ' ' + str(setting_data[1])).encode('utf-8'))
        for j in range(1, 5):
            for i in range(1, -1, -1):
                s = ('D' if ((i+j) % 2) == 0 else 'U')
                dataSend(s, setting_data[2] * j * 30 * i, setting_data[3] * j * 30 * i)
                time.sleep(0.5)
        calib_check = True
    else:
        showinfo(title=error_msg[lang][0], message=setCalibr_[lang][1])


# printimg references
def openImg():
    # asks for filepath and loads selected img into 'img_global'
    # then he calls 'elabImg()' in order to visualize CANNY(img_global) into 'printimg page'
    filepath = askopenfilename(title=openImg_[lang], filetypes=[("File img", "*.jpg *.png *.jpeg"), ("JPG", "*.jpg"), ("PNG", "*.png"), ("JPEG", "*.jpeg"), ("All Files", "*.*")])
    if not filepath:
        return
    else:
        global img_global
        img_global = cv2.imread(filepath)
        printimg_setting_filling.config(state='normal')
        printimg_setting_quality.config(state='normal')
        elabImg(0)
        printimg_setting_quality.set(100)


def elabImg(print_go):
    # works on 'img_work' = 'img_global'
    # delta_Y/X are delta between dimension of 'dim_visualizer' and dimension in 'img_work'
    # 'filling.get()' is off -> he uses quality as parameters for 'cv2.Canny()'
    # 'filling.get()' is on  -> he uses quality as parameters for 'cv2.threshold()', working on a GRAY version of img_work
    # 'print_go' is False -> he displays 'img_work' in 'printimg page'
    # 'print_go' is True -> return ('img_work', 'delta_X', 'delta_Y')
    img_work = img_global
    quality = printimg_setting_quality.get()
    height, width = img_work.shape[:2]
    if (width > height):
        delta_Y = dim_visualizer - round(height*dim_visualizer/width)
        delta_X = 0
    else:
        delta_Y = 0
        delta_X = dim_visualizer - round(width*dim_visualizer/height)
    img_work = cv2.resize(img_work, (dim_visualizer-delta_X, dim_visualizer-delta_Y))
    if (filling.get() == 0):
        img_work = cv2.Canny(img_work, quality, quality)
        img_work = cv2.bitwise_not(img_work)
    else:
        img_work = cv2.threshold(cv2.cvtColor(img_work, cv2.COLOR_BGR2GRAY), quality / 2, 255, cv2.THRESH_BINARY)[1]
    if (print_go != 1):
        img_to_display = ImageTk.PhotoImage(image=Image.fromarray(img_work)) 
        printimg_visualizer.configure(image=img_to_display)
        printimg_visualizer.image = img_to_display
    else:
        return(img_work, delta_X, delta_Y)


# new version
def startPrintImg():
    # ask 'elabImg()' to get initial parameters
    # while all 'img_to_print' is not white, he continusly looks for next black pixel nearest from the previous one found
    # he uses slicing technique for 2D array to find black pixel position
    # by 'dataSend()' he send pen_position and coordinates to serial port
    img_to_print, delta_X, delta_Y = elabImg(1)
    X = 0
    Y = 0
    while not img_to_print.all():
        i = 0
        while True:
            i += 1
            try:
                y = np.where(img_to_print[max(0, Y-i): Y+i+1, max(0, X-i): X+i+1] == 0)[0][0]
                x = np.where(img_to_print[max(0, Y-i): Y+i+1, max(0, X-i): X+i+1] == 0)[1][0]
                X = x + max(0, X-i)#(x if (X-i) < 0 else x-i+X)
                Y = y + max(0, Y-i)#(y if (Y-i) < 0 else y-i+Y)
                img_to_print[Y][X] = 255
                break
            except:
                pass
        if not dataSend(('U' if (i > 2) else 'D'), round(setting_data[2]*(X + delta_X)*250/dim_visualizer), round(setting_data[3]*(Y + delta_Y)*250/dim_visualizer)):
            return
        time.sleep(0.01)
    dataSend('U', 0, 0)


# printhand references
def savePosn(event):
    # he gets coordinates from the current mouse position
    # if new position is far from the previous one, set pen_position up
    # by 'dataSend' sends pen_position and current coordinates to the board
    global lastx, lasty
    try:
        if ((abs(event.x - lastx) > 15) or (abs(event.y - lasty) > 15)):
            s = 'U'
        else:
            s = 'D'
    except:
        s = 'U'
    lastx, lasty = event.x, event.y
    if ((lastx > 0) and (lastx < dim_visualizer) and (lasty > 0) and (lasty < dim_visualizer)):
        dataSend(s, round(setting_data[2]*event.x/2), round(setting_data[3]*event.y/2))


def addLine(event):
    # draw a line on the whiteboard and call 'savePosn()' to get next mouse position
    printhand_visualizer_board.create_line(lastx, lasty, event.x, event.y)
    savePosn(event)


def saveCanvas():
    # create a postscript file and ask filepath to save the canvas witheboard
    # then he eliminate postscript file
    printhand_visualizer_board.postscript(file="sources\\data\\Lavagna__work.eps")
    board_work = Image.open("sources\\data\\Lavagna__work.eps")
    filepath = asksaveasfilename(title=saveCanvas_[lang][0], initialfile=saveCanvas_[lang][1], defaultextension="png", filetypes=[("PNG", "*.png"), ("JPG", "*.jpg"), ("JPEG", "*.jpeg"), ("All Files", "*.*")])
    if filepath:
        board_work.save(filepath)
    else:
        pass
    board_work.close()
    os.remove("sources\\data\\Lavagna__work.eps")


# printtext referencs
def fontChanged(event):
    # when a text parameters is changhed, he reload the entire text and save il into an image file (using PIL library funtions)
    # then he set the 'text image' into the 'text page' 
    # text_image is declared as a global variable
    global text_image
    text_to_print = printtext_setting_entry.get('1.0', 'end-1c')
    text_image = Image.new('RGB', (500, 500), (255,255,255))
    draw = ImageDraw.Draw(text_image)
    font_ = ImageFont.truetype(printtext_setting_character.get(), size=int(printtext_setting_dimension.get()))
    w, h = draw.textsize(text_to_print, font=font_)

    horizontal = {align_o[lang][0]: (1, 'left'), align_o[lang][1]: ((500-w)/2, 'center'), align_o[lang][2]: ((500-w-1), 'right')}
    vertical = {align_v[lang][0]: 1, align_v[lang][1]: (500-h)/2, align_v[lang][2]: (500-h-1)}

    X, align = horizontal[printtext_setting_align_o.get()]
    Y = vertical[printtext_setting_align_v.get()]

    draw.text((X, Y), font=font_, text=text_to_print, fill='black', align=align)
    text_image = text_image.rotate(printtext_setting_rotation.get())
    img_to_show = ImageTk.PhotoImage(text_image)

    printtext_visualizer.config(image = img_to_show)
    printtext_visualizer.image = img_to_show


def printText():
    # he set img_global as text_image (taken from 'fontChanghed()')
    # open 'printimg page'
    global img_global, text_image
    img_global = np.array(text_image)
    printimg_setting_filling.config(state = 'normal')
    printimg_setting_quality.config(state = 'normal')
    elabImg(0)
    openPage(3)


# generical sending data
def dataSend(pen, X, Y):
    # he send data array = (pen_position, coordinate_point_X, coordinate_point_Y)
    # if pen_position is up, he wait for positive response ('A') from the board
    # if serial fails, return False
    global calib_check
    line = ('%s %d %d\n' % (pen, X, Y))
    if not calib_check:
        showinfo(title=error_msg[lang][0], message=error_msg[lang][2])
        return False
    try:
        ser.write(line.encode('utf-8'))
    except:
        showinfo(title = error_msg[lang][0], message = error_msg[lang][1])
        return False
    if (line[0] == 'U'):
        while ser.read() != str.encode('A'):
            continue


# ------------------------------
# windows
windows = tk.Tk()
windows.geometry('1000x600')
menubar = tk.Menu(windows)
info_menu = tk.Menu(menubar, tearoff=0)
config_menu = tk.Menu(menubar, tearoff=0)
main_frame = tk.Frame(windows, borderwidth=2, relief='solid')
main_frame.pack(fill=tk.BOTH, expand=True)

# global variable
setting_file_ = "sources\\data\\Printer_calibration.txt"
calib_check = False
img_global = []
text_image = []

# general widget configuration
bg_general = '#E7E6E6'
bg_button = '#7F7F7F'
bg_visualizer = 'white'
dim_visualizer = 500
text_font = font.Font(family='calibri', size=14, weight=font.BOLD)
text_config = {'bg': bg_general, 'font': text_font}
button_config = {'bg': bg_button, 'font': text_font}
combobox_config = {'state': 'readonly', 'font': text_font}
visualizer_config = {'bg': bg_visualizer, 'bd': 1, 'relief': 'solid', 'height': dim_visualizer, 'width': dim_visualizer}


# ------------------------------
# lang_frame
lang_frame = tk.Frame(main_frame, bg=bg_general)
lang_img_it = tk.Label(lang_frame)
lang_img_en = tk.Label(lang_frame)
lang_img_fr = tk.Label(lang_frame)
img_it = ImageTk.PhotoImage(Image.open('sources\\img\\it.png'))
img_en = ImageTk.PhotoImage(Image.open('sources\\img\\en.png'))
img_fr = ImageTk.PhotoImage(Image.open('sources\\img\\fr.png'))
lang_img_it.configure(image=img_it, bg=bg_general)
lang_img_en.configure(image=img_en, bg=bg_general)
lang_img_fr.configure(image=img_fr, bg=bg_general)
lang_button_it = tk.Button(lang_frame, text="Iniziamo!", command=lambda: selectLang(0), **button_config)
lang_button_en = tk.Button(lang_frame, text="Let's start!", command=lambda: selectLang(1), **button_config)
lang_button_fr = tk.Button(lang_frame, text="Allons-y!", command=lambda: selectLang(2), **button_config)

# lang pack/grid
lang_frame.columnconfigure([0, 1, 2], weight=1)
lang_frame.rowconfigure([0, 1, 2], weight=1)

lang_img_it.grid(column=0, row=0, pady=30, sticky='s')
lang_img_en.grid(column=1, row=0, pady=30, sticky='s')
lang_img_fr.grid(column=2, row=0, pady=30, sticky='s')
lang_button_it.grid(column=0, row=1, padx=70, sticky='wen')
lang_button_en.grid(column=1, row=1, padx=70, sticky='wen')
lang_button_fr.grid(column=2, row=1, padx=70, sticky='wen')


# ------------------------------
# info_frame
info_frame = tk.Frame(main_frame, bg=bg_general)
info_name = tk.Label(info_frame, **text_config)
info_text_1 = tk.Label(info_frame, **text_config)
info_text_2 = tk.Label(info_frame, **text_config)
info_img = tk.Label(info_frame, bg=bg_general)
info_separator_0 = ttk.Separator(info_frame, orient=tk.HORIZONTAL)

img_gorlu = ImageTk.PhotoImage(Image.open('sources\\img\\info.png'))
info_img.configure(image=img_gorlu)

# info pack/grid
info_name.pack(fill=tk.X, pady=30)
info_separator_0.pack(fill=tk.X, padx=200)
info_text_1.pack(fill=tk.X, pady=30)
info_img.pack(pady=5)
info_text_2.pack(fill=tk.X, pady=30)


# ------------------------------
# config_frame
COM_ports = []
for i in range(1, 11):
    COM_ports.append('COM' + str(i))
config_frame = tk.Frame(main_frame, bg=bg_general)
config_text_0 = tk.Label(config_frame, **text_config)
config_text_1 = tk.Label(config_frame, **text_config)
config_text_2 = tk.Label(config_frame, **text_config)
config_COM = ttk.Combobox(config_frame, values=COM_ports, textvariable= tk.StringVar(), **combobox_config)
config_separator_0 = ttk.Separator(config_frame, orient=tk.HORIZONTAL)
config_separator_1 = ttk.Separator(config_frame, orient=tk.HORIZONTAL)
config_save_code = tk.Button(config_frame, command=lambda: saveCode(), **button_config)

config_COM['font'] = ('calibri', 20)

config_code_frame = tk.Frame(config_frame)
config_arduino_code = tk.Text(config_code_frame, height=12, width=70)
config_arduino_scroll = ttk.Scrollbar(config_code_frame, orient=tk.VERTICAL, command=config_arduino_code.yview)

config_arduino_code['yscrollcommand'] = config_arduino_scroll.set
file_arduino_code = open('sources\\data\\Arduino_code.txt', 'r')
config_arduino_code.insert('1.0', file_arduino_code.read())
file_arduino_code.close()

# config pack/grid
config_text_0.pack(pady=8)
config_COM.pack(pady=5)
config_separator_0.pack(fill=tk.X, padx=200, pady=15)
config_text_1.pack()
config_separator_1.pack(fill=tk.X, padx=200, pady=15)
config_text_2.pack(pady=5)
config_code_frame.pack(pady=10)
config_arduino_code.grid(column=0, row=0, sticky='we')
config_arduino_scroll.grid(column=1, row=0, sticky='ns')
config_save_code.pack(pady=10)

config_COM.bind('<<ComboboxSelected>>', lambda e: setConfig(None))


# -------------------------------
# calibration_frame
servo_max = tk.IntVar()
servo_min = tk.IntVar()
calibration_frame = tk.Frame(main_frame, bg=bg_general)

calibration_setting_frame = tk.Frame(calibration_frame, bg=bg_general)
calibration_setting_text_0 = tk.Label(calibration_setting_frame, **text_config)
calibration_setting_text_1 = tk.Label(calibration_setting_frame, **text_config)
calibration_setting_text_2 = tk.Label(calibration_setting_frame, **text_config)
calibration_setting_text_3 = tk.Label(calibration_setting_frame, **text_config)
calibration_setting_text_4 = tk.Label(calibration_setting_frame, **text_config)
calibration_setting_text_5 = tk.Label(calibration_setting_frame, **text_config)
calibration_setting_text_6 = tk.Label(calibration_setting_frame, **text_config)
calibration_setting_separator_0 = ttk.Separator(calibration_setting_frame, orient=tk.HORIZONTAL)
calibration_setting_separator_1 = ttk.Separator(calibration_setting_frame, orient=tk.HORIZONTAL)
calibration_setting_servo_max = tk.Entry(calibration_setting_frame, textvariable=servo_max, width=10, font=text_font)
calibration_setting_servo_min = tk.Entry(calibration_setting_frame, textvariable=servo_min, width=10, font=text_font)
calibration_setting_direction_X = ttk.Combobox(calibration_setting_frame, width=15, textvariable= tk.StringVar(), **combobox_config)
calibration_setting_direction_Y = ttk.Combobox(calibration_setting_frame, width=15, textvariable= tk.StringVar(), **combobox_config)
calibration_setting_load = tk.Button(calibration_setting_frame, command=lambda: setCalibr(None), **button_config)

calibration_visualizer_frame = tk.Frame(calibration_frame, bg=bg_visualizer)
calibration_visualizer = tk.Label(calibration_visualizer_frame, **visualizer_config)

img_calibration = ImageTk.PhotoImage(file='sources\\img\\calibration.png')
calibration_visualizer.configure(image=img_calibration)

# calibration pack/grid
calibration_setting_frame.rowconfigure([0, 4, 8, 9], minsize=70)
calibration_setting_frame.rowconfigure([1, 2, 5, 6], minsize=20)
calibration_setting_frame.rowconfigure([3, 7], minsize=30)
calibration_setting_frame.columnconfigure(0, minsize=400)

calibration_setting_frame.pack(fill=tk.Y, side=tk.LEFT, pady=50)
calibration_setting_text_0.grid(sticky='ns')
calibration_setting_text_1.grid(row=1, padx=80, sticky='nsw')
calibration_setting_text_2.grid(row=2, padx=80, sticky='nsw')
calibration_setting_servo_max.grid(row=1, padx=80, sticky='e')
calibration_setting_servo_min.grid(row=2, padx=80, sticky='e')
calibration_setting_separator_0.grid(padx=40, sticky='wes')
calibration_setting_text_3.grid(sticky='ns')
calibration_setting_text_4.grid(row=5, padx=30, sticky='nsw')
calibration_setting_text_5.grid(row=6, padx=30, sticky='nsw')
calibration_setting_direction_X.grid(row=5, padx=30, sticky='e')
calibration_setting_direction_Y.grid(row=6, padx=30, sticky='e')
calibration_setting_separator_1.grid(padx=40, sticky='wes')
calibration_setting_text_6.grid(sticky='s')
calibration_setting_load.grid(sticky='s')
calibration_visualizer_frame.pack(fill=tk.BOTH, expand=True)
calibration_visualizer.pack(expand=True)


# ------------------------------
# printimg_frame
filling = tk.IntVar(value=0)
printimg_frame = tk.Frame(main_frame, bg=bg_general)

printimg_setting_frame = tk.Frame(printimg_frame, bg=bg_general)
printimg_setting_text_0 = tk.Label(printimg_setting_frame, **text_config)
printimg_setting_text_1 = tk.Label(printimg_setting_frame, **text_config)
printimg_setting_separator_0 = ttk.Separator(printimg_setting_frame, orient=tk.HORIZONTAL)
printimg_setting_separator_1 = ttk.Separator(printimg_setting_frame, orient=tk.HORIZONTAL)
printimg_setting_selection = tk.Button(printimg_setting_frame, command=lambda: openImg(), **button_config)
printimg_setting_quality = tk.Scale(printimg_setting_frame, orient=tk.HORIZONTAL, length=300, from_=1.0, to=500.0, command=lambda e: elabImg(0), **button_config)
printimg_setting_filling = tk.Checkbutton(printimg_setting_frame,  variable=filling, onvalue=1, offvalue=0, command=lambda: elabImg(0), **text_config)
printimg_setting_go = tk.Button(printimg_setting_frame, command=lambda: startPrintImg(), **button_config)

printimg_setting_go['font'] = ('calibri', 20, font.BOLD)

printimg_visualizer_frame = tk.Frame(printimg_frame, bg=bg_visualizer)
printimg_visualizer = tk.Label(printimg_visualizer_frame, **visualizer_config)

# printimg pack/grid
printimg_setting_frame.rowconfigure([0, 3, 4, 7, 8], minsize=70)
printimg_setting_frame.rowconfigure([2, 5, 6], minsize=40)
printimg_setting_frame.rowconfigure(1, minsize=60)
printimg_setting_frame.columnconfigure(0, minsize=400)

printimg_setting_frame.pack(fill=tk.Y, side=tk.LEFT, pady=50)
printimg_setting_text_0.grid(sticky='ns')
printimg_setting_selection.grid(sticky='n')
printimg_setting_separator_0.grid(padx=40, sticky='we')
printimg_setting_text_1.grid(sticky='ns')
printimg_setting_quality.grid(sticky='n')
printimg_setting_filling.grid(sticky='wens')
printimg_setting_separator_1.grid(padx=40, sticky='we')
printimg_setting_go.grid(pady=30, sticky='s')
printimg_visualizer_frame.pack(fill=tk.BOTH, expand=True)
printimg_visualizer.pack(expand=True)


# ------------------------------
# printhand_frame
printhand_frame = tk.Frame(main_frame, bg=bg_general)

printhand_setting_frame = tk.Frame(printhand_frame, bg=bg_general)
printhand_setting_text_0 = tk.Label(printhand_setting_frame, **text_config)
printhand_setting_text_1 = tk.Label(printhand_setting_frame, **text_config)
printhand_setting_text_2 = tk.Label(printhand_setting_frame, **text_config)
printhand_setting_text_3 = tk.Label(printhand_setting_frame, **text_config)
printhand_setting_separator_0 = ttk.Separator(printhand_setting_frame, orient=tk.HORIZONTAL)
printhand_setting_separator_1 = ttk.Separator(printhand_setting_frame, orient=tk.HORIZONTAL)
printhand_setting_button_0 = tk.Button(printhand_setting_frame, command=lambda: printhand_visualizer_board.delete('all'), **button_config)
printhand_setting_button_1 = tk.Button(printhand_setting_frame, command=lambda: saveCanvas(), **button_config)

printhand_visualizer_frame = tk.Frame(printhand_frame, bg=bg_visualizer)
printhand_visualizer_board = tk.Canvas(printhand_visualizer_frame, **visualizer_config)

# printhand pack/grid
printhand_setting_frame.rowconfigure([0, 3, 4, 6, 7], minsize=70)
printhand_setting_frame.rowconfigure([2, 5], minsize=30)
printhand_setting_frame.rowconfigure(1, minsize=30)
printhand_setting_frame.columnconfigure(0, minsize=400)

printhand_setting_frame.pack(fill=tk.Y, side=tk.LEFT, pady=50)
printhand_setting_text_0.grid(sticky='ns')
printhand_setting_separator_0.grid(padx=40, sticky='we')
printhand_setting_text_1.grid(pady=10, sticky='ns')
printhand_setting_text_2.grid(sticky='ns')
printhand_setting_text_3.grid(sticky='ns')
printhand_setting_separator_1.grid(padx=40, sticky='we')
printhand_setting_button_0.grid(pady=20, sticky='s')
printhand_setting_button_1.grid(pady=0, sticky='n')
printhand_visualizer_frame.pack(fill=tk.BOTH, expand=True)
printhand_visualizer_board.pack(expand=True)

printhand_visualizer_board.bind('<Button-1>', savePosn)
printhand_visualizer_board.bind('<B1-Motion>', addLine)


# ------------------------------
# printtext_frame
text_dimension = tk.IntVar(value=30)
printtext_frame = tk.Frame(main_frame, bg=bg_general)

printtext_setting_frame = tk.Frame(printtext_frame, bg=bg_general)
printtext_setting_text_0 = tk.Label(printtext_setting_frame, **text_config)
printtext_setting_text_5 = tk.Label(printtext_setting_frame, **text_config)
printtext_setting_entry = tk.Text(printtext_setting_frame, font=('calibri', 13), width=35, height=4)
printtext_setting_separator_0 = ttk.Separator(printtext_setting_frame, orient=tk.HORIZONTAL)
printtext_setting_separator_2 = ttk.Separator(printtext_setting_frame, orient=tk.HORIZONTAL)
printtext_setting_rotation = tk.Scale(printtext_setting_frame, orient=tk.HORIZONTAL,length=300, from_=-180.0, to=180.0, command=fontChanged, **button_config)
printtext_setting_button = tk.Button(printtext_setting_frame, command=lambda: printText(), **button_config)

printtext_setting_subframe = tk.Frame(printtext_setting_frame, bg=bg_general)
printtext_setting_text_1 = tk.Label(printtext_setting_subframe, **text_config)
printtext_setting_text_4 = tk.Label(printtext_setting_subframe, **text_config)
printtext_setting_text_2 = tk.Label(printtext_setting_subframe, **text_config)
printtext_setting_text_3 = tk.Label(printtext_setting_subframe, **text_config)
printtext_setting_separator_1 = ttk.Separator(printtext_setting_subframe, orient=tk.VERTICAL)
printtext_setting_dimension = tk.Entry(printtext_setting_subframe, textvariable=text_dimension, font=text_font, width=3)
printtext_setting_character = ttk.Combobox(printtext_setting_subframe, width=10, textvariable= tk.StringVar(), **combobox_config)
printtext_setting_align_o = ttk.Combobox(printtext_setting_subframe, width=9, textvariable= tk.StringVar(), **combobox_config)
printtext_setting_align_v = ttk.Combobox(printtext_setting_subframe, width=9, textvariable= tk.StringVar(), **combobox_config)

printtext_visualizer_frame = tk.Frame(printtext_frame, bg=bg_visualizer)
printtext_visualizer = tk.Label(printtext_visualizer_frame, **visualizer_config)

# printtext pack/grid
printtext_setting_frame.rowconfigure(0, minsize=50)
printtext_setting_frame.rowconfigure([1, 2, 3, 5, 6, 7], minsize=30)
printtext_setting_frame.rowconfigure(4, minsize=40)
printtext_setting_frame.columnconfigure(0, minsize=400)

printtext_setting_subframe.columnconfigure(0, minsize=180)
printtext_setting_subframe.columnconfigure(1, minsize=50)
printtext_setting_subframe.columnconfigure(2, minsize=60)
printtext_setting_subframe.rowconfigure([0, 1, 2], minsize=40)

printtext_setting_frame.pack(fill=tk.Y, side=tk.LEFT, pady=50)
printtext_setting_text_0.grid(sticky='s')
printtext_setting_entry.grid(padx=30, pady=10, sticky='n')
printtext_setting_separator_0.grid(padx=40, sticky='we')

printtext_setting_subframe.grid()
printtext_setting_text_1.grid(row=0, column=0, sticky='ns')
printtext_setting_text_4.grid(row=0, column=2, sticky='ns')
printtext_setting_text_2.grid(row=1, column=0, sticky='w')
printtext_setting_text_3.grid(row=2, column=0, sticky='w')
printtext_setting_dimension.grid(row=1, column=0, sticky='e')
printtext_setting_character.grid(row=2, column=0, sticky='e')
printtext_setting_align_o.grid(row=1, column=2)
printtext_setting_align_v.grid(row=2, column=2)
printtext_setting_separator_1.grid(column=1, row=1, rowspan=3, sticky='ns')

printtext_setting_text_5.grid(sticky='ns')
printtext_setting_rotation.grid(row=5)
printtext_setting_separator_2.grid(padx=40, sticky='wes')
printtext_setting_button.grid(pady=20, sticky='n')
printtext_visualizer_frame.pack(fill=tk.BOTH, expand=True)
printtext_visualizer.pack(expand=True)

printtext_setting_entry.bind('<Key>', fontChanged)
printtext_setting_dimension.bind('<Return>', fontChanged)
printtext_setting_dimension.bind("<FocusOut>", fontChanged)
printtext_setting_character.bind('<<ComboboxSelected>>', fontChanged)
printtext_setting_align_o.bind('<<ComboboxSelected>>', fontChanged)
printtext_setting_align_v.bind('<<ComboboxSelected>>', fontChanged)


# open lang_frame
openPage(6)
windows.mainloop()
