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
options=[option_box1,option_box2,option_box3,option_box4]

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
    screen.draw.textbox(question[0],question_box,color="black")
    screen.draw.textbox(question[1],option_box1,color="black")
    screen.draw.textbox(question[2],option_box2,color="black")
    screen.draw.textbox(question[3],option_box3,color="black")
    screen.draw.textbox(question[4],option_box4,color="black")
    screen.draw.textbox(str(timer),timer_box,color="black")
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

def readnextquestion():
    global question
    question=questions[currentquestion].split(",")
    print(question)

readquestionfile()
readnextquestion()

def on_mouse_down(pos):
    global score
    optionnumber=1
    for option in options:
        if option.collidepoint(pos):
            if optionnumber==int(question[5]):
                correctanswer()
                score=score+1
            else:
                game_over()
        optionnumber=optionnumber+1
    if skip_button.collidepoint(pos):
        correctanswer()
        
def correctanswer():
    global timer, score, currentquestion
    currentquestion=currentquestion+1
    if currentquestion>=11:
        game_over()
    else:
        readnextquestion()
    timer=10
def game_over():
    global gameover
    global question
    gameover=True
    question=["game over. Your score is"+str(score),"-","-","-","-","5"]


def reducetime():
    global timer
    if timer>0:
        timer=timer-1
    else:
        game_over()
clock.schedule_interval(reducetime,1)





pgzrun.go()