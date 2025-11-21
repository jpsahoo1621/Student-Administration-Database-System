from tkinter import *
from tkinter import messagebox

from pymysql import *
conobj = connect (host = 'localhost',user = 'root', password='',port = 3306)
curobj = conobj.cursor()
curobj.execute('use project;')
win1 = Tk ()

#====================================================
def Login():
		
		p1=Sregno.get()
		p2=Spwd.get()
		p3=Accyear.get()
		#print(Sregno.get(), Accyear.get(),Dept.get(),Spwd.get())
		r = 'select * from student where Regno = {} and Accyear = "{}" and Dept = "{}" and Password="{}";'.format(Sregno.get(),Accyear.get(),Dept.get(),Spwd.get())
		curobj.execute(r)
		record = curobj.fetchall()
		if len(record):
			win1.destroy()
			win2 = Tk()
			#==========================================
			def Update():
				
				#print(Uregno.get(),Uname.get(),Ugender.get(),Upname.get(),Uaccyear.get(),Udept.get(),Ucno.get(),Upwd.get())
				
				r = 'update student set Name = "{}",Gender = "{}", Parent = "{}",Contact="{}", Dept= "{}",Password="{}" where Regno = {} and Password= "{}" ;'. format(Uname.get(),Ugender.get(),Upname.get(),Ucno.get(),Udept.get(),Upwd.get(),p1,p2)
												
				print(r)
				curobj.execute(r)
				conobj.commit()
				win2.destroy()
				
			def Exit():
				win2.destroy()
			def Reset():
				Uregno.delete(0,END)
				Uname.delete(0,END)
				Ugender.set(None)
				Upname.delete(0,END)
				Uaccyear.set("Select Acad Year")
				Udept.set("Select Dept. Name")
				Ucno.delete(0,END)
				Upwd.delete(0,END)


			#==========================================


			win2.maxsize(1000,600)		#set maximum size
			win2.minsize(1000,600) 		#set minimum size
			win2.title ("Student Home Page") 		#set the title
			win2.configure(bg = "pink")		#set the color of the page
			
			Label(win2, text = "Student Regno", font=('Ebrima',13),fg = "black", width = 17,relief = 'raised').place(x=30,y=100)		#Create admin user id label
			v1 = StringVar(win2,value=p1)
			Uregno = Entry(win2,textvariable = v1,font = ('Ebrima',13),bg = 'white', fg = 'black', width = 20)
			Uregno.place(x = 250,y = 100)		#input text here


			Label(win2, text = "Student Name", font=('Ebrima',13),fg = "black", width = 17,relief = 'raised').place(x=530,y=100)		#Create admin user id label
			Uname = Entry(win2,font = ('Ebrima',13),bg = 'white', fg = 'black', width = 20)
			Uname.place(x = 730,y = 100)		#input text here


			Label(win2, text = "Student Gender", font=('Ebrima',13),fg = "black", width = 17,relief 	= 'raised').place(x=30,y=150)		#Create admin user id label
			Ugender = StringVar()
			r1 = Radiobutton(win2,text = "Male",font=('Ebrima',13),variable = Ugender,value = 'M')
			r1.place(x=250,y=150)	
			r2 = Radiobutton(win2,text = "Female",font=('Ebrima',13),variable = Ugender,value = 'F')
			r2.place(x=350,y=150)			
		


			Label(win2, text = "Parent Name", font=('Ebrima',13),fg = "black", width = 17,relief = 'raised').place(x=530,y=150)		#Create admin user id label
			Upname = Entry(win2,font = ('Ebrima',13),bg = 'white', fg = 'black', width = 20)
			Upname.place(x = 730,y = 150)		#input text here



			Label(win2, text = "-- Select Acad Year --", font=('Ebrima',13),fg = "black", width = 17,relief 			= 'raised').place(x=30,y=200)		#Create admin user id label
			
			Uaccyear= StringVar()
			#v2=StringVar(win2,value = p3)
			Uaccyear.set(p3)														
			menu1	=OptionMenu(win2,Uaccyear,"2019-2023","2020-2024","2021-2025","2022-2026","2023-2027","2024-2028")
			menu1.place(x=250,y=200)
					


			Label(win2, text = "Select Dept Name", font=('Ebrima',13),fg = "black", width = 17,relief = 'raised').place(x=530,y=200)		#Create admin user id label
			Udept = StringVar()
			Udept.set("-- Select Department Name --")
			menu2 = OptionMenu(win2,Udept,"CSE","CSIT","EEE","ME","CIVIL")
			menu2.place(x=730,y=200)					#input text here


			Label(win2, text = "Student Cont. No", font=('Ebrima',13),fg = "black", width = 17,relief 	= 'raised').place(x=30,y=250)		#Create admin user id label
			Ucno = Entry(win2,font = ('Ebrima',13),bg = 'white', fg = 'black', width = 20)
			Ucno.place(x = 250,y = 250)		#input text here


			Label(win2, text = "Password", font=('Ebrima',13),fg = "black", width = 17,relief 	= 'raised').place(x=530,y=250)		#Create admin user id label
			v2=StringVar(win2,value=p2)
			Upwd = Entry(win2,textvariable=v2,font = ('Ebrima',13),bg = 'white', fg = 'black', width = 20)
			Upwd.place(x = 730,y = 250)		#input text here


			Button(win2, text = 'RESET', font=('Ebrima',15), width = 10, height = 1,fg = 'red', activebackground = '#ccfb5d', relief = 'raised',command = Reset).place(x =100,y = 400) 	#to create button


			Button(win2, text = 'UPDATE', font=('Ebrima',15), width = 10, height = 1,fg = 'red', activebackground = '#ccfb5d', relief = 'raised',command = Update).place(x = 450,y = 400) 	#to create button


			Button(win2, text = 'EXIT', font=('Ebrima',15), width = 10, height = 1,fg = 'red', activebackground = '#ccfb5d', relief = 'raised',command =Exit).place(x = 800,y = 400) 	#to create button





			
			win2.mainloop()
		else:
			messagebox.showinfo("Invalid Login","Try Next Time")
			win1.destroy()

