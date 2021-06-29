# !/bin/python3.8
# powered by masih ghorbani under GPL License
# gmail : masihgh8@gmail.com
# github : https://github.com/masih-dev/pygexer

from re import *
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as s
from tkinter import messagebox as m

win = Tk()
win.tk.call('tk', 'scaling', '0.95')
win.title("pygexer")
win.configure(bg="white")
win.geometry("850x600")
win.resizable(0, 0)

# Definition of three functions to change the appearance of the program.
def green_mode():
	win.configure(background="white")
	MainMenu.configure(bg="steelblue",fg="white",bd=3)
	EnTextLabel1.configure(bg="mediumaquamarine")
	EnReLabel.configure(bg="mediumaquamarine")
	MatchLabel.configure(bg="steelblue")
	GroupsLabel.configure(bg="steelblue")
	EnReLabel2.configure(bg="mediumaquamarine")
	EnTextLabel2.configure(bg="mediumaquamarine")
	ReplacementLabel.configure(bg="mediumaquamarine")
	RePhoneLabel.configure(bg="mediumaquamarine")
	ReYoutubeLabel.configure(bg="mediumaquamarine")
	ReEmailLabel.configure(bg="mediumaquamarine")
	copyleft.configure(bg="mediumaquamarine")
	PygexerLabel.configure(bg="steelblue")

def blue_mode():
	win.configure(background="white")
	EnTextLabel1.configure(bg="steelblue")
	EnReLabel.configure(bg="steelblue")
	MatchLabel.configure(bg="slategrey")
	GroupsLabel.configure(bg="slategrey")
	EnReLabel2.configure(bg="steelblue")
	EnTextLabel2.configure(bg="steelblue")
	ReplacementLabel.configure(bg="steelblue")
	RePhoneLabel.configure(bg="steelblue")
	ReYoutubeLabel.configure(bg="steelblue")
	ReEmailLabel.configure(bg="steelblue")
	copyleft.configure(bg="steelblue")

def black_mode():
	win.configure(background="black")
	MainMenu.configure(bg="black",fg="white",bd=5)
	EnTextLabel1.configure(bg="black")
	EnReLabel.configure(bg="black")
	MatchLabel.configure(bg="slategrey")
	GroupsLabel.configure(bg="slategrey")
	EnReLabel2.configure(bg="black")
	EnTextLabel2.configure(bg="black")
	ReplacementLabel.configure(bg="black")
	RePhoneLabel.configure(bg="black")
	ReYoutubeLabel.configure(bg="black")
	ReEmailLabel.configure(bg="black")
	PygexerLabel.configure(bg="black")
	copyleft.configure(bg="slategrey")

# This function executes the input regex on the input text and shows the result to the user.
def RunRegex():
	MainRegex = regex1.get()
	MainText = InputText1.get("1.0",END)
	if search(MainRegex,MainText) != None:
		result = search(MainRegex,MainText)
	else:
		result = "Error".split()
	matchs.insert(INSERT,f"Full Matchs: {result[0]} \n")
	try:
		groups.insert(INSERT,result.groups())
	except:
		groups.insert(INSERT,"None \n")

# This function deletes all available information in the input and output fields.
def ClearScreen1():
	InputRegex1.delete(0, 'end')
	InputText1.delete('1.0','end')
	matchs.delete('1.0','end')
	groups.delete('1.0','end')

# This function can run the input regex on the text and replace the desired result with the desired user's desired value.
def RunReplace():
	MainReplaceRegex = regex2.get()
	MainReplaceText = InputText2.get('1.0',END)
	if search(MainReplaceRegex,MainReplaceText) != None:
		MainReplacement = InputReplacement.get('1.0',END)
		MainResult = sub(MainReplaceRegex,MainReplacement,MainReplaceText)
		ReplaceResult.insert(INSERT,str(MainResult).strip())
	else:
		ReplaceResult.insert(INSERT,"PLEASE CHECK THE REGEX OR TEXT \n")

