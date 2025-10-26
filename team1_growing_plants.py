from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.title("식물 키우기")
window.config(padx=10, pady=10, bg="lightgreen")
window.resizable(width=FALSE, height= FALSE)
canvas = Canvas(window, height=600, width=850, bg="ivory")
canvas.pack()

# 주의사항 안내
warn = Label(window,text="주의사항: 물과 햇빛 쬐는 것에 모두 이상이 있을 경우 하나만 표시됩니다.",font=("맑은고딕", 15, "bold"), bg="lightgreen")
warn.pack()

# 변수 기본 값
day = 1

plant_lv = 0
plant_h = 1

Sun = 5
Water = 5
P = 5
Zn = 5
Cu = 5
Mn = 5
Bug = 0
mday = 3

#이미지 추가
img_pot = PhotoImage(file="image/pot.png")
img_lv1 = PhotoImage(file="image/lv1.png")
img_lv2 = PhotoImage(file="image/lv2.png")
img_lv3 = PhotoImage(file="image/lv3.png")
img_lv4 = PhotoImage(file="image/lv4.png")
img_Death = PhotoImage(file="image/Death.png")
img_air = PhotoImage(file="image/air.png")

img_Hl = PhotoImage(file="image/Hl.png")
img_Sunp = PhotoImage(file="image/Sun+.png")
img_Sunm = PhotoImage(file="image/Sun-.png")
img_Wp = PhotoImage(file="image/W+.png")
img_Wm = PhotoImage(file="image/W-.png")

img_Hr = PhotoImage(file="image/Hr.png")
img_Bug = PhotoImage(file="image/Bug.png")
img_P = PhotoImage(file="image/P.png")
img_Zn = PhotoImage(file="image/Zn.png")
img_Cu = PhotoImage(file="image/Cu.png")
img_Mn = PhotoImage(file="image/Mn.png")

img_gSun = PhotoImage(file="image/sun.png")
img_gWater = PhotoImage(file="image/water.png")
img_gP = PhotoImage(file="image/gP.png")
img_gZn = PhotoImage(file="image/gZn.png")
img_gCu = PhotoImage(file="image/gCu.png")
img_gMn = PhotoImage(file="image/gMn.png")
img_gBug = PhotoImage(file="image/gBug.png")
img_gegg = PhotoImage(file="image/egg.png")
img_gvng = PhotoImage(file="image/vng.png")

#첫 화면 띄우기
canvas_img = canvas.create_image(425, 300, image=img_pot)
plant_img = canvas.create_image(425, 300, image=img_air)
lleaf_img = canvas.create_image(425, 300, image=img_air)
rleaf_img = canvas.create_image(425, 300, image=img_air)
give_img = canvas.create_image(425, 300, image=img_air)

day_text = canvas.create_text(100, 40, text= f"DAY {day}", fill="brown", font=("맑은고딕", 35, "bold") )   # 날짜
canvas.itemconfig(day_text)

# 날짜 조정
level2 = random.choice([5,6,7,8,9])
level3 = random.choice([10,11,12,13])
level4 = random.choice([14,15,16])

# 버튼용 함수
def bad_end():
    messagebox.showinfo("배드 엔딩","식물이 그만 죽고 말았습니다.... 다시 도전해보세요.")

def happy_end():
    messagebox.showinfo("해피 엔딩","성공적으로 식물을 키워냈습니다!")

