import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("/Users/junwoo/Desktop/pythonworkspace/background.png")

# 캐릭터 불러오기 
character = pygame.image.load("/Users/junwoo/Desktop/pythonworkspace/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] #가로
character_height = character_size[1] # 세로
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
    #screen.fill((0,0,255))
    screen.blit(background,(0,0))

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

# pygame 종료
pygame.quit()