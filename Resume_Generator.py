from tkinter import *
from pyautogui import *
from tkinter.filedialog import *
from PIL import *
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
b=0
def new():
    font1=("Times new Roman",20)
    font2=("Times new Roman",15)
    master=Tk()
    master.configure(bg="#ffa07a")
    master.title("Resume Builder")
    master.geometry('1300x1200+320+0')
    #Label(master,text="",font=("Times new Roman",30,"bold","italic"),bg="#ffa07a").pack()
    Label(master,text="Resume Builder",font=("Times new Roman",25,"bold"),bg="#ffa07a").pack()
    
    my_canvas=Canvas(master,width=1100,bg="#ffdab9",highlightbackground="#ff8c69", highlightthickness=2)

    my_canvas.pack(side=LEFT,fill=Y,expand=1)

    my_scrollbar=Scrollbar(master,orient=VERTICAL,command=my_canvas.yview)

    my_scrollbar.pack(side=RIGHT,fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)

    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    root=Frame(my_canvas)

    my_canvas.create_window((120,100),window=root,anchor="nw")
    root.configure(bg="#ffdab9")
    master.title("Application Form")
    
    #layout adjustments
    Label(root,text="     ",font=font1,bg="#ffdab9").grid(row=1,column=1,sticky='w')
    Label(root,text="     ",font=font1,bg="#ffdab9").grid(row=1,column=100,sticky='w')
    
    #objective
    Label(root,text="Objective",font=font1,bg="#ffdab9").grid(row=2,column=0,sticky='w')
    obj=Text(root,width=25,height=3,font=font2)
    obj.grid(row=2,column=11)
    
    #creating a label Called Candidate's name

    Label(root,text="Candidate's Name",font=font1,bg="#ffdab9").grid(row=7,column=0,sticky='w')

    cname=StringVar(root)
    Entry(root,width=25,textvariable=cname,font=font2).grid(row=7,column=11,sticky='w')

    
    #Job position

    Label(root,text="Job Applying",font=font1,bg="#ffdab9").grid(row=12,column=0,sticky='w')

    job=StringVar(root)
    Entry(root,width=25,textvariable=job,font=font2).grid (row=12,column=11,sticky='w')


    #Mobile Number

    Label(root,text="Mobile Number",font=font1,bg="#ffdab9").grid(row=14,column=0,sticky='w')

    mobile=StringVar(root)
    Entry(root,width=25,textvariable=mobile,font=font2).grid(row=14,column=11,sticky='w')

    #Email address

    Label(root,text="E-mail address",font=font1,bg="#ffdab9").grid(row=15,column=0,sticky='w')

    email=StringVar(root)
    Entry(root,width=25,textvariable=email,font=font2).grid(row=15,column=11,sticky='w')

    #Address
    
    Label(root,text="Address",font=font1,bg="#ffdab9").grid(row=16,column=0,sticky='w')
    add=Text(root,width=25,height=3,font=font2)
    add.grid(row=16,column=11,sticky='w')
    
    
    #SSC details

    Label(root,text="**Enter your SSC details**",font=("Times new Roman",20,'bold'),bg="#ffdab9").grid(row=19,column=0,sticky='w')

    Label(root,text="Institution",font=font1,bg="#ffdab9").grid(row=20,column=0,sticky='w')
    ssc_ins=StringVar(root)
    Entry(root,width=25,textvariable=ssc_ins,font=font2).grid(row=20,column=11,sticky='w')

    Label(root,text="Board",font=font1,bg="#ffdab9").grid(row=21,column=0,sticky='w')
    ssc_b=StringVar(root)
    Entry(root,width=25,textvariable=ssc_b,font=font2).grid(row=21,column=11,sticky='w')

    Label(root,text="Year of Passing",font=font1,bg="#ffdab9").grid(row=22,column=0,sticky='w')
    ssc_p=StringVar(root)
    Entry(root,width=25,textvariable=ssc_p,font=font2).grid(row=22,column=11,sticky='w')

    Label(root,text="Percentage",font=font1,bg="#ffdab9").grid(row=23,column=0,sticky='w')
    ssc_per=StringVar(root)
    Entry(root,width=25,textvariable=ssc_per,font=font2).grid(row=23,column=11,sticky='w')

    #Intermediate details

    Label(root,text="**Enter your Intermediate details**",font=("Times new Roman",20,'bold'),bg="#ffdab9").grid(row=24,column=0,sticky='w')

    Label(root,text="Institution",font=font1,bg="#ffdab9").grid(row=25,column=0,sticky='w')
    inter_ins=StringVar(root)
    Entry(root,width=25,textvariable=inter_ins,font=font2).grid(row=25,column=11,sticky='w')

    Label(root,text="Board",font=font1,bg="#ffdab9").grid(row=26,column=0,sticky='w')
    inter_b=StringVar(root)
    Entry(root,width=25,textvariable=inter_b,font=font2).grid(row=26,column=11,sticky='w')

    Label(root,text="Year of Passing",font=font1,bg="#ffdab9").grid(row=27,column=0,sticky='w')
    inter_p=StringVar(root)
    Entry(root,width=25,textvariable=inter_p,font=font2).grid(row=27,column=11,sticky='w')

    Label(root,text="Percentage",font=font1,bg="#ffdab9").grid(row=28,column=0,sticky='w')
    inter_per=StringVar(root)
    Entry(root,width=25,textvariable=inter_per,font=font2).grid(row=28,column=11,sticky='w')

    #Higher Education details

    Label(root,text="**Enter your Higher education details**",font=("Times new Roman",20,'bold'),bg="#ffdab9").grid(row=29,column=0,sticky='w')

    Label(root,text="Institution",font=font1,bg="#ffdab9").grid(row=30,column=0,sticky='w')
    hedu_ins=StringVar(root)
    Entry(root,width=25,textvariable=hedu_ins,font=font2).grid(row=30,column=11,sticky='w')

    Label(root,text="Course",font=font1,bg="#ffdab9").grid(row=31,column=0,sticky='w')
    hedu_b=StringVar(root)
    Entry(root,width=25,textvariable=hedu_b,font=font2).grid(row=31,column=11,sticky='w')

    Label(root,text="Year of Passing",font=font1,bg="#ffdab9").grid(row=32,column=0,sticky='w')
    hedu_p=StringVar(root)
    Entry(root,width=25,textvariable=hedu_p,font=font2).grid(row=32,column=11,sticky='w')

    Label(root,text="Percentage",font=font1,bg="#ffdab9").grid(row=33,column=0,sticky='w')
    hedu_per=StringVar(root)
    Entry(root,width=25,textvariable=hedu_per,font=font2).grid(row=33,column=11,sticky='w')

    #Technical skills

    Label(root,text="Technical skills",font=font1,bg="#ffdab9").grid(row=34,column=0,sticky='w')
    tskills=Text(root,width=25,height=3,font=font2)
    tskills.grid(row=34,column=11,sticky='w')
    
    Label(root,text="  ",font=font1,bg="#ffdab9").grid(row=37,column=0,sticky='w')

    
    #strengths

    Label(root,text="Strengths",font=font1,bg="#ffdab9").grid(row=42,column=0,sticky='w')
    strength=Text(root,width=25,height=3,font=font2)
    strength.grid(row=42,column=11,sticky='w')
    

    #work Experience

    Label(root,text="**Work Experience**",font=("Times new Roman",20,'bold'),bg="#ffdab9").grid(row=45,column=0,sticky='w')
    Label(root,text="Timeline  ",font=font1,bg="#ffdab9").grid(row=46,column=0,sticky='w')
    t_line=StringVar(root)
    Entry(root,width=25,textvariable=t_line,font=font2).grid(row=46,column=11,sticky='w')
    Label(root,text="Company",font=font1,bg="#ffdab9").grid(row=47,column=0,sticky='w')
    com=StringVar(root)
    Entry(root,width=25,textvariable=com,font=font2).grid(row=47,column=11,sticky='w')
    Label(root,text="Job Position",font=font1,bg="#ffdab9").grid(row=48,column=0,sticky='w')
    J_pos=StringVar(root)
    Entry(root,width=25,textvariable=J_pos,font=font2).grid(row=48,column=11,sticky='w')
    Label(root,text="Job Description",font=font1,bg="#ffdab9").grid(row=49,column=0,sticky='w')
    J_des=StringVar(root)
    Entry(root,width=25,textvariable=J_des,font=font2).grid(row=49,column=11,sticky='w')
    def new_exp():
        global b, t_line1, com1, J_pos1,J_des1
        b=2
        Label(root,text="Timeline   ",font=font1,bg="#ffdab9").grid(row=50,column=0,sticky='w')
        t_line1=StringVar(root)
        Entry(root,width=25,textvariable=t_line1,font=font2).grid(row=50,column=11,sticky='w')
        Label(root,text="Company",font=font1,bg="#ffdab9").grid(row=51,column=0,sticky='w')
        com1=StringVar(root)
        Entry(root,width=25,textvariable=com1,font=font2).grid(row=51,column=11,sticky='w')
        Label(root,text="Job Position",font=font1,bg="#ffdab9").grid(row=52,column=0,sticky='w')
        J_pos1=StringVar(root)
        Entry(root,width=25,textvariable=J_pos1,font=font2).grid(row=52,column=11,sticky='w')
        Label(root,text="Job Description",font=font1,bg="#ffdab9").grid(row=53,column=0,sticky='w')
        J_des1=StringVar(root)
        Entry(root,width=25,textvariable=J_des1,font=font2).grid(row=53,column=11,sticky='w')
    Button(root,text='Another experience',command=new_exp).grid(row=50,column=0,sticky='w')
    #pic
    Label(root,text='Upload your picture',font=font1,bg="#ffdab9").grid(row=55,column=0,sticky='w')
    def upload_file():
        try:
            global img
            f_types = [('Jpg Files', '*.jpg'),('Jpeg Files','*.jpeg'),('Jfif File','.jfif')]
            filename =askopenfilename(filetypes=f_types)
            img = Image.open(filename)
            width ,height=img.size
            if (width >height):
                
                size=(width//2-height//2,0,width//2+height//2,height)
                img=img.crop(size)
            else:
                size=(0,0,width,width)
                img=img.crop(size)
        except:
            pass
    Button(root, text='Upload File', width=20,command = upload_file).grid(row=55,column=11)

    #subbmitting/ creatinthe pdf
    def ok():
        files=[('Pdf Files','*.pdf')]
        filename=asksaveasfile(mode='wb',filetypes = files,defaultextension=files)
        C=canvas.Canvas(filename,pagesize='A4')

        #left box with grey color
        C.setFillColor('#424242')
        C.rect(0,0,200,800, fill=1)

        #left layout 
        C.setStrokeColor('white')
        C.setFillColor('white')
        C.line(25,570,200,570)
              

        #picture
        C.drawInlineImage(img,20,610,160,160,"True")
        
        #contact info
        C.setFont('Times-Roman',20)
        C.drawString(25,580,'Contact Info')
        C.setFont('Times-Roman',12)
        C.drawString(25,550,mobile.get())
        C.drawString(25,530,email.get())
        address=add.get(1.0, END)
        address=address[0:len(address)-1]
        style_add=ParagraphStyle('Mystyle',fontName='Times-Roman',fontSize=12,textColor='white')
        para=Paragraph(address,style_add)
        para.wrapOn(C,160,60)
        no_lines=len(address)//35+1
        if no_lines==1:
            a=510
        elif no_lines==2:
            a=500
        elif no_lines==3:
            a=490
        para.drawOn(C,25,a)
        
        #Technical skills
        C.setFont('Times-Roman',20)
        C.setFillColor('white')
        a=a-30
        C.drawString(25,a,'Technical skills')
        C.setFont('Times-Roman',12)
        a-=10
        C.line(25,a,200,a)
        a-=20
        skills=tskills.get(1.0,END)
        skills=skills[0:len(skills)-1]
        skills=skills.split(',')
        for i in range(len(skills)):
            C.drawString(25,a,skills[i])
            a=a-20

        #strengths
        C.setFont('Times-Roman',20)
        C.setFillColor('white')
        a=a-20
        C.drawString(25,a,'Strengths')
        C.setFont('Times-Roman',12)
        a-=10
        C.line(25,a,200,a)
        a-=20
        stren=strength.get(1.0,END)
        stren=stren[0:len(stren)-1]
        stren=stren.split(',')
        for i in range(len(stren)):
            C.drawString(25,a,stren[i])
            a=a-20

        #Right layout
        C.setStrokeColor('black')
        C.line(220,570,700,570)
        C.circle(220,560,3)
        C.circle(220,500,3)
        C.circle(220,440,3)
        C.line(220,557,220,503)
        C.line(220,497,220,443)
        C.line(220,437,220,370)
        C.line(220,320,700,320)
        
        #Canidte name and job
        C.setFont('Times-Roman',25)
        C.setFillColor('black')
        C.drawString(220,750,cname.get())
        C.setFont('Times-Roman',18)
        C.drawString(220,720,job.get())
        
        #objective
        C.setFillColor('black')
        C.setFont('Times-Roman',12)
        objc=obj.get(1.0, END)
        objc=objc[0:len(objc)-1]
        style_obj=ParagraphStyle('Mystyle1',fontName='Times-Roman',fontSize=14,textColor='black')
        para_o=Paragraph(objc)
        para_o.wrapOn(C,350,500)
        obj_lines=len(objc)//75+1
        b=700-10*obj_lines
        para_o.drawOn(C,220,b)

        

        #Education
        C.setFont('Times-Roman',20)
        C.drawString(220,580,'Education')
        C.setFont('Times-Roman',12)
        C.drawString(230,555,hedu_p.get())
        hedu=hedu_b.get()+", "+hedu_per.get()
        C.drawString(230,535,hedu)
        C.drawString(230,515,hedu_ins.get())
        C.drawString(230,495,inter_p.get())
        inter=inter_b.get()+", "+inter_per.get()
        C.drawString(230,475,inter)
        C.drawString(230,455,inter_ins.get())
        C.drawString(230,435,ssc_p.get())
        ssc=ssc_b.get()+", "+ssc_per.get()
        C.drawString(230,415,ssc)
        C.drawString(230,395,ssc_ins.get())


        #Work Experience
        C.setFont('Times-Roman',20)
        C.drawString(220,330,'Work Experience')
        C.setFont('Times-Roman',12)
        C.drawString(230,300,t_line.get())
        C.drawString(230,280,com.get())
        C.drawString(230,260,J_pos.get())
        C.drawString(230,240,J_des.get())
        if b==2:
            C.drawString(230,200,t_line1.get())
            C.drawString(230,180,com1.get())
            C.drawString(230,160,J_pos1.get())
            C.drawString(230,140,J_des1.get())        
        
        C.showPage()
        C.save()
        filename.close()

    #submit functionality
    def submit():
        if (cname.get()!='' and mobile.get()!='' and email.get()!=0 and add.get(1.0, END)!='' and  obj.get(1.0, END)!='' and job.get()!='' and
           hedu_p.get()!='' and hedu_b.get()!='' and hedu_per.get()!='' and hedu_ins.get() and inter_p.get()!='' and inter_b.get()!='' and inter_per.get()!='' and
            inter_ins.get()!='' and ssc_p.get()!='' and ssc_b.get()!='' and ssc_per.get()!='' and ssc_ins.get()!='' and t_line.get()!='' and com.get()!='' and
            J_pos.get()!='' and J_des.get()!='' and strength.get(1.0,END)!='' and tskills.get(1.0,END)!=''):
              
             if len(mobile.get())==10:
                 try:
                    int(mobile.get())
                    if email.get()[-1:-11:-1]=='moc.liamg@':
                        Label(root,text=" "*70,font=("Times new Roman",18),bg="#ffdab9").grid(row=57,column=0,sticky='w')
                        if len(add.get(1.0, END))-1<105:
                            if len(obj.get(1.0, END))-1<1400:
                                try:
                                    img.size
                                    out=confirm(text='Are you sure to submit your application?', title='Submission confirmation', buttons=['OK', 'Cancel'])
                                    if out=='OK':            
                                        ok()
                                        master.destroy()
                                except NameError:
                                    Label(root,text="please upload photo",font=("Times new Roman",18),bg="#ffdab9",fg="red").grid(row=57,column=11,sticky='w')
                            else:
                                Label(root,text="Objective must not exceed 700 letters       ",font=("Times new Roman",18),bg="#ffdab9",fg="red").grid(row=57,column=0,sticky='w') 
                        else:
                           Label(root,text="Address must not exceed 105 letters       ",font=("Times new Roman",18),bg="#ffdab9",fg="red").grid(row=57,column=0,sticky='w') 
                    else:
                      Label(root,text="Please enter your E-mail ID correctly              ",font=("Times new Roman",18),bg="#ffdab9",fg="red").grid(row=57,column=0,sticky='w')
                 except:
                   Label(root,text="Please enter your Mobile number correctly",font=("Times new Roman",18),bg="#ffdab9",fg="red").grid(row=57,column=0,sticky='w')
                
                
             else:
                Label(root,text="Please enter your Mobile number correctly",font=("Times new Roman",18),bg="#ffdab9",fg="red").grid(row=57,column=0,sticky='w')
                    
        else:
            Label(root,text="All fields are mandatory please fill them",font=("Times new Roman",18),bg="#ffdab9",fg="red").grid(row=57,column=0,sticky='w')
    #submit button

    Button(root,text="Submit",font=font1,command=submit).grid(row=58,column=6)

    #Reset functionality

    def Reset():
        out=confirm(text='Are you sure to reset your application?', title='Submission confirmation', buttons=['Yes', 'No'])
        if out=='Yes':
            master.destroy()
            new()

    #Reset button

    Button(root,text="Reset",font=font1,command=Reset).grid(row=58,column=0)

    
    Label(root,text="  ",font=("Times new Roman",25),bg="#ffdab9").grid(row=59,column=0,sticky='w')
    master.mainloop()

new()