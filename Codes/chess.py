
import pygame

 

# Width & Height
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# initializing.
pygame.init()

# Making screen
SCREEN = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

# Set title of the window
pygame.display.set_caption("pygame test")

# creat clock instance
clock = pygame.time.Clock()

#Status
playing = True

 

while playing:

    #Handling events.
    for event in pygame.event.get():

        #If exit Button (X) is pressed, quit the game
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()

 

        # When the key is pressed
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_a:
                    print("a is pressed")
                    pass
                case pygame.K_RIGHT:
                    pass
                case pygame.K_UP:
                    pass
                case pygame.K_DOWN:
                    pass

        # When the key is up
        if event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_a:
                    print("a is pressed")
                    pass
                case pygame.K_RIGHT:
                    pass
                case pygame.K_UP:
                    pass
                case pygame.K_DOWN:
                    pass


    # setting fps limit (60) --> 60fps
    clock.tick(60)