import tkinter as tk
import mysql.connector
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import webbrowser


class Demo1( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        root = Tk()
        root.geometry("1000x500")
        Path2 = 'C:\\Users\\MY PC\\Desktop\\bg.jpg'
        imageFile = ImageTk.PhotoImage(Image.open(Path2))
        pane1 = Label(self, image=imageFile)
        pane1.pack(side = "bottom",fill = "both",expand = "yes")
        self.pack()
        self.master.title("Library Management System")
        self.button1 = Button( self, text = "Wanna switch to SQL", width = 25,
                               command = self.new_window )
        self.button1.pack()

        def open1():
            webbrowser.open(webbrowser.open(r'C:\Users\MY PC\Desktop\Desktop Files\OSTURNING.swf'))

        def aboutus():
            print(
                "\n\nOur project is Library management . It provides the online view of Library. We have also provided the flipping effect for books which gives the real book reading experience."
                "\nComing to the technicalities of the project, We have achieved really big one. We have successfully achieved the link between a query language(SQL) and a programming language(PYTHON)."
                "\nFlipping effect , its one of the important aspect in our project. It needs herculian task to finish the flipping effect using ADOBE aftereffects."
                "\nSpeciality :"
                "\nDBMS projects are usually written with a user-name and a password,with a cheap GUI. But we have made a clear GUI with no username and password stuff."
                "\nComing to the contribution of the teammates, we have really worked hard for our project.Our project is big because it involves coding skills as well as graphic technicalities."
                "\nEvery one of us have tried their level best in making this project a good success")

        def cse1():
            webbrowser.open(
                webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\cse\web development\web development.swf'))

        def cse2():
            webbrowser.open(
                webbrowser.open((r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\cse\dld_morris\dld_morris.swf')))

        def cse3():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\cse\computer networking\computer networking.swf'))

        def cse4():
            webbrowser.open(webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\cse\toc\toc.swf'))

        def cse5():
            webbrowser.open(webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\cse\os\os.swf'))

        def cse6():
            webbrowser.open(webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\cse\c++\c++.swf'))

        def cse7():
            webbrowser.open(webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\cse\cao\cao.swf'))

        def cse8():
            webbrowser.open(webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\cse\web programming\web.swf'))

        # ECE Functions
        def ece1():
            webbrowser.open(webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\ece\dc\dc.swf'))

        def ece2():
            webbrowser.open(
                webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\ece\linear algebra\linear algebra.swf'))

        def ece3():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\ece\mobile ad networking\mobile ad networking.swf'))

        def ece4():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\ece\systems and signals\systems and signals.swf'))

        def ece5():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\ece\systems and signals\systems and signals.swf'))

        def ece6():
            webbrowser.open(webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\ece\analog_2\analog.swf'))

        def ece7():
            webbrowser.open(webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\ece\antenas\antenas.swf'))

        def ece8():
            webbrowser.open(
                webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\ece\semiconductors\semiconductors.swf'))

        def ece9():
            webbrowser.open(webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\ece\sensors\sensors.swf'))

        def eee1():
            webbrowser.open(
                webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\bit\bio_thermodynamics\bio_thermo.swf'))

        def eee2():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\bit\Bioinformatics-Sequence and Genome Analysis\bio informatics.swf'))

        def eee3():
            webbrowser.open(
                webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\bit\downstream pro\downstream pro.swf'))

        def eee4():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\bit\genetics and micro bio\genetics and micro bio.swf'))

        def eee5():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\bit\heat transfer bio\heat transfer bio.swf'))

        def eee6():
            webbrowser.open(
                webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\bit\pharmaceutical\pharmaceutical.swf'))

        def eee7():
            webbrowser.open(webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\bit\plant_bio\plant_bio.swf'))

        def mech1():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\mechanical\dynamics of machines\dynamics of machines.swf'))

        def mech2():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\mechanical\strenth of materials\strength of materials.swf'))

        def mech3():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\mechanical\strenth of materials\strength of materials.swf'))

        def mech4():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\mechanical\thermodynamics\thermodynamics.swf'))

        def mech5():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\mechanical\heat and mass transfer\heat and mass transfer.swf'))

        def mech6():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\mechanical\fluid mechanics\fluid mechanics.swf'))

        def mech7():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\mechanical\behaviour of materials\behaviour of materials.swf'))

        def mech8():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\mechanical\manufacturing\manufacturing.swf'))

        def civil1():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\civil\construction engineering\computational fluid.swf'))

        def civil2():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\civil\control systems\control systems.swf'))

        def civil3():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\civil\environmental engineering\environmental engineering.swf'))

        def civil4():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\civil\geo technical engineering\geo technical engineering.swf'))

        def civil5():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\civil\micro electronics\micro electronics.swf'))

        def civil6():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\civil\power semi conductors\micro electronics.swf'))

        def civil7():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\civil\structural engineering\structural engineering.swf'))

        def mis1():
            webbrowser.open(webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\mis\dbms\dbms.swf'))

        def mis2():
            webbrowser.open(webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\mis\dlmp\dlmp.swf'))

        def mis3():
            webbrowser.open(webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\mis\dsa\dsa.swf'))

        def mis4():
            webbrowser.open(webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\mis\eee\eee.swf'))

        def mis5():
            webbrowser.open(webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\mis\evs\evs.swf'))

        def mis6():
            webbrowser.open(webbrowser.open(
                r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\mis\programing in java\programming in java.swf'))

        def mis7():
            webbrowser.open(webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\mis\stats\stats.swf'))

        def bio1():
            webbrowser.open(
                webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\bcb\calculus_1\calculus-1.swf'))

        def bio2():
            webbrowser.open(
                webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\bcb\chemical_bio\Untitled-2.swf'))

        def bio3():
            webbrowser.open(
                webbrowser.open(r'C:\Users\MY PC\Desktop\dbms_pdf_after edit\bcb\humanities\humanities.swf'))




        root.wm_title("\t\t\tLIBRARY MANAGEMENT SYSTEM")

        Menubar = Menu(root)
        root.config(menu=Menubar)  # configuring a menu
        Submenu = Menu(Menubar)
        Menubar.add_cascade(label="About Us", menu=Submenu)  # to add a menu in a menubar,to designate a submenu
        Submenu.add_command(label="Information",command = aboutus)
        Menubar2 = Menu(Menubar)
        Menubar.add_cascade(label="Courses", menu=Menubar2)
        Submenu2 = Menu(Menubar2)

        Menubar3 = Menu(Menubar2)
        # CSE CORE SUBJECTS AND ITS PROGRAMMING STARTS HERE
        cse = Menu(Menubar2)
        Menubar2.add_cascade(label="Computer Science", menu=cse)
        dsa = Menu(Menubar3)
        cse.add_cascade(label='DATASTRUCTURES', menu=dsa)
        dsa.add_command(label="Datastructures and algorithms by Bhoominathan", command=cse1)
        dld = Menu(Menubar3)
        cse.add_cascade(label='DIGITAL LOGIC and DESIGN', menu=dld)
        dld.add_command(label='Digital logic and design by morris manno', command=cse2)
        net = Menu(Menubar3)
        cse.add_cascade(label='NETWORK AND COMMUNICATION', menu=net)
        net.add_command(label='Network and Communication by ', command=cse3)
        toc = Menu(Menubar3)
        cse.add_cascade(label='Theory of Computation and compiler design', menu=toc)
        toc.add_command(label='Theory of computaion by john', command=cse4)
        os = Menu(Menubar3)
        cse.add_cascade(label='OPERATING SYSTEM', menu=os)
        os.add_command(label='Operating system by Silberschatz', command=cse5)
        dbms = Menu(Menubar3)
        cse.add_cascade(label='DATABASE MANAGEMENT SYSTEMS', menu=dbms)
        dbms.add_command(label='DATABASE SYSTEMS BY ELMASREE AND NAVATHE', command=cse6)
        cao = Menu(Menubar3)
        cse.add_cascade(label='COMPUTER ARCHITECTURE', menu=cao)
        cao.add_command(label='Computer architecture by Morris Mano', command=cse7)
        web = Menu(Menubar3)
        cse.add_cascade(label='WEB PROGRAMMING', menu=web)
        web.add_command(label='Web programming by lewis', command=cse8)

        # ECE CORE SUBJECTS AND ITS CORE PROGRAMMING STARTS HERE
        ece = Menu(Menubar2)
        Menubar2.add_cascade(label="Electronic Communication and engineering", menu=ece)
        edc = Menu(Menubar3)
        ece.add_cascade(label='Electronics and Devices circuits', menu=edc)
        edc.add_command(label='Electronics and Devices circuits', command=ece1)
        eca = Menu(Menubar3)
        ece.add_cascade(label='Electrical circuit analysis', menu=eca)
        eca.add_command(label='Electrical circuit analysis by ', command=ece2)
        prob = Menu(Menubar3)
        ece.add_cascade(label='Probability theory and stochastic process ', menu=prob)
        prob.add_command(label='Probability theory and stochastic process', command=ece3)
        dsp = Menu(Menubar3)
        ece.add_cascade(label='Digital Signal processing', menu=dsp)
        dsp.add_command(label='Digital Signal Processing', command=ece4)
        sas = Menu(Menubar3)
        ece.add_cascade(label='Signals and Systems', menu=sas)
        sas.add_command(label='Signals and Systems by ', command=ece5)
        ana = Menu(Menubar3)
        ece.add_cascade(label='Analog Communications', menu=ana)
        ana.add_command(label='Analog Communication by ', command=ece6)
        mp = Menu(Menubar3)
        ece.add_cascade(label='MicroProcessor and Micro Controllers', menu=mp)
        mp.add_command(label='Microprocessor and Microcontrollers by ', command=ece7)
        ele = Menu(Menubar3)
        ece.add_cascade(label='Electromagnetic theory and Transmission lines', menu=ele)
        ele.add_command(label='Electromagnetic theory and transmission lines by ', command=ece8)
        oe = Menu(Menubar3)
        ece.add_cascade(label='Opto electronics', menu=oe)
        oe.add_command(label="Opto electronics by ", command=ece9)

        # HERE ONWARDS WE CODE ABOUT EEE CORE SUBJECTS
        eee = Menu(Menubar2)
        Menubar2.add_cascade(label='Electrical Engeneering', menu=eee)
        ec = Menu(Menubar3)
        eee.add_cascade(label='Electrical Circuit Analysis', menu=ec)
        ec.add_command(label='Electrical Circuit analysis by .....')
        ee = Menu(Menubar3)
        eee.add_cascade(label='Engeneering Economy', menu=ee)
        ee.add_command(label='Engeneering economy by....')
        ssf = Menu(Menubar3)
        eee.add_cascade(label='Solid state fundamentals', menu=ssf)
        ssf.add_command(label='Solid state fundamentals by....')
        am = Menu(Menubar3)
        eee.add_cascade(label='Analytical Methods for continuos time systems', menu=am)
        am.add_command(label='Analytical Methods for continuos time systems by ....')
        ecs = Menu(Menubar3)
        eee.add_cascade(label='Intro to embeded computer systems', menu=ecs)
        ecs.add_command(label='Intro to embeded computer systems')
        eam = Menu(Menubar3)
        eee.add_cascade(label='Electricity and Magnetism', menu=eam)
        eam.add_command(label='Electricity and magnetism by ....')
        Ee = Menu(Menubar3)
        eee.add_cascade(label='Electromagnetic Engeneering', menu=Ee)
        Ee.add_command(label='Electronic Engeneering by.....')

        # WE TAKE ON MECHANICAL ENGENEERING
        mech = Menu(Menubar2)
        Menubar2.add_cascade(label='Mechanichal Engeneering', menu=mech)
        sad = Menu(Menubar3)
        mech.add_cascade(label='Stats and Dynamics', menu=sad)
        sad.add_command(label='Stats and Dynamics by...', command=mech1)
        som = Menu(Menubar3)
        mech.add_cascade(label='Strength of Materials', menu=som)
        som.add_command(label='Strength of material by .....', command=mech2)
        me = Menu(Menubar3)
        mech.add_cascade(label='Material Engeneering', menu=me)
        me.add_command(label='Material Engeneering by ...', command=mech2)
        Td = Menu(Menubar3)
        mech.add_cascade(label='Thermodynamics', menu=Td)
        Td.add_command(label='Thermodynamics by ....', command=mech4)
        fuels = Menu(Menubar3)
        mech.add_cascade(label='Fuels,Combustion,Internal Combustion engine', menu=fuels)
        fuels.add_command(label='Fuels and combustion by ....', command=mech5)
        fluid = Menu(Menubar3)
        mech.add_cascade(label='Fluid Mechanics', menu=fluid)
        fluid.add_command(label='Fluid mechanics by .....', command=mech6)
        instru = Menu(Menubar3)
        mech.add_cascade(label='Instrumentation', menu=instru)
        instru.add_command(label='Instrumentation by ....', command=mech7)
        manu = Menu(Menubar3)
        mech.add_cascade(label='Manufacturing Engeneering', menu=manu)
        manu.add_command(label='Manufacturing Engeneering by...', command=mech8)

        # WE GO ON THE BUILDERS:)

        civil = Menu(Menubar2)
        Menubar2.add_cascade(label='Civil Engeneering', menu=civil)
        bom = Menu(Menubar3)
        civil.add_cascade(label='Construction Engeneering ', menu=bom)
        bom.add_command(label='construction engeneering by ....', command=civil1)
        te = Menu(Menubar3)
        civil.add_cascade(label='Control Systems', menu=te)
        te.add_command(label='Control systems by ....', command=civil2)
        ce = Menu(Menubar3)
        civil.add_cascade(label='Environmental Engeneering', menu=ce)
        ce.add_command(label='Environmental Engeneering engineering by ...', command=civil3)
        EE = Menu(Menubar3)
        civil.add_cascade(label='Geo technical Engineering', menu=EE)
        EE.add_command(label='Geo technical Engeneering by .....', command=civil4)
        wr = Menu(Menubar3)
        civil.add_cascade(label='Micro Electronics', menu=wr)
        wr.add_command(label='Micro Electronics by ...', command=civil5)
        SE = Menu(Menubar3)
        civil.add_cascade(label='Power Semi Conductors', menu=SE)
        SE.add_command(label='Power Semiconductors by ....', command=civil6)
        ge = Menu(Menubar3)
        civil.add_cascade(label='Structural Engeneering', menu=ge)
        ge.add_command(label='Structural  Engineering by...', command=civil7)

        # Now we deal with the MIS(5 years)

        mis = Menu(Menubar2)
        Menubar2.add_cascade(label='Software Engeneering', menu=mis)
        Dbms = Menu(Menubar3)
        mis.add_cascade(label='Database Management', menu=Dbms)
        Dbms.add_command(label='Database Management by ....')
        dlmp = Menu(Menubar3)
        mis.add_cascade(label='DLMP', menu=dlmp)
        dlmp.add_command(label='DLMP')
        Dsa = Menu(Menubar3)
        mis.add_cascade(label='Datastructure', menu=Dsa)
        Dsa.add_command(label='Datastructures by ')
        EeE = Menu(Menubar3)
        mis.add_cascade(label='Electrical and electronic engeneering', menu=EeE)
        EeE.add_command(label='Electrical and Electronic engeneering by ')
        evs = Menu(Menubar3)
        mis.add_cascade(label='Environmental Studies', menu=evs)
        evs.add_command(label='Enviromental sciences by Koushick')
        java = Menu(Menubar3)
        mis.add_cascade(label='Programming in JAVA', menu=java)
        java.add_command(label='Programming in java by ')
        stats = Menu(Menubar3)
        mis.add_cascade(label='STATISTICS ', menu=stats)
        stats.add_command(label='Statistics by ...')

        # Tribute to BCB

        bcb = Menu(Menubar2)
        Menubar2.add_cascade(label='Computerscience with Biology', menu=bcb)
        cal = Menu(Menubar3)
        bcb.add_cascade(label='Calculus for engeneers', menu=cal)
        cal.add_command(label='Calculus for engeneers by ..')
        bio = Menu(Menubar3)
        bcb.add_cascade(label='Chemistry and biology', menu=bio)
        bio.add_command(label='Chemistry and biology by..')
        hum = Menu(Menubar3)
        bcb.add_cascade(label='Humanities for students ', menu=hum)
        hum.add_command(label='Humanities for students by')

    def new_window(self):
        self.newWindow = Demo2()

class Demo2(Frame):
    def __init__(self):
        new =tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("SQL")
        cnx = mysql.connector.Connect(user='udaymysql', password='udayvitian', host='  172.16.30.221', database='mydb')
        cursor = cnx.cursor()

        def total1():
            cnx = mysql.connector.Connect(user='udaymysql', password='udayvitian', host=' 172.16.30.221',
                                          database='mydb')
            cursor = cnx.cursor()
            query = ("SELECT * FROM lib")
            cursor.execute(query)
            for (course, sub, book_name, id) in cursor:
                print("{}, {}, {}".format(course, sub, book_name, id))

        def total2():
            cnx = mysql.connector.Connect(user='udaymysql', password='udayvitian', host=' 172.16.30.221',
                                          database='mydb')
            cursor = cnx.cursor()
            query = ("SELECT * FROM student")
            cursor.execute(query)
            for (name, book_name) in cursor:
                print("{}, {}".format(name, book_name))

        def name():
            cnx = mysql.connector.Connect(user='udaymysql', password='udayvitian', host='  172.16.30.221',
                                          database='mydb')
            cursor = cnx.cursor()
            query = ("SELECT name FROM student")
            cursor.execute(query)
            for (name) in cursor:
                print("{}".format(name))

        def course():
            cnx = mysql.connector.Connect(user='udaymysql', password='udayvitian', host=' 172.16.30.221',
                                          database='mydb')
            cursor = cnx.cursor()
            query = ("SELECT DISTINCT  course FROM lib")
            cursor.execute(query)
            for (course) in cursor:
                print("{}".format(course))

        def ex():
            cnx = mysql.connector.Connect(user='udaymysql', password='udayvitian', host=' 172.16.30.221',
                                          database='mydb')
            cursor = cnx.cursor()
            query = (
            "SELECT student.name,lib.course,lib.book_name FROM student INNER JOIN lib ON lib.book_name = student.book_name")
            cursor.execute(query)
            for (name, course, book_name) in cursor:
                print(" {},{},{} ".format(name, course, book_name))





        b2 = Button(new, text='Total Library data', command=total1)
        b3 = Button(new, text='Total student data', command=total2)
        b4 = Button(new, text='Name of Students', command=name)
        b5 = Button(new, text='List of courses', command=course)
        b4.bind()
        b4.pack()
        b5.bind()
        b5.pack()
        b3.bind()
        b3.pack()
        b1 = Button(new, text='SQL button1', command=ex)
        b2.bind()
        b2.pack()

        new.button = tk.Button(  text = "Quit SQL", width = 25,
                                 command = self.close_window )
        new.button.pack()
        cursor.close()
        cnx.close()

    def close_window(self):
        self.destroy()

def main():
    Demo1().mainloop()

if __name__ == '__main__':
main()
