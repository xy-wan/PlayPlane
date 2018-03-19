#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pygame

pygame.init() #游戏初始化
pygame.mixer.init() #混音器初始化

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 游戏背景音乐
pygame.mixer.music.load("material/sound/game_music.wav")
pygame.mixer.music.set_volume(0.2)


# 子弹发射音乐
bullet_sound = pygame.mixer.Sound("material/sound/bullet.wav")
bullet_sound.set_volume(0.2)


# 飞机失事的音乐
me_down_sound = pygame.mixer.Sound("material/sound/game_over.wav")
me_down_sound.set_volume(0.2)


# 敌方飞机被消灭 

enemy1_down_sound = pygame.mixer.Sound("material/sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)

