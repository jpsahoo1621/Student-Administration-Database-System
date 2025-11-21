from tkinter import *
from tkinter import messagebox
import csv

from pymysql import *
conobj = connect (host = 'localhost',user = 'root', password='',port = 3306)
curobj = conobj.cursor()
curobj.execute('use project;')
win1 = Tk ()

#==================================================
def  Reset():
	pass
#--------------------
def  Exit():
	win1.destroy()
#--------------------
def Login():
	#print(AUid.get())
	#print(Apwd.get())
	r = 'select * from admin where AUser= "{}" and APwd = "{}" ; '.format(AUid.get(),Apwd.get())
	curobj.execute(r)
	record = curobj.fetchall()
	if len(record):
		win1.destroy()
		messagebox.showinfo("Login Successful","Welcome to Admin Home Page")
		win2=Tk	()	#create new window


		#=============================================
		def AddStudent():
			win2.destroy()
			win3=Tk()
		#=============================================
			def Submit():
				#print(Sregno.get(),Sname.get(),Accyear.get(),Dept.get(),Spwd.get())

				r = 'insert into student (Regno,Name,Accyear,Dept,Password) values({},"{}","{}","{}","{}")'.format(Sregno.get(),Sname.get(),Accyear.get(),Dept.get(),Spwd.get())
				curobj.execute(r)
				conobj.commit()
				win3.destroy()
			def Reset():
				Sregno.delete(0,END)
				Sname.delete(0,END)
				Dept.set("Select Dept. Name")
				Accyear.set("Select Academic Year")
				Spwd.delete(0,END)

		#=============================================
			win3.maxsize(500,500)		#set maximum size
			win3.minsize(500,500) 		#set minimum size
			win3.configure(bg = "violet")
			win3.title("Add New Student")
			Label(win3, text = "Student Reg. No.", font=('Ebrima',15),fg = "black", width = 15,relief = 'raised').place(x=30,y=50)		#Create admin user id label
			Sregno = Entry(win3,font = ('Ebrima',15),bg = 'white', fg = 'black', width = 20)
			Sregno.place(x = 250,y = 50)		#input text here

			Label(win3, text = "Student Name", font=('Ebrima',15),fg = "black", width = 15,relief = 'raised').place(x=30,y=120)		#Create admin user id label
			Sname = Entry(win3,font = ('Ebrima',15),bg = 'white', fg = 'black', width = 20)
			Sname.place(x = 250,y = 120)		#input text here

			Label(win3, text = "Select Acad. Year", font=('Ebrima',15),fg = "black", width = 15,relief = 'raised').place(x=30,y=190)		#Create admin user id label
			Accyear= StringVar()
			Accyear.set("Select Any  Academic Year")
			menu1 = OptionMenu(win3,Accyear,"2019-2023","2020-2024","2021-2025","2022-2026","2023-2027","2024-2028")
			menu1.place(x=250,y=190)

			Label(win3, text = "Select Dept. Name", font=('Ebrima',15),fg = "black", width = 15,relief = 'raised').place(x=30,y=260)		#Create admin user id label
			Dept = StringVar()
			Dept.set("-- Select Department Name --")
			menu2 = OptionMenu(win3,Dept,"CSE","CSIT","EEE","ME","CIVIL")
			menu2.place(x=250,y=260)
			

			Label(win3, text = "Enter Password", font=('Ebrima',15),fg = "black", width = 15,relief = 'raised').place(x=30,y=330)		#Create admin user id label
			Spwd = Entry(win3,font = ('Ebrima',15),bg = 'white', fg = 'black', width = 20)
			Spwd.place(x = 250,y = 330)		#input text here


			Button(win3, text = 'RESET', font=('Ebrima',15), width = 10, height = 1,fg = 'red', activebackground = '#ccfb5d', relief = 'raised',command = Reset).place(x = 50,y = 400) 	#to create button


			Button(win3, text = 'SUBMIT', font=('Ebrima',15), width = 10, height = 1,fg = 'red', activebackground = '#ccfb5d', relief = 'raised', command = Submit).place(x = 200,y = 400) 	#to create button


			Button(win3, text = 'EXIT', font=('Ebrima',15), width = 10, height = 1,fg = 'red', activebackground = '#ccfb5d', relief = 'raised', command = Exit).place(x = 350,y = 400) 	#to create button


			win3.mainloop()
		#---------------------------------------------
		def DownloadStudent():
			
			curobj.execute("select * from student;")
			record = curobj.fetchall()
			
			fobj=open("studentdetails.txt","w")
			fobj1= open("student.csv","w",newline = "\n")
			cobj = csv.writer(fobj1)
			cobj.writerow(["Regno" ,"Name" , "Parent" ," Gender" , "Accyear" ,  " Dept" ," Contact" ," Password "])
			for row in record:
				fobj.write(str(row))
				cobj.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
				fobj.write("\n")
			fobj.close()
			messagebox.showinfo('Download Complete','Thank You')
			win2.destroy()
		#---------------------------------------------
		def Exit():
			win2.destroy()

		#=============================================


		win2.maxsize(500,500)		#set maximum size
		win2.minsize(500,500) 		#set minimum size
		win2.configure(bg = "light blue")
		win2.title("Admin Home Page")

		Button(win2, text = "Add New Student ",width = 25, height = 1,fg = 'red', 						activebackground = '#ccfb5d', relief = 'raised',font=('Ebrima',18), command = AddStudent).place(x =70,y = 50)

		Button(win2, text = "Download Student Details",width = 25, height = 1,fg = 'red', activebackground = '#ccfb5d', relief = 'raised',font=('Ebrima',18), command = DownloadStudent).place(x =70,y = 150)

		Button(win2, text = "Exit",width = 25, height = 1,fg = 'red', 				    					activebackground = '#ccfb5d', relief = 'raised',font=('Ebrima',18),command=Exit).place(x =70,y = 250)

		win2.mainloop()
	else:
		print("Invalid Login")
		win1.destroy()

