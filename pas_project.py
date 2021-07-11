from tkinter import *
from tkinter import ttk
from page1 import *
import random
from os import getcwd
#--------------------------------***this is add info backend***-------------------------------------------
def add_info():

    queri_add = 'INSERT INTO PRIVATE (platform,username,password) values(%s,%s,%s)'
    values = (name_platform.get(),name_username.get(),name_password.get())
    cursor.execute(queri_add,values)
    mydb.commit()


#--------------------------------***show password define of button***------------------------------------------------------------------------------------------------
def show():
    name_password.config(show = '')

#--------------------------------***search pass define***---------------------------------------------------------------------------
def search_passwords():
    
    win = Tk()
    win.config(bg = '#ffffff')
    win.geometry('600x400')
    win.title("search by name")
    
    def search_by_username():
        search = ent_search.get()
        query = 'select * from PRIVATE where platform = %s'
        plat = (search,)
        cursor.execute(query,plat)
        result = cursor.fetchall()
        a = []
        for i in result:
            a.append(("  platform :"+str(i[0])+ "  username:" + str(i[1])+ "  password:"+ str(i[2])+"    " ))
            label_result.config(text="\n".join(a)) 


    top_frame = Frame(win,bg = 'deepskyblue')
    top_frame.place(x = 0,y = 0,height = 180,width = 600)
    Label(top_frame,text = 'search    your    password',font = 'dyuthi 18 bold',bg='deepskyblue',fg = 'white').place(x =170,y = 20)
    
    ent_search = Entry(top_frame,bg = 'white',fg = 'blue')
    ent_search.place(x = 125,y = 100,height = 35)
    
    label_result = Label(win,text='',bg = "white",fg = 'deepskyblue',font='tahoma 10 ')
    label_result.place(x = 0,y = 200)
    
    btn_search = Button(win,bg = 'white',fg = 'black',activeforeground='white',activebackground='dodgerblue4',text = 'Search',font = 'tahoma 10 bold',command=search_by_username)
    btn_search.place(x = 20, y = 100,height = 35,width=100)
#--------------------------------***generator***-----------------------------------------------------------------------------            
def pass_generator():
    
    win2 = Tk()
    win2.config(bg = '#ffffff')
    win2.geometry('500x300')
    win2.title("search by name")

    def generate_password():
        num = int(number_entry.get())
        word = "".join([chr(65 + i) for i in range(26)])
        number = "".join([str(i) for i in range(1, 10)])
        symbol = [".", "_", "-"]
        word_num = []
        while len(word_num) != num:
            word_num.append("".join(random.choices(word, k=1)))
            word_num.append("".join(random.choices(number, k=1)))
            word_num.append("".join(random.choices(symbol, k=1)))

            if len(word_num) >= num:
                a = len(word_num) - num
                for j in range(0,a):
                    word_num.pop()

                
        gen_passwd.insert(0,''.join(word_num))

    top_frame = Frame(win2,bg = 'deepskyblue')
    top_frame.place(x = 0,y = 0,height = 90,width = 500)
    Label(top_frame,text = 'strong    your    password',font = 'dyuthi 18 bold',bg='deepskyblue',fg = 'white').place(x =115,y = 30)

    gen_passwd = Entry(win2,bg = 'white',font='tahoma 13 bold',fg = 'deepskyblue')
    gen_passwd.place(x =183,y = 170,height =35)
    
    number_entry = Entry(win2,bg = 'white',font='dyuthi 11 bold',fg = 'deepskyblue')
    number_entry.place(x = 185,y = 117,height = 25,width =25)

    label_result = Label(win2,text='number of generate :',font='dyuthi 11 bold',bg = "white",fg = 'black')
    label_result.place(x = 24,y = 120)

    btn_generate = Button(win2,bg = 'white',font='tahoma 10 bold',fg = 'black',activeforeground='white',activebackground='deepskyblue',text = 'generate_password',command=generate_password)
    btn_generate.place(x = 24, y = 170,height = 35) 



#--------------------------------***front_end***------------------------------------------------------------------------------------
win = Tk()
win.geometry('620x400')
img1 = PhotoImage(file =getcwd()+'/my-vector'+'/Untitled.png')
frame_left = Frame(win,bg = '#ffffff')
frame_left.place(x = -20,y = 0,height =400,width =200)
Label(frame_left,image = img1,bg = '#ffffff').place(x=0,y=0,width =200,height =400)

frame_right = Frame(win,bg = '#ffffff')
frame_right.place(x =180,y = 0,height =400,width =525)


Label(frame_right,text = 'platform: ',bg = '#ffffff',fg ='#3a7ff7',font = 'dyuthi 13 bold').place(x = 20 ,y = 55,height = 30,width =100)
name_platform = Entry(frame_right,text = 'your platform',fg='dodgerblue2',font = 'dyuthi 14 ',bg = '#ffffff',highlightcolor='blue',highlightbackground='#ffffff')
name_platform.place(x=130 ,y = 55,height = 35,width =200)

Label(frame_right,text ='username: ',bg = '#ffffff',fg ='#3a7ff7',font = 'dyuthi 13 bold').place(x = 20 ,y =105, height = 35,width =100)
name_username = Entry(frame_right,text = 'email',fg='dodgerblue2',font='dyuthi 14',bg = '#ffffff',highlightcolor='blue',highlightbackground='#ffffff')
name_username.place(x = 130, y=105 , height =35, width =200)


Label(frame_right,text ='password: ',bg = '#ffffff',fg ='#3a7ff7', font = 'dyuthi 13 bold').place(x = 20 ,y =155  , height = 35,width =100)
name_password = Entry(frame_right,text ='password',font='dyuthi 14',show = '*',fg='dodgerblue2',bg = '#ffffff',highlightcolor='blue',highlightbackground='#ffffff')
name_password.place(x = 130 ,y =155, height = 35,width =200)


#---------------------------------------***show password button***--------------------------------------------------------------
img_scure = PhotoImage(file = getcwd() + '/my-vector' + '/images.png')
secur_btn = Button(frame_right,image = img_scure,command =show,bg='#ffffff',highlightbackground='#ffffff',activebackground='#ffffff',borderwidth=0)
secur_btn.place(x =331,y=155)


#----------------------------------------***submit button***-------------------------------------------------------------
img_submit = PhotoImage(file = getcwd() + '/my-vector' + '/submit.png')
btn = Button(frame_right,image =img_submit,activebackground='white',bg = '#ffffff',highlightbackground = 'white',borderwidth=0,command = add_info)
btn.place(x = 24,y=220)

#search button
img_search = PhotoImage(file = getcwd() + '/my-vector' + '/5.png')
btn = Button(frame_right,image =img_search,activebackground='white',bg = '#ffffff',highlightbackground = 'white',borderwidth=0,command = search_passwords)
btn.place(x = 300,y=220)

#generate button
img_generate = PhotoImage(file = getcwd() + '/my-vector' + '/4.png')
btn = Button(frame_right,image =img_generate,activebackground='white',bg = '#ffffff',highlightbackground = 'white',borderwidth=0,command=pass_generator)
btn.place(x = 160,y=220)


win.mainloop()
