#!/usr/bin/env python
# coding: utf-8

# PYGAME INSTALLNG

# In[1]:


pip install pygame


# In[2]:


pip show pygame


# IMPORT PYGAME MODULE:

# In[1]:


import pygame
pygame.init()


# CREATING PYGAME WINDOW:

# In[30]:


screen=pygame.display.set_mode((400,400),pygame.RESIZABLE)
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            running=False


# CHANGE PYGAME TITLE:

# In[2]:


pygame.display.set_caption("my game")


# CHANGE BACKGROUD COLOR:

# In[38]:


#color website "https://www.rapidtables.com/web/color/RGB_Color.html"
screen=pygame.display.set_mode((400,400),pygame.RESIZABLE)
running=True
while running:
    screen.fill((255,204,204))     #(red,green,blue)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            running=False


# CHANGE IMAGE ICON:

# In[3]:


icon=pygame.image.load("C:\\Users\\aedpu\\arpudha34\\icon1")
pygame.display.set_icon(icon)


# LOAD IMAGE IN PYGAME:

# In[8]:


import pygame
pygame.init()
image=pygame.image.load("C:\\Users\\aedpu\\arpudha34\\icon1")
position=(10,10)
#set the new dimention for the image
new_width=400
new_breadth=400
#resized_image=pygame.transform.scale(image,(new_width,new_breadth))


# In[12]:


screen=pygame.display.set_mode((400,400),pygame.RESIZABLE)
running=True
while running:
    screen.fill((255,204,204))  #(red,green,blue)
    screen.blit(image,position)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            running=False


# TIME FUNCTION

# In[10]:


pygame.time.wait(5000)  #milli seconds in brackets


# In[11]:


pygame.time.delay(6000)


# drawing shapes:

# In[3]:


import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
running=True
while running:
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(0,0,255),[100,100,200,100],0) # if last value is 0 then the shape is filled
    pygame.draw.circle(screen,(255,0,0),(300,300),100,3)
                                        # (position),radius
    pygame.draw.line(screen,(0,0,0),[100,300],[500,300],3)
                                    #[start position],[end position]
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            running=False


# EVENTS IN PYGAME:

# In[5]:


import pygame
pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("hello world")
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:                                                                                                                                                                                                                                               
            pygame.quit()
            running=False
        if event.type==pygame.KEYDOWN: #when a key is pressed
            key=pygame.key.name(event.key)
            print(key,"key is pressed")
        if event.type==pygame.KEYUP:  #when key is released
            key=pygame.key.name(event.key)
            print(key,"key is released")


# In[ ]:


import pygame
pygame.init()
#set the dimentions of the window
window_width=400
window_height=400

#create the window
window=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("python event demo")

#set colors
white=(255,255,255)
black=(0,0,0)

#setting nitial position of rectangle
rect_x=50
rect_y=50

#set the size of the rectangle
rect_width=10
rect_height=15

#mainloop
running=True
while running:
    #hamdle event
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.k_escape:
                running=False
            elif event.key==pygame.K_UP:
                rect_y-=10
            elif event.key==pygame.K_DOWN:
                rect_y+=10
            elif event.key==pygame.K_LEFT:
                rect_x-=10
            elif event.key==pygame.K_RIGHT:
                rect_x+=10
        elif event.type==pygame.MOUSEBUTTON:
            if event.button==1: # left mouse button
                rect_x,rect_y=event.pos
        else:
            if event.type==pygame.QUIT:
                running=

window.fill(WHITE)
pyagme.draw.rect(window,BLACK,(rect_x,))
pygame.display.update()
pygame.quit()


# DISPLAYING TEXT IN WINDOW:

# In[ ]:


fnt=SysFont(name,size,bold=False,italic=False)


# In[7]:


fonts=pygame.font.get_fonts()
for f in fonts:
    print(f)


# In[1]:


import pygame
pygame.init()
#set the dimentions of the window
screen_length=400
screen_height=400

#create the window
window=pygame.display.set_mode((screen_length,screen_height))
pygame.display.set_caption("python text demo")
black=(0,0,0)
white=(255,255,255)
font=pygame.font.SysFont("arialblack",36)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
    screen.fill(WHITE)
    text=font.render("hello,pygame",True,BLACK)
    text_rect=text.get_rect()
    text_rect.center=(screen_width//2,screen_height//2)
    screen.blit(text,text_rect)
    pygame.display.update()
pygame.quit()


# sound and music:

# In[ ]:


import pygame
pygame.init()
#set the dimentions of the window
window_width=400
window_height=400

#create the window
window=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("pygame sound and music demo")
sound_effect=pygame.mixer.Sound("stay")
pygame.mixer.music.load("name")
WHITE=(255,255,255)
BLACK=(0,0,0)
def display_text(surface,text):
    
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.KEYDOWN:
                sound_effect.play()
                pass
        elif event.type==pygame.MOUSEBUTTON:
            sound_effect.play()
        
    pygame.display.update()
pygame.mixer.music.stop()
pygame.quit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