# This function deletes all available information in the input and output fields.	
def ClearScreen2():
	InputRegex2.delete(0,'end')
	InputText2.delete('1.0','end')
	InputReplacement.delete('1.0','end')
	ReplaceResult.delete('1.0','end')

# These three function display my accounts in social media to the user.
def ShowInstagramID():
	m.showinfo("My instagram","https://instagram.com/masih.gh23")
def ShowGithubAddress():
	m.showinfo("My Git Hub","https://github.com/masih-dev")
def ShowGmailAddress():
	m.showinfo("My Gmail","masihgh8@gmail.com")

# making a menu ...  
MainMenu = Menu(win,bd=10)
win.config(menu=MainMenu)

# Making the theme option in the menu so that the user can easily change the appearance of the program.
themes = Menu(MainMenu)
MainMenu.add_cascade(label="Themes",menu=themes)
themes.add_command(label="Green Mode",command=green_mode)
themes.add_command(label="Blue Mode",command=blue_mode)
themes.add_command(label="Black Mode",command=black_mode)

# create tab for different part of program 
MainTab = ttk.Notebook(win)

# in the home tab ,  user can process input regex on the input text.
HomeTab = ttk.Frame(MainTab)
MainTab.add(HomeTab,text="Home")

 # in the replace tab , The user has an environment that can replace the search result on the input text with the desired value. 
ReplaceTab = ttk.Frame(MainTab)
MainTab.add(ReplaceTab,text="Replace")

# in the example tab , useful examples is available to the user who can use them to learn or other things.
ExampleTab = ttk.Frame(MainTab)
MainTab.add(ExampleTab,text="Example")

# In this chapter, the developer information is available
AboutTab = ttk.Frame(MainTab)
MainTab.add(AboutTab,text="About")
MainTab.grid(ipadx="6px")

# Get input regex from user  in the home tab
EnReLabel = Label(HomeTab,text="Enter Regex",bg="steelblue",fg="white")
EnReLabel.grid(ipadx=390,ipady=10,pady="1px")
regex1 = StringVar()
InputRegex1 = Entry(HomeTab,textvariable=regex1,width=120)
InputRegex1.grid(ipady=10)

# Get a input text from user in the home tab.
EnTextLabel1 = Label(HomeTab,text="Enter Text",bg="steelblue",fg="white")
EnTextLabel1.grid(ipadx=395,ipady=10,pady="10px")
InputText1 = s.ScrolledText(HomeTab,width=104,height=5)
InputText1.grid(ipadx="40px")

# This button call the RunRegex function
RunRegexButton = ttk.Button(HomeTab,text="run ",command=RunRegex)
RunRegexButton.grid(ipadx=391)

# This button call the ClearScreen function
ClearScreenButton1 = ttk.Button(HomeTab,text="Clear",command=ClearScreen1)
ClearScreenButton1.grid(ipadx=391)

# This section presents the results of regex processing on the text
MatchLabel = Label(HomeTab,text="Matchs",bg="slategrey",fg="white")
MatchLabel.grid(ipadx=405,ipady=10,pady="5px")
matchs = s.ScrolledText(HomeTab,width=120,height=5)
matchs.grid()

# If you have been using groups in your input regex, the corresponding result is shown in this section.
GroupsLabel = Label(HomeTab,text="Groups",bg="slategrey",fg="white")
GroupsLabel.grid(ipadx=405,ipady=10,pady=5)
groups = s.ScrolledText(HomeTab,width=120,height=5)
groups.grid()

# Get a input regex from user in the replace tab
EnReLabel2 = Label(ReplaceTab,text="Enter Regex",bg="steelblue",fg="white")
EnReLabel2.grid(ipadx=390,ipady=10,pady="4px")
regex2 = StringVar()
InputRegex2 = Entry(ReplaceTab,width=120,textvariable=regex2)
InputRegex2.grid(ipady=10)

# Get a input text from user in the replace tab
EnTextLabel2 = Label(ReplaceTab,text="Enter Text",bg="steelblue",fg="white")
EnTextLabel2.grid(ipadx=395,ipady=10,pady="4px")
InputText2 = s.ScrolledText(ReplaceTab,width=104,height=5)
InputText2.grid(ipadx="40px")

