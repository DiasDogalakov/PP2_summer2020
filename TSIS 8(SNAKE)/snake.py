import pygame
import math
import random



def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("The best snake game")
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)
        
        active_scene = active_scene.next
        
        pygame.display.flip()
        clock.tick(fps)







###########################################################################################

class SceneBase:
    def __init__(self):
        self.next = self
    
    def ProcessInput(self, events):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene

############################################################################################

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.menuBG = pygame.image.load('menu.jpg')
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene())
    
    def showMenu(self, screen):
        screen.blit(self.menuBG, (0, 0))
    
    def Update(self):
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((153, 153, 255))
        self.showMenu(screen)

#############################################################################################

class GamePoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#############################################################################################

class Food:
    def __init__(self, location):
        self.location = location
        self.color = (100, 100, 200)
        self.apple = pygame.image.load("apple.png")
    
    """def draw(self, screen):
        pygame.draw.rect(
            screen,
            self.color,
            pygame.Rect(
                self.location.x,
                self.location.y,
                20,
                20
            )
        )
    """
    def draw(self,screen):
        screen.blit(self.apple, (self.location.x, self.location.y))





#############################################################################################

class Snake:
    def __init__(self, head):
        self.body = []
        self.head = pygame.image.load("snakehead.png")
        self.body.append(head)
        self.color = (0, 204, 0) #цвет прямоугольника
        self.dx = 20
        self.dy = 0
    
    def saveNewDirection(self, dx, dy):
        self.dx = dx
        self.dy = dy
    
    def updateSnakePosition(self):
        newHeadPosition = GamePoint(self.body[0].x + self.dx, self.body[0].y + self.dy)
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        for i in range(0, len(self.body)):
            if newHeadPosition.x >= 800:
                newHeadPosition.x -= 800; 
            if newHeadPosition.x + 20 <= 0:
                newHeadPosition.x += 800; 
            if newHeadPosition.y >= 600:
                newHeadPosition.y -= 600; 
            if newHeadPosition.y + 20 <= 0:
                newHeadPosition.y += 600; 
        
        self.body[0].x = newHeadPosition.x
        self.body[0].y = newHeadPosition.y

    def distance(self, p1, p2):
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    def canEatFood(self, food):
        if self.distance(self.body[0], food.location) < 2:
            print("test")
            return True
    
    def canChangeLevel(self):
        return len(self.body) == 5


    def increase(self, point):
        taill = self.body[len(self.body) - 1]
        newTaill = GamePoint(taill.x - 20, taill.y)
        self.body.append(newTaill)

    
    def draw(self, screen):
        if self.dx > 0:
            screen.blit(pygame.transform.rotate(self.head,90), (self.body[0].x, self.body[0].y))
        if self.dx < 0:
            screen.blit(pygame.transform.rotate(self.head,270), (self.body[0].x, self.body[0].y))
        if self.dy < 0:
            screen.blit(pygame.transform.rotate(self.head,180), (self.body[0].x, self.body[0].y))
        if self.dy > 0:
            screen.blit(self.head, (self.body[0].x, self.body[0].y))
        for i in range(1, len(self.body), 1):
            pygame.draw.rect(   
                screen,
                self.color,
                pygame.Rect(
                    self.body[i].x,
                    self.body[i].y,
                    20,
                    20
                )
            )
    
    def printStatus(self, screen):
        font = pygame.font.SysFont("comicsansms", 20)
        text = font.render("length: {}".format(len(self.body)), True, (0, 255, 255))
        screen.blit(text, (850, 25 - text.get_height() // 2))

#############################################################################################

class Wall:
    def __init__(self, level):
        self.body = []
        self.color = (255, 153, 51)
        f = open("levels/level{0}.txt".format(level), "r")
        rowNumber = -1
        for row in f:
            rowNumber += 1
            for columNumber in range(0, len(row)):
                if row[columNumber] == '#':
                    brick = GamePoint(columNumber * 20, rowNumber * 20)
                    self.body.append(brick)
                if row[columNumber] == '*':
                    brick = GamePoint(columNumber * 20, rowNumber * 20)
                    self.body.append(brick)
    
    def draw(self, screen):
        for i in range(0, len(self.body), 1):
            pygame.draw.rect(   
                screen,
                self.color,
                pygame.Rect(
                    self.body[i].x,
                    self.body[i].y,
                    20,
                    20
                )
            )
    
    
    def death(x, y, level, flag):
        if flag:
            return 1
        else:
            f = open("levels/level{0}.txt".format(level), "r")
            rowNumber = -1
            for row in f:
                rowNumber += 1
                for columNumber in range(0, len(row)):
                    if row[columNumber] == '#':
                        if columNumber * 20 == x and rowNumber * 20 == y:
                            return 1
    
    
    def randomize(self, level): # проверка на спаун еды
        f = open("levels/level{0}.txt".format(level), "r")
        rand_x = random.randint(0, 40)
        rand_y = random.randint(0, 30)
        rowNumber = -1
        for row in f:
            rowNumber += 1
            for columNumber in range(0, len(row)):
                if row[columNumber] == '#':
                    if columNumber == rand_x and rowNumber == rand_y:
                        return self.randomize(level)
        return (rand_x, rand_y)

#############################################################################################   

class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.snake = Snake(GamePoint(100, 100))
        self.food = Food(GamePoint(20, 140))
        self.food_pos = (0, 0)
        self.currentLevel = 1
        self.maxLevel = 3 # максимальное кол-во уровней(позже сменить на 3)
        self.wall = Wall(self.currentLevel)
        self.flag = 0
    
    def ProcessInput(self, events, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.snake.saveNewDirection(0, -20)       
        elif pressed_keys[pygame.K_DOWN]:
            self.snake.saveNewDirection(0, 20)
        elif pressed_keys[pygame.K_LEFT]:
            self.snake.saveNewDirection(-20, 0)
        elif pressed_keys[pygame.K_RIGHT]:
            self.snake.saveNewDirection(20, 0)
        
    def Update(self):
        self.snake.updateSnakePosition()
        if(self.snake.canEatFood(self.food)):
            self.snake.increase(self.food.location) 
            self.food_pos = self.wall.randomize(self.currentLevel)
            self.food = Food(GamePoint(self.food_pos[0] * 20,self.food_pos[1] * 20))
            if self.snake.canChangeLevel():
                self.currentLevel += 1
                
                if self.currentLevel > self.maxLevel:
                    self.currentLevel = 1
                
                self.wall = Wall(self.currentLevel)
                self.snake = Snake(GamePoint(100, 100))

    
    def Render(self, screen):
        # The game scene is just a blank blue screen
        #menuBG = pygame.image.load('menu.jpg')
        self.flag = Wall.death(self.snake.body[0].x, self.snake.body[0].y, self.currentLevel, self.flag)
        if self.flag:
            pygame.draw.rect(   
                screen,
                (0,0,0),
                pygame.Rect(
                    0,
                    0,
                    1000,
                    600
                )
            )
            font = pygame.font.SysFont("comicsansms", 40)
            text = font.render("GAME OVER", True, (0, 255, 255))
            screen.blit(text, (350, 250))
        else:
            screen.fill((51, 255, 153))

            for i in range(0, 600, 20):
                pygame.draw.line(screen, (0, 0, 0), (0, i), (800, i), 1)
            
            for i in range(0, 800, 20):
                pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 600), 1)

            pygame.draw.rect(screen, (153, 153, 255), (800, 0, 200, 600)) # 800 0 - это левый верхний угол, а 200 600 - это правый нижний угол
            self.wall.draw(screen)
            self.snake.draw(screen)
            #self.food.apple(screen)
            self.food.draw(screen)
            self.snake.printStatus(screen)
        

##############################################################################################

run_game(1000, 600, 10, TitleScene())
