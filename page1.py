from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector.errors import Error

#---------------------------------------***database***--------------------------------------------------
def mydatabase():
    global mydb
    global cursor

    try:

        mydb = mysql.connector.connect(user = db_username.get(),host = db_host.get(), password = db_password.get())

        cursor = mydb.cursor()

        queri_db = ('CREATE DATABASE IF NOT EXISTS pass ')
        cursor.execute(queri_db)

        queri_use = ('use pass')
        cursor.execute(queri_use)

        query_table = 'CREATE TABLE IF NOT EXISTS PRIVATE( platform varchar(255) ,username varchar(255) ,password varchar(255))'
        cursor.execute(query_table)

        if mysql:
            lbl_cnt.config(text ='database is connect please enter in next_page button')

    except mysql.connector.Error as err:
        lbl_cnt.config(text ='Somethings went wrong try again')


#-------------------------------------***next page backend****-----------------------------------------------------------
def next_page():
    win.destroy()
    import pas_project


#--------------------------------***show password define of button***------------------------------------------------------------------------------------------------
def show():
    db_password.config(show = '')


#-------------------------------------***front of page 1****----------------------------------------------------

win = Tk()
win.geometry('620x400')
frame_left = Frame(win,bg = '#e7ff08')
frame_left.place(x = -20 ,y = 0,height =400,width =200)
img1 = PhotoImage(file = '/home/reza/Desktop/Untitled2.png')
Label(frame_left,image = img1,bg = '#ffffff').place(x=0,y=0,width =200,height =400)

frame_right = Frame(win,bg = '#ffffff')
frame_right.place(x =180,y = 0,height =400,width =525)
#label of text in top of frame
Label(frame_right,text ='please enter your database and username and password and host',font = 'dyuthi 10 ',bg = '#ffffff',fg="#3a7ff7").place(x = 15, y = 10)

Label(frame_right,text = 'username: ',bg = '#ffffff',fg ='#3a7ff7',font = 'dyuthi 13 bold').place(x = 20 ,y = 55,height = 30,width =100)
db_username = Entry(frame_right,text = 'your platform',highlightcolor='blue',font='dyuthi 14',fg='dodgerblue2',bg = '#ffffff',highlightbackground='#ffffff')
db_username.place(x=130 ,y = 55,height = 35,width =200)

Label(frame_right,text ='password: ',bg = '#ffffff',fg ='#3a7ff7',font = 'dyuthi 13 bold').place(x = 20 ,y =105, height = 35,width =100)
db_password = Entry(frame_right,show = "*",fg='dodgerblue2',bg = '#ffffff',font='dyuthi 14',highlightcolor='blue',highlightbackground='#ffffff')
db_password.place(x = 130, y=105 , height =35, width =200)

Label(frame_right,text ='      HOST: ',bg = '#ffffff',fg ='#3a7ff7',font = 'dyuthi 13 bold').place(x = 20 ,y =155, height = 35,width =100)
db_host = Entry(frame_right,fg='dodgerblue2',bg = '#ffffff',font='dyuthi 14',highlightcolor='blue',highlightbackground='#ffffff')
db_host.place(x = 130, y=155 , height =35, width =200)

#---------------------------------------***show password button***--------------------------------------------------------------
img_scure = PhotoImage(file = '/home/reza/Desktop/images.png')
secur_btn = Button(frame_right,image = img_scure,command =show,bg='#ffffff',highlightbackground='#ffffff',activebackground='#ffffff',borderwidth=0)
secur_btn.place(x =331,y=105)


#next page button
img_nextpg = PhotoImage(file = '/home/reza/Desktop/nextpage.png')
btn = Button(frame_right,image =img_nextpg,activebackground='white',bg = '#ffffff',highlightbackground = 'white',borderwidth=0,command =next_page)
btn.place(x = 24,y=220)

#connect button 
img_connectpg = PhotoImage(file = '/home/reza/Desktop/connect.png')
btn = Button(frame_right,image =img_connectpg,activebackground='white',bg = '#ffffff',highlightbackground = 'white',borderwidth=0,command =mydatabase)
btn.place(x = 300,y=220)


#label of text for coneecting to database in down of page
lbl_cnt =Label(frame_right,text ='',bg = '#ffffff',fg ='black')
lbl_cnt.place(x=10,y = 350)

win.mainloop()