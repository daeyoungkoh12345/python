import pygame as p
import random as r
p.init()#초기화
w=(255,255,255)#red,green,blue
size=(900,400)#가로 세로 화면 비율
sc=p.display.set_mode(size)
p.display.set_caption("게임판")
playing=True

plane=p.image.load("1.png")
p_rect=plane.get_rect(left=0,top=150)
p_y=0
bg=p.image.load("2.jpg")
bg_x=0
bg_y=0
bg1=bg.copy()
bg1_x=900
bg1_y=0
#적군
en=p.image.load("3.png")
e_rect=en.get_rect(left=850,top=100)
ep=p.image.load("4.png")
ep_rect=ep.get_rect(left=850,top=100)
eo=p.image.load("5.png")
eo_rect=eo.get_rect(left=850,top=100)
er=p.image.load("6.png")
er_rect=er.get_rect(left=850,top=100)

while playing:
    for event in p.event.get():#사용자가 무엇을 눌렀는지
        if event.type==p.QUIT:#게임창 x버튼 누르면
            playing=False #계속 반복 종료
            p.quit()
            quit()

        if event.type==p.KEYDOWN:#키보드를 눌렀을때
            if event.key==p.K_UP:
                p_y=-3
            if event.key==p.K_DOWN:
                p_y=3
        if event.type==p.KEYUP:#키보드를 눌렀을때
            if event.key==p.K_UP:
                p_y=0
            if event.key==p.K_DOWN:
                p_y=0

    p_rect.top+=p_y

    sc.blit(bg,(bg_x,bg_y))
    sc.blit(bg1,(bg1_x,bg1_y))
    bg_x-=0.5
    bg1_x-=0.5
    if bg_x <= -900:
        bg_x=900
    if bg1_x <= -900:
        bg1_x=900
    
    sc.blit(plane,p_rect)
    if p_rect.top<=0:
        p_rect.top=0        
    if p_rect.top>=340:
        p_rect.top=340
        
    sc.blit(en,e_rect)
    e_rect.left-=3
    if e_rect.left<=0:
          e_rect.left=850
          e_rect.top=r.randint(0,350)
          
    sc.blit(ep,ep_rect)
    ep_rect.left-=4
    if ep_rect.left<=0:
          ep_rect.left=850
          ep_rect.top=r.randint(0,350)

    sc.blit(eo,eo_rect)
    eo_rect.left-=5
    if eo_rect.left<=0:
          eo_rect.left=850
          eo_rect.top=r.randint(0,350)

    sc.blit(er,er_rect)
    er_rect.left-=2
    if er_rect.left<=0:
          er_rect.left=850
          er_rect.top=r.randint(0,350)
    if p_rect.colliderect(e_rect):
          playing=False
    if p_rect.colliderect(ep_rect):
          playing=False
    if p_rect.colliderect(eo_rect):
          playing=False
    if p_rect.colliderect(er_rect):
          playing=False
        
    p.display.flip()#화면 업데이트
    