def game():
    global day, plant_lv, plant_h, Sun, Water, P, Zn, Cu, Mn, Bug, mday
    canvas.itemconfig(give_img, image = img_air)

    day += 1
    if day == 2:
        plant_lv = 1
    if day == level2:
        plant_lv = 2
    if day == level3:
        plant_lv = 3
    if day == level4:
        plant_lv = 4

    # 전 날의 결과
    Sun -= random.choice([1,2])
    Water -= random.choice([1,2])
    if P < 5 or Zn < 5 or Cu < 5 or Mn < 5:
        mday -= 1
    if Bug > 0:
        Bug += 1

    # 식물 상태 판단
    if Sun <= 0 or Sun >= 10 or Water <= 0 or Water >= 10:
        plant_h = 0
    if P > 6 or Zn > 6 or Cu > 6 or Mn > 6 or mday <= 0 or Bug > 4 or Bug < 0:
        plant_h = 0

    # 이벤트 발생
    if plant_h == 1 and P >= 5 and Zn >= 5 and Cu >= 5 and Mn >= 5 and Bug <= 0:
        mday = 3
        percent = random.randrange(1, 100)
        if 1 <= percent <= 10:
            P -= 1
        elif 11 <= percent <= 20:
            Zn -= 1
        elif 21 <= percent <= 37:
            Cu -= 1
        elif 38 <= percent <= 54:
            Mn -= 1
        elif 55 <= percent <= 70:
            Bug += 1

    # 화면 띄우기
    canvas.itemconfig(day_text, text="DAY {}".format(day))
    if plant_h == 1:
        # 몸체
        if plant_lv == 1:
            canvas.itemconfig(plant_img, image = img_lv1)
        elif plant_lv == 2:
            canvas.itemconfig(plant_img, image = img_lv2)
        elif plant_lv == 3:
            canvas.itemconfig(plant_img, image = img_lv3)
        elif plant_lv == 4:
            canvas.itemconfig(plant_img, image = img_lv4)
            b_happy_end = Button(window, text="    엔 딩    ", bg="white", fg="black", font=("맑은고딕", 30, "bold"), command = happy_end)
            b_happy_end.place(x=30, y=480)

        # 왼 잎
        if Sun <= 3:
            canvas.itemconfig(lleaf_img, image = img_Sunm)      # 햇빛 부족
        elif Sun >= 8:
            canvas.itemconfig(lleaf_img, image = img_Sunp)      # 햇빛 화상
        elif Water <= 3:
            canvas.itemconfig(lleaf_img, image = img_Wm)        # 수분 부족
        elif Water >= 8:
            canvas.itemconfig(lleaf_img, image = img_Wp)        # 과습
        else:
            canvas.itemconfig(lleaf_img, image = img_Hl)        # 건강한 잎

        # 오른 잎
        if P < 5:
            canvas.itemconfig(rleaf_img, image = img_P)         # 인 부족
        elif Zn < 5:
            canvas.itemconfig(rleaf_img, image = img_Zn)        # 아연 부족
        elif Cu < 5:
            canvas.itemconfig(rleaf_img, image = img_Cu)        # 구리 부족
        elif Mn < 5:
            canvas.itemconfig(rleaf_img, image = img_Mn)        # 망간 부족
        elif Bug > 0:
            canvas.itemconfig(rleaf_img, image = img_Bug)       # 해충 발생
        else:
            canvas.itemconfig(rleaf_img, image = img_Hr)        # 건강한 잎
        
    else:
        canvas.itemconfig(plant_img, image = img_Death)         # 식물 죽음
        canvas.itemconfig(lleaf_img, image = img_air)
        canvas.itemconfig(rleaf_img, image = img_air)
        b_bad_end = Button(window, text="    엔 딩    ", bg="white", fg="black", font=("맑은고딕", 30, "bold"), command = bad_end)
        b_bad_end.place(x=30, y=480)

def give_Sun():
    global Sun
    Sun += 1
    canvas.itemconfig(give_img, image=img_gSun)

def give_Water():
    global Water
    Water += 1
    canvas.itemconfig(give_img, image=img_gWater)

def give_P():
    global P
    P += 1
    canvas.itemconfig(give_img, image=img_gP)

def give_Zn():
    global Zn
    Zn += 1
    canvas.itemconfig(give_img, image=img_gZn)

def give_Cu():
    global Cu
    Cu += 1
    canvas.itemconfig(give_img, image=img_gCu)

def give_Mn():
    global Mn
    Mn += 1
    canvas.itemconfig(give_img, image=img_gMn)

def give_Bug():
    global Bug
    Bug -= 1
    canvas.itemconfig(give_img, image=img_gBug)

def give_vng():
    global plant_h
    plant_h = 0
    canvas.itemconfig(give_img, image=img_gvng)

def give_egg():
    canvas.itemconfig(give_img, image=img_gegg)

# 버튼 설정
b_day = Button(window, text="다음 날로", bg="white", fg="black", font=("맑은고딕", 30, "bold"), command = game)
b_day.place(x=30, y=480)
b_sun = Button(window, text="햇빛 쬐기", bg="white", fg="orange", font=("맑은고딕", 20, "bold"), command = give_Sun)
b_sun.place(x=30, y=90)
b_water = Button(window, text="물 주기", bg="white", fg="blue", font=("맑은고딕", 20, "bold"), command = give_Water)
b_water.place(x=30, y=160)
b_P = Button(window, text="인 영양제 주기", bg="white", fg="black", font=("맑은고딕", 20, "bold"), command = give_P)
b_P.place(x=647, y=15)
b_Zn = Button(window, text="아연 영양제 주기", bg="white", fg="black", font=("맑은고딕", 20, "bold"), command = give_Zn)
b_Zn.place(x=620, y=90)
b_Cu = Button(window, text="구리 영양제 주기", bg="white", fg="black", font=("맑은고딕", 20, "bold"), command = give_Cu)
b_Cu.place(x=620, y=165)
b_Mn = Button(window, text="망간 영양제 주기", bg="white", fg="black", font=("맑은고딕", 20, "bold"), command = give_Mn)
b_Mn.place(x=620, y=240)
b_bug = Button(window, text="해충 퇴치제 주기", bg="white", fg="black", font=("맑은고딕", 20, "bold"), command = give_Bug)
b_bug.place(x=620, y=315)
b_egg = Button(window, text="부순 계란 껍질 두기", bg="white", fg="black", font=("맑은고딕", 20, "bold"), command = give_egg)
b_egg.place(x=586, y=390)
b_death = Button(window, text="식초 주기", bg="white", fg="black", font=("맑은고딕", 20, "bold"), command = give_vng)
b_death.place(x=710, y=465)

window.mainloop()