# Get a input replacement from user in the replace tab
ReplacementLabel = Label(ReplaceTab,text="Replacement",bg="steelblue",fg="white")
ReplacementLabel.grid(ipadx=390,ipady=10,pady="4px")
InputReplacement = s.ScrolledText(ReplaceTab,width=104,height=5)
InputReplacement.grid(ipadx="40px")

# This button call the RunReplace function
RunReplaceButton = ttk.Button(ReplaceTab,text="Replace",command=RunReplace)
RunReplaceButton.grid(ipadx=391)

# This button call the ClearScreen function
ClearScreenButton2 = ttk.Button(ReplaceTab,text="Clear",command=ClearScreen2)
ClearScreenButton2.grid(ipadx=391,pady="4px")

# Show the result of substitution
ResultLabel2 = Label(ReplaceTab,text="Result",bg="slategrey",fg="white")
ResultLabel2.grid(ipadx=406,ipady=10,pady="4px")
ReplaceResult = s.ScrolledText(ReplaceTab,width=104,height=5)
ReplaceResult.grid(ipadx="40px")

# show a regex sample for the validation of Iranian telephone numbers in the example tab
RePhoneLabel = Label(ExampleTab,text="Check Phone Number",bg="steelblue",fg="white")
RePhoneLabel.grid(ipadx=405,ipady=10,pady="4px")
RegexForCheckPhoneNu= s.ScrolledText(ExampleTab,width=115,height=4,fg="white",bg="slategrey")
RegexForCheckPhoneNu.insert(INSERT,"^(\+98|0)?9\d{9}$")
RegexForCheckPhoneNu.grid(ipadx="40px")

# show RFC5322 regex To validate the email address , in the example tab
ReEmailLabel = Label(ExampleTab,text="RFC5322 For check email",bg="steelblue",fg="white")
ReEmailLabel.grid(ipady=10,ipadx=395,pady="4px")
RegexForCheckEmail = s.ScrolledText(ExampleTab,width=115,height=4,bg="slategrey",fg="white")
RegexForCheckEmail.insert(INSERT,"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
RegexForCheckEmail.grid(ipadx="40px")

# show  A regex to validate video link from the youtube.com , in the example tab
ReYoutubeLabel = Label(ExampleTab,text="Get video link from Youtube",bg="steelblue",fg="white")
ReYoutubeLabel.grid(ipady=10,ipadx=395,pady="4px")
RegexForYoutubeLink = s.ScrolledText(ExampleTab,width=115,height=5,bg="slategrey",fg="white")
RegexForYoutubeLink.insert(INSERT,"""https?:\/\/(?:[0-9A-Z-]+\.)?(?:youtu\.be\/|youtube(?:-nocookie)?\.com\S*[^\w\s-])([\w-]{11})(?=[^\w-]|$)(?![?=&+%\w.-]*(?:['"][^<>]*>|<\/a>))[?=&+%\w.-]* ^^ """)
RegexForYoutubeLink.grid(ipadx="40px")

PygexerLabel = Label(AboutTab,text="Pygexer",bg="steelblue",fg="white",font="tahoma 8 bold")
PygexerLabel.grid(ipady=10,ipadx=405)

instagram = ttk.Button(AboutTab,text="Instagram",command=ShowInstagramID)
instagram.grid(ipadx=391,ipady=10,pady="3px")

github = ttk.Button(AboutTab,text="GitHub",command=ShowGithubAddress)
github.grid(ipadx=391,ipady=10, pady=1)

gmail = ttk.Button(AboutTab,text="Gmail",command=ShowGmailAddress)
gmail.grid(ipadx=391,ipady=10, pady=10)

copyleft = Label(AboutTab,text="Powered By Masih Ghorbani",
bg="steelblue",fg="white",font="tahoma 7 bold")
copyleft.grid(ipadx=360,ipady=10,pady=310)

win.mainloop()