#====================================================
#win1.geometry('500x500')  #without this window is small
win1.maxsize(500,500)		#set maximum size
win1.minsize(500,500) 		#set minimum size
win1.title ("Admin Login Page") 		#set the title
win1.configure(bg = "pink")		#set the color of the page

Label(win1, text = "Admin Login Here", font=('Ebrima',18),bg="orange",fg = "white", width = 39,relief = 'groov').place(x=0,y=50)   #create label text


Label(win1, text = "Admin User Id", font=('Ebrima',15),fg = "black", width = 15,relief = 'raised').place(x=30,y=180)		#Create admin user id label
AUid = Entry(win1,font = ('Ebrima',15),bg = 'white', fg = 'black', width = 20)
AUid.place(x = 250,y = 180)		#input text here


Label(win1, text = "Admin Password", font=('Ebrima',15),fg = "black", width = 15,relief = 'raised').place(x=30,y=250)		#Create admin user id label
Apwd = Entry(win1,font = ('Ebrima',15),bg = 'white', fg = 'black', width = 20, show = "*")
Apwd.place(x = 250,y = 250)		#input text here


Button(win1, text = 'RESET', font=('Ebrima',15), width = 10, height = 1,fg = 'red', activebackground = '#ccfb5d', relief = 'raised', command  = Reset).place(x = 50,y = 340) 	#to create button


Button(win1, text = 'LOGIN', font=('Ebrima',15), width = 10, height = 1,fg = 'red', activebackground = '#ccfb5d', relief = 'raised', command  = Login).place(x = 200,y = 340) 	#to create button


Button(win1, text = 'EXIT', font=('Ebrima',15), width = 10, height = 1,fg = 'red', activebackground = '#ccfb5d', relief = 'raised', command  = Exit).place(x = 350,y = 340) 	#to create button


win1.mainloop ()  #Display window
