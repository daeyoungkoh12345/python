import pygame as p
p.init()#초기화
w=(255,255,255)#red,green,blue
size=(800,400)#가로 세로 화면 비율
sc=p.display.set_mode(size)
p.display.set_caption("게임판")
playing=True

while playing:
    for event in p.event.get():#사용자가 무엇을 눌렀는지
        if event.type==p.QUIT:#게임창 x버튼 누르면
            playing=False #계속 반복 종료
            p.quit()
            quit()

    sc.fill(w)
    p.display.flip()#화면 업데이트
