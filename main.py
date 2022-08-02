import pygame
import colors
import os
import random
import csv

pygame.init()
pygame.font.init()

# game specific variables.
# phone screen size 1080x2160
clock = pygame.time.Clock()
window_width, window_hight = 1080, 1450
win = pygame.display.set_mode ((window_width, window_hight))
main_screen_size = (1070,1450)
main_screen_pos = (5,75)
score = 0
hits = 0



def display_text(pos: list, size: list, text: str) -> None:
    
    """Function to display text on screen
    
    :param pos: position of displayed text
    :param size: font size
    :param text: text to be displayed
            
    
    """
    
    font = pygame.font.SysFont(None, size)
    img = font.render(text, True, colors.BLACK)
    win.blit(img, pos)
    
    return


def draw_window ():
    
    """Anything that is to be drawn on window
    
    """
    
    # drawing background
    win.fill(colors.GREEN)
    pygame.draw.rect(win,(colors.BLACK), main_screen_pos + main_screen_size)
    
    # draw objects
    spaceship.move()
    asteroid.dropAsteroid()
    
    # display hits and score
    display_text((20,10), 80, 'hits : '+str(hits))
    
    # update all above activities
    pygame.display.update()
    
    


class Asteroid ():
    
    image_list = [
    "asteroid_1.png",
    "asteroid_2.png",
    "asteroid_3.png",
    "asteroid_4.png",
    "asteroid_5.png",
    "asteroid_6.png",
    ]
    
    def __init__ (self):
        
        """
        
        """
        
        self.size = [150, 150]
        self.pos = [random.randint(0,window_width-self.size[0]),-155]
        self.speed = 20
        self.moving = True
        self.movement_direction = "east"
        self.img_unsized = pygame.image.load(os.path.join("assets", random.choice(self.image_list))).convert()
        self.final_image = pygame.transform.scale(self.img_unsized, self.size)
    
    
    def dropAsteroid (self):
        
        """ Drop Astroid:
            drops asteroid with speed self.speed

        
        
        
        """
        
        win.blit(self.final_image, self.pos)
        self.pos[1] += self.speed
        
        if self.pos[1] > window_hight:
            self.pos = [random.randint(0,window_width-self.size[0]),-155]
            self.img_unsized = pygame.image.load(os.path.join("assets", random.choice(self.image_list)))
            self.final_image = pygame.transform.scale(self.img_unsized, self.size)
        return

    


class Spaceship ():
    
    def __init__(self):
        self.pos = [300, 1250]
        self.size = [200, 200]
        self.speed = 10
        self.moving = True
        self.movement_direction = None
        self.spaceship_img = pygame.image.load(os.path.join("assets","spaceship.png")).convert()
        self.spaceship = pygame.transform.scale(self.spaceship_img, self.size)
        return
    
    def move (self):
        
        """Move Spaceship object with
           speed = self.speed in
           direction = 

    
        
        """
        
        win.blit(self.spaceship, self.pos)
        
        # Spaceship movement
        if self.moving == True:
            if self.movement_direction == "north":
                self.pos[1] -= self.speed
            if self.movement_direction == "south":
                self.pos[1] += self.speed
            if self.movement_direction == "east":
                self.pos[0] +=self.speed
            if self.movement_direction == "west":
                self.pos[0] -= self.speed
        
        # border restriction  
        if self.pos[0] + self.size[0] >= window_width:
            self.moving = False
            self.pos[0] -= self.speed
        if self.pos[0] <= 0:
            self.moving = False
            self.pos[0] += self.speed
            
        
        
            
            
        
#  GAME OBJECTS
spaceship = Spaceship()
asteroid = Asteroid() 



# images
def main () ->None:
    
    # game specific variables
    run = True
    FPS = 60
    

    # testing
    
    # main loop of the game
    while run:
        
        clock.tick(FPS)
        
        # event management system
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
                
    
        # drawing
        draw_window()
        
        
        
        # Spaceship movement
        click_pos_x, click_pos_y = pygame.mouse.get_pos()
        if click_pos_y >  window_hight:
            if click_pos_x > window_width //2:
                spaceship.moving = True
                spaceship.movement_direction = "east"
            elif click_pos_x < window_width//2:
                spaceship.moving = True
                spaceship.movement_direction = "west"
        
        
        # game over (HITTING)
        if spaceship.pos[0]+(spaceship.size[0]//2) in range(asteroid.pos[0]+5,asteroid.pos[0]+asteroid.size[0]-5):
            if spaceship.pos[1] < asteroid.pos[1]+asteroid.size[1]:
                asteroid.pos = [random.randint(0,window_width - asteroid.size[0]),-155]
                global hits
                hits += 1
                
                asteroid.img_unsized = pygame.image.load(os.path.join("assets", random.choice(asteroid.image_list)))
                asteroid.final_image = pygame.transform.scale(asteroid.img_unsized, asteroid.size)
            
                
    
    
    # function for quitting pygame win 
    pygame.quit()

if  __name__ == "__main__":
    main()
