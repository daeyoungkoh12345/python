import pygame as p
p.init()#초기화
w=(255,255,255)#red,green,blue
size=(500,800)#가로 세로 화면 비율
sc=p.display.set_mode(size)
p.display.set_caption("슈팅게임")
playing=True
plane = p.image.load("떳다떳다 비행기.png")
p_rect=plane.get_rect(left=200,top=700)
p_x = 0
space = p.image.load("space2.jpg")
bullet=p.image.load("ㄱㅗㅏㅇ.png")
b_list=[]

while playing:
    for event in p.event.get():#사용자가 무엇을 눌렀는지
        if event.type==p.QUIT:#게임창 x버튼 누르면
            playing=False #계속 반복 종료
            p.quit()
            quit()
        if event.type == p.KEYDOWN:
            if event.key==p.K_LEFT:
                p_x=-2
            if event.key==p.K_RIGHT:
                p_x=2
            if event.key==p.K_SPACE:
                b_rect=bullet.get_rect(left=p_rect.left+42 , top=p_rect.top)
                b_list.append(b_rect)
        if event.type==p.KEYUP:#키보드를 눌렀을때
            if event.key==p.K_LEFT:
                p_x=0
            if event.key==p.K_RIGHT:
                p_x=0

    p_rect.left+=p_x
    sc.fill(w)
    sc.blit(space,(0,0))
    sc.blit(plane,p_rect)
    if p_rect.left<=0:
        p_rect.left=0
    if p_rect.left>=400:
        p_rect.left=400

    for b_rect in b_list:
        sc.blit(bullet,b_rect)
        b_rect.top-=10
        if b_rect.top<=0:
            b_list.remove(b_rect)
    p.display.flip()#화면 업데이트    
