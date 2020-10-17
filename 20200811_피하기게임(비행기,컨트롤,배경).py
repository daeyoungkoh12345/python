import pygame as p
p.init()#초기화
w=(255,255,255)#red,green,blue
size=(900,400)#가로 세로 화면 비율
sc=p.display.set_mode(size)
p.display.set_caption("게임판")
playing=True

plane=p.image.load("1.png")
bg=p.image.load("2.jpg")
bg_x=0
bg_y=0
bg1=bg.copy()
bg1_x=900
bg1_y=0


while playing:
    for event in p.event.get():#사용자가 무엇을 눌렀는지
        if event.type==p.QUIT:#게임창 x버튼 누르면
            playing=False #계속 반복 종료
            p.quit()
            quit()


    sc.blit(bg,(bg_x,bg_y))
    sc.blit(bg1,(bg1_x,bg1_y))
    bg_x-=0.5
    bg1_x-=0.5
    if bg_x <= -900:
        bg_x=900
    if bg1_x <= -900:
        bg1_x=900
    
    sc.blit(plane,(000,150))
    p.display.flip()#화면 업데이트
    
