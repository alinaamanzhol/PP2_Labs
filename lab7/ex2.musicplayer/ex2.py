import pygame
import os
import random
pygame.init()
W, H = 600, 600
RED = (255, 0, 0)

musics = [f"songs/{i}" for i in os.listdir(r'C:\\Users\\Алина\\OneDrive\\Desktop\\PP2\\lab7\\ex2.musicplayer\\songs') if '.mp3' in i]
images = [f"songs/{i}" for i in os.listdir(r'C:\\Users\\Алина\\OneDrive\\Desktop\\PP2\\lab7\\ex2.musicplayer\\songs') if '.jpg' in i]
authors = {}
for i in musics:
    authors[i[i.find('-')+1:-4]] = i[6:i.find('-')]
songs = {}
for i in musics:
    songs[i[i.find('-')+1:-4]] = i


def play_music():
    
    pygame.mixer.music.load(songs)
    


def start(current_photo_name_view, current_photo_name_search):
    global musics, images, authors, songs
    '''current_photo_path = images[0]
    current_photo_sc = pygame.image.load(current_photo_path)
    current_photo_sc = pygame.transform.scale(current_photo_sc, (300, 300))
    current_photo_rect = current_photo_sc.get_rect(center=(W//2, 200))
    sc.blit(current_photo_sc, current_photo_rect)

    current_photo_name = current_photo_path[6:-4]
    current_photo_name_view = current_photo_name.replace('-', ' ')
    current_photo_name_search = current_photo_name.replace('-', '_')'''

    name_font = pygame.font.Font('font_user.ttf', 24)
    name = name_font.render(current_photo_name_view, 1, RED)

    name_rect = name.get_rect(center=(W//2, 380))
    #sc.blit(name, name_rect)

    name_author_font = pygame.font.Font('font_user.ttf', 20)
    name_author = name_author_font.render(authors[current_photo_name_search], 1, RED)
    name_author_rect = name_author.get_rect(center=(W//2, 400))
    #sc.blit(name_author, name_author_rect)
    return (name, name_rect, name_author, name_author_rect)



def get_current_photo(images):
    current_photo_path = images[0]
    current_photo_sc = pygame.image.load(current_photo_path).convert()
    current_photo_sc = pygame.transform.scale(current_photo_sc, (300, 300))
    current_photo_rect = current_photo_sc.get_rect(center=(W//2, 200))
    current_photo_name = current_photo_path[6:-4]
    current_photo_name_view = current_photo_name.replace('-', ' ')
    current_photo_name_search = current_photo_name.replace('-', '_')
    return (current_photo_sc, current_photo_rect, current_photo_path, current_photo_name, current_photo_name_view, current_photo_name_search)



def next():
    global images
    images = images[1:] + [images[0]]

    pygame.mixer.music.load(songs[images[0][6:-4].replace('-', '_')])

def previous():
    global images
    images = [images[-1]] + images[:-1]
    pygame.mixer.music.load(songs[images[0][6:-4].replace('-', '_')])
    

def mute():
    pygame.mixer.music.set_volume(0)

def unmute():
    pygame.mixer.music.set_volume(1)

def dec_volume():
    current_volume = pygame.mixer.music.get_volume()
    
    pygame.mixer.music.set_volume(current_volume-0.1)
    if pygame.mixer.music.get_volume() < 0.1:
        pygame.mixer.music.set_volume(0.0)

def inc_volume():
    current_volume = pygame.mixer.music.get_volume()
    if current_volume == 1.0:
        pygame.mixer.music.set_volume(1.0)
    else:
        pygame.mixer.music.set_volume(current_volume+0.1)
#def 


sc = pygame.display.set_mode((W, H))
pygame.display.set_icon(pygame.image.load('icon.png'))
pygame.display.set_caption('My Player')
bg = pygame.image.load('bg.jpg')
sc.blit(bg, (0, 0))

clock = pygame.time.Clock()

pause_sc = pygame.image.load('buttons/pause.png').convert_alpha()
mute_sc = pygame.image.load('buttons/mute.png').convert_alpha()
play_sc = pygame.image.load('buttons/play.png').convert_alpha()
skip_sc = pygame.image.load('buttons/skip.png').convert_alpha()
previous_sc = pygame.image.load('buttons/previous.png').convert_alpha()
unmute_sc = pygame.image.load('buttons/unmute.png').convert_alpha()
minus_sc = pygame.image.load('buttons/minus.png').convert_alpha()
plus_sc = pygame.image.load('buttons/plus.png').convert_alpha()

play_sc = pygame.transform.scale(play_sc, (play_sc.get_width()//7, pause_sc.get_height()//7))
pause_sc = pygame.transform.scale(pause_sc, (pause_sc.get_width()//7, pause_sc.get_height()//7))
skip_sc = pygame.transform.scale(skip_sc, (skip_sc.get_width()//8, skip_sc.get_height()//8))
previous_sc = pygame.transform.scale(previous_sc, (pause_sc.get_width()//1.2, previous_sc.get_height()//8))
mute_sc = pygame.transform.scale(mute_sc, (mute_sc.get_width()//7, mute_sc.get_height()//7))
unmute_sc = pygame.transform.scale(unmute_sc, (unmute_sc.get_width()//7, unmute_sc.get_height()//7))
plus_sc = pygame.transform.scale(plus_sc, (plus_sc.get_width()//8, plus_sc.get_height()//8))
minus_sc = pygame.transform.scale(minus_sc, (minus_sc.get_width()//8, minus_sc.get_height()//8))

pause_rect = pause_sc.get_rect(center=(W//2-400, 500))
skip_rect = skip_sc.get_rect(center=((W//2)+140, 500))
previous_rect = previous_sc.get_rect(center=((W//2)-140, 500))
play_rect = play_sc.get_rect(center=(W//2, 500))
mute_rect = mute_sc.get_rect(center=(500, 100))
unmute_rect = unmute_sc.get_rect(center=(700, 100))
plus_rect = plus_sc.get_rect(center=(550, 500))
minus_rect = minus_sc.get_rect(center=(50, 500))



is_mute = False
is_play = False
current_photo = None
count = 0
check = False
#print(songs[images[0].replace(' ', '_')])
pygame.mixer.music.load(songs[images[0][6:-4].replace('-', '_')])

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if play_rect.collidepoint(event.pos):
                is_play = not is_play
                current_photo = get_current_photo(images)
                
                current_names = start(current_photo[4], current_photo[5])
                
                if check == False:
                    pygame.mixer.music.play()
                    check = not check
                else:
                    pygame.mixer.music.unpause()

                count=1
                play_rect.centerx = -100
                pause_rect.centerx = W//2
                
            elif skip_rect.collidepoint(event.pos):
                if count==1:
                    next()
                    pygame.mixer.music.play()
                    current_photo = get_current_photo(images)
                    #check = not check
                    current_names = start(current_photo[4], current_photo[5])
                
                
            elif previous_rect.collidepoint(event.pos):
                if count==1:
                    previous()
                    current_photo = get_current_photo(images)
                    #if is_play:
                    pygame.mixer.music.play()
                    
                    #check = not check
                    current_names = start(current_photo[4], current_photo[5])
                    print(images[0])
                
            elif pause_rect.collidepoint(event.pos):
                is_play = not is_play
                pause_rect.centerx = -100
                play_rect.centerx = W//2
                pygame.mixer.music.pause()
            
            elif mute_rect.collidepoint(event.pos):
                is_mute = not is_mute
                mute()
                mute_rect.x = 700
                unmute_rect.x = 500
            
            elif unmute_rect.collidepoint(event.pos):
                is_mute = not is_mute
                unmute()
                mute_rect.x = 500
                unmute_rect.x = 700
            
            elif plus_rect.collidepoint(event.pos):
                inc_volume()
                print(pygame.mixer.music.get_volume())
            
            elif minus_rect.collidepoint(event.pos):
                dec_volume()
                print(pygame.mixer.music.get_volume())


                
    sc.blit(bg, (0, 0))
    if is_play:
        sc.blit(pause_sc, pause_rect)
        sc.blit(current_photo[0], current_photo[1])
        sc.blit(current_names[0], current_names[1])
        sc.blit(current_names[2], current_names[3])
    else:
        sc.blit(play_sc, play_rect)
        if count == 1:
            sc.blit(current_photo[0], current_photo[1])
            sc.blit(current_names[0], current_names[1])
            sc.blit(current_names[2], current_names[3])
    
    if is_mute:
        sc.blit(unmute_sc, unmute_rect)
    else:
        sc.blit(mute_sc, mute_rect)
        
    
    
    sc.blit(skip_sc, skip_rect)
    sc.blit(previous_sc, previous_rect)
    sc.blit(plus_sc, plus_rect)
    sc.blit(minus_sc, minus_rect)
    
    pygame.display.update()