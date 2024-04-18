#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import library
import pygame
import time
import random


# In[3]:


#snake speed
snake_speed=15


# In[4]:


window_x=720
window_y=480


# In[5]:


red=(255,0,0)
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
blue=(0,0,255)


# In[6]:


pygame.init()


# In[7]:


pygame.display.set_caption("snakes")
game_window=pygame.display.set_mode((window_x,window_y))


# In[8]:


fps=pygame.time.Clock()


# In[9]:


snake_position=[100,50]


# In[10]:


snake_body=[[100,50],
           [90,50],
           [80,50],
           [70,50]
           ]


# In[11]:


fruit_position=[random.randrange(1,(window_x//10))*10,
               random.randrange(1,(window_y//10))*10]
fruit_spawn=True


# In[12]:


direction="right"
change_to=direction


# In[13]:


score=0


# In[14]:


def show_score(choice,color,font_name,size):
    try:
        score_font=pygame.font.SysFont(font_name,size)
    except pygame.error:
        score_font=pygame.font.Font(None,size)
    score_surface=score_font.render("score: "+str(score),True,color)
    score_rect=score_surface.get_rect()
    game_window.blit(score_surface,score_rect)


# In[15]:


def game_over():
    my_font=pygame.font.SysFont("arial",50)
    game_over_surface=my_font.render('your score is :'+str(score),True,red)
    game_over_rect=game_over_surface.get_rect()
    game_over_rect.midtop=(window_x/2,window_y/4)
    game_window.blit(game_over_surface,game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


# In[16]:


while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                change_to='UP'
            if event.key==pygame.K_DOWN:
                change_to='DOWN'
            if event.key==pygame.K_LEFT:
                change_to='LEFT'
            if event.key==pygame.K_RIGHT:
                change_to='RIGHT'
        if change_to=='UP' and direction!='DOWN':
            direction='UP'
        if change_to=='DOWN' and direction!='UP':
            direction='DOWN'
        if change_to=='LEFT' and direction!='RIGHT':
            direction='LEFT'
        if change_to=='RIGHT' and direction!='LEFT':
            direction='RIGHT'
    if direction=='UP':
        snake_position[1]-=10
    if direction=='DOWN':
        snake_position[1]+=10
    if direction=='LEFT':
        snake_position[0]-=10
    if direction=='RIGHT':
        snake_position[0]+=10
    snake_body.insert(0,list(snake_position))
    if snake_position[0]==fruit_position[0] and snake_position[1]==fruit_position[1] :
        score+=10
        fruit_spawn=False
    else:
        snake_body.pop()
    if not fruit_spawn:
        fruit_position=[random.randrange(1,(window_x//10))*10,
                       random.randrange(1,(window_y//10))*10]
    fruit_spawn=True
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window,green,
                        pygame.Rect(pos[0],pos[1],10,10))
    pygame.draw.rect(game_window,white,pygame.Rect(
        fruit_position[0],fruit_position[1],10,10))
    if snake_position[0]<0 or snake_position[0]>window_x-10:
        game_over()
    if snake_position[1]<0 or snake_position[1]>window_y-10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0]==block[0]and snake_position[1]==block[1]:
            game_over()
    show_score(1,white,"arial",20)
    pygame.display.update()
    fps.tick(snake_speed)
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




