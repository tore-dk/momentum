# all imports
import math
import pygame

# init things
pygame.init()
width, height = 1600, 900
screen = pygame.display.set_mode((width, height))

# DEFINING CLASSES

# class defining objects, need speed and mass and position
class obj:
    def __init__(self, speed, mass, cords, size):
        self.speed = speed
        self.mass = mass
        self.cords = list(cords)
        self.size = list(size)

    def newvelocity(self, speednew):
        self.speed = speednew

    def move(self):
        self.cords[0] += self.speed



# GLOBAL FUNCTIONS
def calculateCollision(box1, box2): # it calculates the new velocity of box1
    newSpeed1 = 0
    newSpeed2 = 0

    newSpeed2 = box2.speed*((box2.mass - box1.mass)/(box2.mass + box1.mass)) + box1.speed*((2*box1.mass)/(box2.mass + box1.mass))
    newSpeed1 = box1.speed*((box1.mass - box2.mass)/(box1.mass + box2.mass)) + box2.speed*((2*box2.mass)/(box1.mass + box2.mass))
    box1.speed = newSpeed1
    box2.speed = newSpeed2


def checkCollision(box1, box2):
    if box1.cords[0] <= box2.cords[0] + box2.size[0] and box2.cords[0] <= box1.cords[0] + box1.size[0]:
        return True
    return False

# MAKING INITIAL OBJECTS

obj1 = obj(0, 1, (300, 200), (100, 100))
obj2 = obj(-0.1, 1000000, (1000, 200), (100, 100))
wallCords = (0, 0, 100, height)

# the thing counting collisions
counter = 0

# MAIN LOOP
running = True
while running:

    # so the animation can run multiple times
    running1 = True
    while running1:

        # inputs
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT:
                running = False
                running1 = False
                break
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False
                running1 = False


        # update positions
        obj1.move()
        obj2.move()

        # check collision and update speed if necessary (and counter now)
        if checkCollision(obj1, obj2):
            calculateCollision(obj1, obj2)
            obj1.cords[0] = obj2.cords[0] - obj1.size[0]
            obj2.cords[0] = obj1.cords[0] + obj1.size[0]
            print(obj2.cords[0])
            counter += 1
            print(counter)

        if obj1.cords[0] <= wallCords[0] + wallCords[2] and wallCords[0] < obj1.cords[0] + obj1.size[0]:
            obj1.speed *= -1
            obj1.cords[0] = wallCords[0] + wallCords[2]
            counter += 1
            print(counter)



        # drawing
        screen.fill((0,0,0))

        pygame.draw.rect(screen, (0, 255, 100), (obj1.cords[0], obj1.cords[1], obj1.size[0], obj1.size[1]))
        pygame.draw.rect(screen, (0, 255, 100), (obj2.cords[0], obj2.cords[1], obj2.size[0], obj2.size[1]))
        pygame.draw.rect(screen, (255, 0, 0), wallCords)
        
        #update screen
        pygame.display.update()
    

