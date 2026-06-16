'''
1 for snake
-1 for water
0 for gun'''

import random
import pygame

pygame.mixer.init()

computer = random.choice([-1,0,1])
youstr = input("Enter your choice:-").lower()
youDict = {"s".lower():1, "w".lower():-1 ,"g".lower():0}
reverseDict = {1:"Snake".lower(),-1:"Water".lower(),0:"Gun".lower()}
you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer==you):
    print("Its a draw")
    draw = pygame.mixer.Sound("freesound_community-stop-rest-84947.mp3")
    draw.play()
    pygame.time.wait(3000)


else:
    if(computer==-1 and you==1): #water_vs_snake
        print("You Win!!!",)
        print("Computer Lose")
        snake_sound = pygame.mixer.Sound("freesound_community-snake-hissing-6092.mp3")
        snake_sound.play()
        pygame.time.wait(3000)

    elif(computer==-1 and you==0): #water_vs_gun
        print("You Lose!!")
        water_sound = pygame.mixer.Sound("dragon-studio-big-rock-splash-2-467477.mp3")
        water_sound.play()
        pygame.time.wait(3000)
        something_went_wrong = pygame.mixer.Sound("eritnhut1992-buzzer-or-wrong-answer-20582.mp3")
        something_went_wrong.play()
        pygame.time.wait(5000)

    elif(computer==1 and you==-1): #snake_vs_water
        print("You Win")
        print("Computer Lose")
        water_sound = pygame.mixer.Sound("dragon-studio-big-rock-splash-2-467477.mp3")
        water_sound.play()
        pygame.time.wait(3000)

        
    elif(computer==1 and you==0):  #snake_vs_gun
        print("You Win")
        print("Computer Lose")
        gun_sound = pygame.mixer.Sound("foisal72-gun-fire-346766.mp3")
        gun_sound.play()
        pygame.time.wait(3000)

    elif(computer==0 and you==1):  #gun_vs_snake
        print("You Lose!!")
        gun_sound = pygame.mixer.Sound("foisal72-gun-fire-346766.mp3")
        gun_sound.play()
        pygame.time.wait(3000)
        something_went_wrong = pygame.mixer.Sound("eritnhut1992-buzzer-or-wrong-answer-20582.mp3")
        something_went_wrong.play()
        pygame.time.wait(5000)

    elif(computer==0 and you==-1):  #gun_vs_water
        print("You Win!!")
        print("Computer Lose")
        water_sound = pygame.mixer.Sound("dragon-studio-big-rock-splash-2-467477.mp3")
        water_sound.play()
        pygame.time.wait(3000)

    else:
        print("Something went wrong!") 
        something_went_wrong = pygame.mixer.Sound("eritnhut1992-buzzer-or-wrong-answer-20582.mp3")
        something_went_wrong.play()
        pygame.time.wait(3000)
