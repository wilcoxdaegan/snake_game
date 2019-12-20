'''
Created on Dec 8, 2019

@author: wilcoxdaegan
'''

import sys, pygame, time, random

pygame.init()
game_over_font = pygame.font.Font(None, 100)
play_again_font = pygame.font.Font(None, 48)

white = (255, 255, 255)

snake_img = pygame.image.load('snake_smaller.png')
black_img = pygame.image.load('black_smaller.png')

top, left, bottom, right = 0, 0, 760, 760
start_over = False


class Snake:
    speed = 10
    direction = "left"
    score = 0
    
    def __init__(self, length, game_mode="slow"):
        self.x, self.y = [200], [200]
        self.game_mode = game_mode
        self.length = length + 1  # # misleading length, due to display.blit workaround
        Snake.length_copy = self.length
        
        for l in range(1, length + 1):
            self.x.append(self.x[l - 1])
            self.y.append(self.y[l - 1])
        
        Application.display.blit(snake_img, (self.x[0], self.y[0]))
        
    def moveDir(self, apple):
        done = False
        x, y, speed, length = self.x, self.y, self.speed, self.length
        
        self.derender()
        
        for l in range(length - 1, 0, -1):
            x[l] = x[l - 1]
            y[l] = y[l - 1]
        
        if (Snake.length_copy <= length - 1):  # # small collission immunity; for initializaiton
            done = self.isCollided(apple)
            
        direc = self.direction
        if direc == "left":
            x[0] -= speed
        elif direc == "right":
            x[0] += speed
        elif direc == "up":
            y[0] -= speed
        elif direc == "down":
            y[0] += speed
        
        if (Snake.length_copy <= length - 1):  # # small collission immunity; for initializaiton
            done = self.isCollided(apple)
        
        self.checkBorder()
        Snake.length_copy -= 1
        
        return done

    def render(self):
        for l in range(0, self.length):
            Application.display.blit(snake_img, (self.x[l], self.y[l]))
            
    def derender(self):
        Application.display.blit(black_img, (self.x[self.length - 1], self.y[self.length - 1]))
    
    def derender_all(self):   
        for i in range(0, 780, 20):
            for j in range(0, 780, 20):
                Application.display.blit(black_img, (i, j))

    def checkBorder(self):
        x, y = self.x, self.y
        if (x[0] <= 0):
            self.direction = "down"
            
        if (y[0] >= 780):
            self.direction = "right"
            
        if (x[0] >= 780):
            self.direction = "up"
            
        if (y[0] <= 0):
            self.direction = "left"
            if (x[0] <= 0):  # # necessary to circle back for counter clockwise rotation
                self.direction = "down"
            
    def isCollided(self, apple):
        x, y = self.x, self.y
        for i in range(2, len(x) - 1):
            if (x[0] == x[i] and y[0] == y[i]):
                return True
        
            if (self.isApple(x, y, apple)):
                apple.derender()
                apple.location = random.randint(0, 780), random.randint(0, 780)
                apple.locationCheck()
                apple.render()
                
                # # fast mode? linear vs. constant? command line?
                self.score += 1
                
                game_mode = self.game_mode
                
                if (game_mode == "slow"):
                    self.increaseLength(2)
                elif (game_mode == "fast"):
                    self.increaseLength(5)
                elif (game_mode == "hyper"):
                    self.increaseLength(20)
                else:
                    self.increaseLength(int(self.game_mode))
                
        return False
    
    def isApple(self, x, y, apple):
        for i in range(0, 11, 10):
            for j in range(0, 11, 10):
                if (x[0] + i == apple.location[0] and y[0] + j == apple.location[1]):
                    return True
            
        for i in range(0, 11, 10):
            for j in range(0, 11, 10):
                if (x[0] - i == apple.location[0] and y[0] - j == apple.location[1]):
                    return True
            
    def increaseLength(self, amount):
        for _ in range(0, amount):
            self.length += 1
            self.x.append(self.x[0])
            self.y.append(self.y[0])
    
    def clear(self):
        self.direction = None
        self.length = None
        self.y = None
        self.x = None
        self.speed = None
        
        
class Apple:

    def __init__(self):
        self.location = random.randint(0, 780), random.randint(0, 780)
    
    def render(self):
        Application.display.blit(snake_img, self.location)
        
    def locationCheck(self):
        if (self.location[0] % 10 != 0):
            self.location = (self.location[0] - (self.location[0] % 10)), self.location[1]
            
        if (self.location[1] % 10 != 0):
            self.location = self.location[0], (self.location[1] - (self.location[1] % 10))
    
    def derender(self):
        Application.display.blit(black_img, self.location)
    
    
class Application:

    def __init__(self):
        global start_over 
        start_over = False
        Application.display = pygame.display.set_mode(size=(800, 800))
        args = sys.argv
        if (len(args) != 1): ## need exceptions
            if args[1] == "custom":
                self.player = Snake(5, game_mode=int(args[2]))
            else:
                self.player = Snake(5, game_mode=args[1])
        else:
            self.player = Snake(5)
        
        player = self.player
        
        pygame.display.set_caption("Snake")
        
        apple = Apple()
        apple.locationCheck()
        apple.render()
        
        
        self.while_open(player, apple)
        
        
    def while_open(self, player, apple):
        while True:
            for event in pygame.event.get():  # # closes with exit
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                # # remember if reach wall change direction
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and player.direction != "right":
                        player.direction = "left"
                    elif event.key == pygame.K_RIGHT and player.direction != "left":
                        player.direction = "right"
                    elif event.key == pygame.K_UP and player.direction != "down":
                        player.direction = "up"
                    elif event.key == pygame.K_DOWN and player.direction != "up":
                        player.direction = "down"
    
            done = player.moveDir(apple)
            
            if not done:
                apple.render()
                player.render()
                pygame.display.update()
                time.sleep(.033)
            else:
                player.render()
                self.game_over(player)
                self.while_repeat(player)
                break
            
    def while_repeat(self, player):
        global start_over
        while True:
            for event in pygame.event.get():  # # closes with exit
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        start_over = True
                        player.clear()
                        break
                    elif event.key == pygame.K_n:
                        sys.exit()
            
            pygame.display.update()
            
            if start_over:
                break
        
        

    def game_over(self, player):
        Application.display.blit(game_over_font.render("Game Over!", True, white), (200, 200))
        Application.display.blit(play_again_font.render("Play again? (Y/N)", True, white), (190, 300))
        Application.display.blit(play_again_font.render("Score: " + str(player.score), True, white), (325, 325))

        
while True:        
    App = Application()