def Reset():
		Sregno.delete(0,END)
		Accyear.set("Select Acc Year")
		Dept.set("Select Dept Name")
		Spwd.delete(0,END)
def Exit():
		win1.destroy()
#====================================================
#win1.geometry('500x500')  #without this window is small
win1.maxsize(500,500)		#set maximum size
win1.minsize(500,500) 		#set minimum size
win1.title ("Admin Login Page") 		#set the title
win1.configure(bg = "pink")		#set the color of the page

Label(win1, text = "Student Login Here", font=('Ebrima',18),bg="orange",fg = "white", width = 39,relief = 'groov').place(x=0,y=0)   #create label text


Label(win1, text = "Student Regno", font=('Ebrima',15),fg = "black", width = 15,relief = 'raised').place(x=30,y=100)		#Create admin user id label
Sregno = Entry(win1,font = ('Ebrima',15),bg = 'white', fg = 'black', width = 20)
Sregno.place(x = 250,y = 100)		#input text here
Sregno = Entry(win1,font = ('Ebrima',15),bg = 'white', fg = 'black', width = 20)
Sregno.place(x = 250,y = 100)		#input text here


Label(win1, text = "Select Acad Year", font=('Ebrima',15),fg = "black", width = 15,relief = 'raised').place(x=30,y=150)		#Create admin user id label
Accyear= StringVar()
Accyear.set("Select Any  Academic Year")
menu1=OptionMenu(win1,Accyear,"2019-2023","2020-2024","2021-2025","2022-2026","2023-2027","2024-2028")
menu1.place(x=250,y=150)


Label(win1, text = "Select Dept", font=('Ebrima',15),fg = "black", width = 15,relief = 'raised').place(x=30,y=200)		#Create admin user id label
Dept = StringVar()
Dept.set("-- Select Department Name --")
menu2 = OptionMenu(win1,Dept,"CSE","CSIT","EEE","ME","CIVIL")
menu2.place(x=250,y=200)


Label(win1, text = "Enter Password", font=('Ebrima',15),fg = "black", width = 15,relief = 'raised').place(x=30,y=250)		#Create admin user id label
Spwd = Entry(win1,font = ('Ebrima',15),bg = 'white', fg = 'black', width = 20, show = "*")
Spwd.place(x = 250,y = 250)		#input text here


Button(win1, text = 'RESET', font=('Ebrima',15), width = 10, height = 1,fg = 'red', activebackground = '#ccfb5d', relief = 'raised', command  = Reset).place(x = 50,y = 340) 	#to create button


Button(win1, text = 'LOGIN', font=('Ebrima',15), width = 10, height = 1,fg = 'red', activebackground = '#ccfb5d', relief = 'raised', command  = Login).place(x = 200,y = 340) 	#to create button


Button(win1, text = 'EXIT', font=('Ebrima',15), width = 10, height = 1,fg = 'red', activebackground = '#ccfb5d', relief = 'raised', command  = Exit).place(x = 350,y = 340) 	#to create button


win1.mainloop ()  #Display window
