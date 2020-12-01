import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름


#FPS
clock = pygame.time.Clock()
# 배경 이미지 불러오기
background = pygame.image.load("/Users/junwoo/Desktop/pythonworkspace/background.png")

# 이동할 좌표
to_x = 0
to_y = 0

# 캐릭터 불러오기 
character = pygame.image.load("/Users/junwoo/Desktop/pythonworkspace/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] #가로
character_height = character_size[1] # 세로
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동속도
character_speed = 0.6

# 
# 적 enenmy 캐릭터
enenmy = pygame.image.load("/Users/junwoo/Desktop/pythonworkspace/character.png")
enenmy_size = enenmyzzzz
enenmy_width = character_size[0] #가로
enenmy_height = character_size[1] # 세로
enenmy_x_pos = (screen_width / 2) - (character_width / 2)
enenmy_y_pos = screen_height - character_height
# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60)
    print("fps : " +str(clock.get_fps()))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #screen.fill((0,0,255))
    screen.blit(background,(0,0))

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

# pygame 종료
pygame.quit()