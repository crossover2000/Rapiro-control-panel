import serial
import time
ser = serial.Serial('/dev/cu.usbserial-DA01HOL6', 9600, timeout=1)
ser_forward= '#M1'
ser_back = '#M2'
ser_left = '#M4'
ser_right = '#M3'
ser_stop = '#M0'
ser_wl = '#M8'
ser_wr = '#M6'
ser_wb = '#M5'
ser_sb = '#M7'

#建立窗口
import tkinter as tk
window = tk.Tk()
window.title('Rapiro遥控器')
window.geometry('400x400')
window.config(bg='yellow')

#建立一个标题Label
var_act = tk.StringVar() #建立一个显示变量
label = tk.Label(window, textvariable= var_act, bg='pink', width= 15, height= 2, pady= 10)
label.pack()

#建立一个分隔符
separator = tk.Frame(height=2, pady=20, bd=1, relief="sunken")
separator.pack(fill="x")

#建立按键的主Frame
frm_panal = tk.Frame(window, pady = 50)
frm_panal.pack()

#定义按键输出，点一下，先让Label显示指令
def forward():
    var_act.set('前进')
    ser.write(ser_forward.encode('utf-8')) #串口发送数据
def back():
    var_act.set('后退')
    ser.write(ser_back.encode('utf-8'))  # 串口发送数据
def left():
    var_act.set('向左转')
    ser.write(ser_left.encode('utf-8'))  # 串口发送数据
def right():
    var_act.set('向右转')
    ser.write(ser_right.encode('utf-8'))  # 串口发送数据
def stop():
    var_act.set('停止')
    ser.write(ser_stop.encode('utf-8'))  # 串口发送数据
def wave_left():
    var_act.set('挥左手')
    ser.write(ser_wl.encode('utf-8'))  # 串口发送数据
def wave_right():
    var_act.set('挥右手')
    ser.write(ser_wr.encode('utf-8'))  # 串口发送数据
def wave_both():
    var_act.set('挥双手')
    ser.write(ser_wb.encode('utf-8'))  # 串口发送数据
def shake_both():
    var_act.set('摇双手')
    ser.write(ser_sb.encode('utf-8'))  # 串口发送数据

#建立按键
b_forward = tk.Button(frm_panal, text = '前进', width= 10, height= 2,bg='white', command = forward).grid(row= 2, column= 1)
b_back = tk.Button(frm_panal, text = '后退', width= 10, height= 2, bg='white', command = back).grid(row= 4, column= 1)
b_left = tk.Button(frm_panal, text = '向左转', width= 10, height= 2, bg='white', command = left) .grid(row= 3, column= 0)
b_right = tk.Button(frm_panal, text = '向右转', width= 10, height= 2, bg='white', command = right) .grid(row= 3, column= 2)
b_stop = tk.Button(frm_panal, text = '停止', width= 10, height= 2, bg='white', command = stop) .grid(row= 3, column= 1)
b_wl = tk.Button(frm_panal, text = '挥左手', width= 10, height= 2, bg='yellow', command = wave_left) .grid(row= 0, column= 0)
b_wr = tk.Button(frm_panal, text = '挥右手', width= 10, height= 2, bg='yellow', command = wave_right) .grid(row= 0, column= 2)
b_wb = tk.Button(frm_panal, text = '挥双手', width= 10, height= 2, bg='yellow', command = wave_both) .grid(row= 1, column= 0)
b_sb = tk.Button(frm_panal, text = '摇双手', width= 10, height= 2, bg='yellow', command = shake_both ).grid(row= 1, column= 2)

window.mainloop()