import random
import pgzrun
WIDTH=800
HEIGHT=600
TITLE="quiz game"

questions=[]
question=[]
timer=10
score=0
totalquestions=0
currentquestion=0
gameover=False

message_box=Rect(0,0,800,100)
question_box=Rect(20,120,540,150)
timer_box=Rect(590,120,150,150)
skip_button=Rect(590,280,150,260)
option_box1=Rect(20,280,265,130)
option_box2=Rect(295,280,265,130)
option_box3=Rect(20,420,265,130)
option_box4=Rect(295,420,265,130)

def draw():
    screen.fill("black")
    screen.draw.filled_rect(message_box,"red")
    screen.draw.filled_rect(question_box,"blue")
    screen.draw.filled_rect(option_box1,"orange")
    screen.draw.filled_rect(option_box2,"orange")
    screen.draw.filled_rect(option_box3,"orange")
    screen.draw.filled_rect(option_box4,"orange")
    screen.draw.filled_rect(timer_box,"blue")
    screen.draw.filled_rect(skip_button,"green")

    screen.draw.textbox("welcome to quiz game",message_box,color="black")
    screen.draw.textbox("question",question_box,color="black")
    screen.draw.textbox("answer",option_box1,color="black")
    screen.draw.textbox("answer",option_box2,color="black")
    screen.draw.textbox("answer",option_box3,color="black")
    screen.draw.textbox("answer",option_box4,color="black")
    screen.draw.textbox("time",timer_box,color="black")
    screen.draw.textbox("skip",skip_button,color="black")
def update():
    pass
def readquestionfile():
    global questions
    global totalquestions
    file=open("questions.txt","r")
    questions=file.readlines()
    totalquestions=len(questions)
    file.close()
    question=questions[currentquestion].split(",")
    print(question)

readquestionfile()

pgzrun.go()