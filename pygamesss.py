import pygame
pygame.init()#Search Results

pygame. init() #initialize all imported pygame modules. No exceptions will be raised if a module fails, 
#but the total number if successful and failed inits will be returned as a tuple.
win = pygame.display.set_mode((500,500))#screen

pygame.display.set_caption("My First Game")

#global variables:
x=50
y=50
width=60
height=40
vel = 5
run = True

#main loop:
while run:
	pygame.time.delay(100)#in millisecs
	for event in pygame.event.get():#returns actions that took place
		if event.type==pygame.QUIT:#its the close button
			run=False
		pygame.draw.rect(win,(255,0,0), (x,y,width,height))#takes 3 parameters:where to draw the rect(any other shape is also possible)
		#parameters: where to draw(window), color(r,g,b)(max value=255),tuple with position,dimensions
		# to display the rect:
		pygame.display.update()
		# to move the rect
	keys=pygame.key.get_pressed()#returns a list of keys pressed
	if keys[pygame.K_LEFT]:
		x -= vel #refer to pygame graphing , this causes change in position
	if keys[pygame.K_RIGHT]:
		x += vel
	if keys[pygame.K_UP]:
		y -= vel
	if keys[pygame.K_DOWN]:
		y += vel
	win.fill((0,0,0))# fills the background so that we dont see a mess of rectangles , see pygame docs for more info
	

pygame.quit()
