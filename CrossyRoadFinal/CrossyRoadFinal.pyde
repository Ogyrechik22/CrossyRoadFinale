def col(x,y,w,h,x2,y2,w2,h2):
   if (x + w >= x2) and (x <= x2 + w2) and (y + h >= y2) and (y <= y2 + h2):
       return True
   else:
       return False
x = 475
y = 750
rand = 0
fir = -150
sec = -150
thir = -150
four = -150
five = -150
visota = 400
rand2 = 0
rand3 = 0
vod1 = -200
vod2 = -200
fir2 = 0
sec2 = 0
thir2 = 0
four2 = 0
five2 = 0
fir3 = 0
sec3 = 0
thir3 = 0
four3 = 0
five3 = 0
new1 = 0
new2 = 0
new3 = 0
new4 = 0
new5 = 0
new6 = 0
new7 = 0
new8 = 0
new9 = 0
new10 = 0
new11 = 0
rod = 1
red1 = 0 
def setup():
    size(1000,1000)
    textMode(CENTER)
def draw():
    global x,y,rand,fir,sec,thir,four,five,visota,rand2,rand3,vod1,vod2,fir2,sec2,thir2,four2,five2,fir3,sec3,thir3,four3,five3,new1,new2,new3,new4,new5,new6,new7,new8,new9,new10,new11,rod,red1
    background(0,255,78)
    fill(1)
    rect(0,visota,1000,70)
    fill(255)
    rect(fir,visota,150,70)
    if col(fir,visota + 1,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 250,1000,70)
    fill(255)
    rect(sec,visota - 250,150,70)
    if col(sec,visota - 249,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 500,1000,70)
    fill(255)
    rect(thir,visota - 500,150,70)
    if col(thir,visota - 499,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 750,1000,70)
    fill(255)
    rect(four,visota - 750,150,70)
    if col(four,visota - 749,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 1000,1000,70)
    fill(255)
    rect(five,visota - 1000,150,70)
    if col(five,visota - 999,150,70,x,y,50,50):
        noLoop()
    fill(0,244,255)
    rect(0,visota - 1300,1000,200,100)
    if col(0,visota - 1290,1000,170,x,y,50,50):
        rod = 0
    fill(95,54,0)
    rect(vod1,visota - 1200,200,100)
    if col(vod1 - 10,visota - 1195,200,85,x,y,50,50):
        loop()
        x += 15
        rod = 1
    vod1 += 5
    rect(vod2,visota - 1300,200,100)
    if col(vod2 - 10,visota - 1295,90,85,x,y,50,50):
        loop()
        x += 21
        rod = 1
    vod2 += 7
    fill(1)
    rect(0,visota - 1800,1000,70)
    fill(255)
    rect(sec,visota - 1800,150,70)
    if col(sec,visota - 1799,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 2050,1000,70)
    fill(255)
    rect(thir,visota - 2050,150,70)
    if col(thir,visota - 2049,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 2400,1000,70)
    fill(255)
    rect(four,visota - 2400,150,70)
    if col(four,visota - 2399,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 2650,1000,70)
    fill(255)
    rect(five,visota - 2650,150,70)
    if col(five,visota - 2649,150,70,x,y,50,50):
        noLoop()
    fill(0,244,255)
    rect(0,visota - 2950,1000,200,100)
    fill(95,54,0)
    rect(vod1,visota - 2850,200,100)
    fill(1)
    rect(0,visota - 1550,1000,70)
    fill(255)
    rect(fir2,visota - 1550,250,70)
    if col(fir2,visota - 1549,250,70,x,y,50,50):
        noLoop()
    fill(255)
    rect(sec2,visota - 1800,150,70)
    if col(sec2,visota - 1799,150,70,x,y,50,50):
        noLoop()
    rect(thir2,visota - 2050,150,70)
    if col(thir2,visota - 2049,150,70,x,y,50,50):
        noLoop()
    rect(four2,visota - 2400,250,70)
    if col(four2,visota - 2399,250,70,x,y,50,50):
        noLoop()
    rect(five2,visota - 2650,300,70)
    if col(five2,visota - 2649,300,70,x,y,50,50):
        noLoop()
    fill(0,244,255)
    rect(0,visota - 2950,1000,200,100)
    if col(0,visota - 2940,1000,180,x,y,50,50):
        rod = 0
    fill(95,54,0)
    rect(vod1,visota - 2850,200,100)
    if col(vod1 + 10,visota - 2845,200,85,x,y,50,50):
        loop()
        x += 15
        rod = 1
    vod1 += 5
    rect(vod2,visota - 2950,200,100)
    if col(vod2 + 10,visota - 2945,200,85,x,y,50,50):
        loop()
        x += 21
        rod = 1
    vod2 += 7
    fill(1)
    rect(0,visota - 3150,1000,70)
    fill(255)
    rect(sec,visota - 3150,150,70)
    if col(sec,visota - 3149,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 3400,1000,70)
    fill(255)
    rect(thir,visota - 3400,150,70)
    if col(thir,visota - 3399,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 3650,1000,70)
    fill(255)
    rect(four,visota - 3650,150,70)
    if col(four,visota - 3649,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 3900,1000,70)
    fill(255)
    rect(five,visota - 3900,150,70)
    if col(five,visota - 3899,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 4150,1000,70)
    fill(255)
    rect(fir2,visota - 4150,250,70)
    if col(fir2,visota - 4149,250,70,x,y,50,50):
        noLoop()
    rect(sec2,visota - 3150,150,70)
    if col(sec2,visota - 3149,150,70,x,y,50,50):
        noLoop()
    rect(thir2,visota - 3400,150,70)
    if col(thir2,visota - 3399,150,70,x,y,50,50):
        noLoop()
    rect(four2,visota - 3650,250,70)
    if col(four2,visota - 3649,250,70,x,y,50,50):
        noLoop()
    rect(five2,visota - 3900,300,70)
    if col(five2,visota - 3899,300,70,x,y,50,50):
        noLoop()
    rect(fir3,visota - 4150,300,70)
    if col(fir3,visota - 4149,300,70,x,y,50,50):
        noLoop()
    rect(sec3,visota - 3150,200,70)
    if col(sec3,visota - 3149,200,70,x,y,50,50):
        noLoop()
    rect(thir3,visota - 3400,250,70)
    if col(thir3,visota - 3399,250,70,x,y,50,50):
        noLoop()
    rect(four3,visota - 3650,250,70)
    if col(four3,visota - 3649,250,70,x,y,50,50):
        noLoop()
    rect(five3,visota - 3900,300,70)
    if col(five3,visota - 3899,300,70,x,y,50,50):
        noLoop()
    fill(0,244,255)
    rect(0,visota - 4550,1000,200,100)
    if col(0,visota - 4540,1000,180,x,y,50,50):
        rod = 0
    fill(95,54,0)
    rect(vod1 + 10,visota - 4450,200,100)
    if col(vod1 + 10,visota - 4449,200,85,x,y,50,50):
        loop()
        x += 15
        rod = 1
    vod1 += 5
    rect(vod2,visota - 4550,200,100)
    if col(vod2 + 10,visota - 4549,200,85,x,y,50,50):
        loop()
        x += 21
        rod = 1
    vod2 += 7
    fill(1)
    rect(0,visota - 4850,1000,140)
    fill(255)
    rect(new1,visota - 4780,250,70)
    if col(new1,visota - 4779,250,70,x,y,50,50):
        noLoop()
    rect(new2,visota - 4850,150,70)
    if col(new2,visota - 4849,150,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 5100,1000,140)
    fill(255)
    rect(new3,visota - 5030,150,70)
    if col(new3,visota - 5029,150,70,x,y,50,50):
        noLoop()
    rect(new4,visota - 5100,200,70)
    if col(new4,visota - 5099,250,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 5430,1000,210)
    fill(255)
    rect(new5,visota - 5290,200,70)
    if col(new5,visota - 5289,200,70,x,y,50,50):
        noLoop()
    rect(new6,visota - 5360,200,70)
    if col(new6,visota - 5359,200,70,x,y,50,50):
        noLoop()
    rect(new7,visota - 5430,200,70)
    if col(new7,visota - 5429,200,70,x,y,50,50):
        noLoop()
    fill(1)
    rect(0,visota - 5850,1000,280)
    fill(255)
    rect(new8,visota - 5640,200,70)
    if col(new8,visota - 5639,200,70,x,y,50,50):
        noLoop()
    rect(new9,visota - 5710,200,70)
    if col(new9,visota - 5709,200,70,x,y,50,50):
        noLoop()
    rect(new10,visota - 5780,200,70)
    if col(new10,visota - 5779,200,70,x,y,50,50):
        noLoop()
    rect(new11,visota - 5850,200,70)
    if col(new11,visota - 5849,200,70,x,y,50,50):
        noLoop()
    if col(-300,red1 + 1000,1800,10000,x,y,50,50):
        background(1)
        fill(255,0,0)
        textSize(55)
        text('You Lose!',390,500)
        noLoop()
    fill(1)
    textSize(30)
    rect(0,visota - 6000,1000,100)
    fill(255,0,0)
    text('Finish',450,visota - 5945)
    if col(0,visota - 6000,1000,100,x,y,50,50):
        textSize(55)
        background(1)
        fill(255,0,0)
        text('You Win!',390,500)
        noLoop()
    fill(255)
    rect(-300,red1 + 1000,1800,10000)
    red1 -= 1.4
    fill(255)
    rect(x,y,50,50)
    rand = random(26,28)
    rand = round(rand)
    rand2 = random(5,16)
    rand3 = random(16,35)
    fir += 5
    if rand == 27:
        sec += 8
    if rand == 27:
        thir += rand2
    if rand == 26:
        four += rand3
    five += rand2
    if fir > 1200:
        fir = -150
    if sec > 1200:
        sec = -150
    if thir > 1200:
        thir = -150
    if four > 1200:
        four = -150
    if five > 1200:
        five = -150
    if vod1 > 1200:
        vod1 = -200
    if vod2 > 1200:
        vod2 = -200
    if x > 1050:
        x = -200
    if fir2 > 1300:
        fir2 = -300
    if sec2 > 1200:
        sec2 = -200
    if thir2 > 1200:
        thir2 = -200
    if four2 > 1300:
        four2 = -300
    if five2 > 1350:
        five2 = -350
    if fir3 > 1300:
        fir3 = -300
    if sec3 > 1300:
        sec3 = -300
    if thir3 > 1300:
        thir3 = -300
    if four3 > 1300:
        four3 = -300
    if five3 > 1350:
        five3 = -350
    if new1 > 1300:
        new1 = -300
    if new2 < -200:
        new2 = 1200
    if new3 > 1300:
        new3 = -300
    if new4 < -200:
        new4 = 1200
    if new5 > 1300:
        new5 = -300
    if new6 < -200:
        new6 = 1200
    if new7 > 1350:
        new7 = -350
    if new8 > 1300:
        new8 = -200
    if new9 < -200:
        new9 = 1200
    if new10 > 1300:
        new10 = -200
    if new11 < -200:
        new11 = 1200

    fir2 += 15
    sec2 += 15
    thir2 += 7
    four2 += 5
    five2 += 20
    fir3 += 25
    sec3 += 20
    thir3 += 17
    four3 += 14
    five3 += 30
    new1 += 13
    new2 -= 20
    new3 += random(25,30)
    new4 -= 23
    new5 += 27
    new6 -= 16
    new7 += random(20,35)
    new8 += 17
    new9 -= 9
    new10 += random(10,19)
    new11 -= 15
    if rod == 0:
        noLoop()
def keyTyped():
    global x,y,rand,fir,sec,thie,four,five,visota,red1
    if key == 'w' or key == 'W':
        visota += 50
        red1 += 50
    if key == 'a' or key == 'A':
        x -= 50
    if key == 'd' or key == 'D':
        x += 50
