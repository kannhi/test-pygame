# 必要ライブラリのインポート
import pygame, sys
from pygame.locals import *
import random
 
pygame.init()
 
# 1sあたりのフレーム数を定義
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
 
# ?
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
# 敵用のclass
# 基本であるSpriteクラスを継承した
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
 
      def move(self):
        # 勝手に10フレームずつ動くように変更
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            # ランダムな場所に出現するようにする
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 
 

# playerクラスのコード
# Plyaerクラスが`pygame.sprite.Sprite`クラスの子クラスになる
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # spliteクラスのinitが行われる
        super().__init__() 
        # 画像のファイルパスを渡している
        # 画像だけでは衝突検出などの時に使うboarderは生じないので、rect関数が必要
        self.image = pygame.image.load("Player.png")
        # 画像と同じサイズの四角形を自動に作成可能
        self.rect = self.image.get_rect()
        # rectの座標と同じ位置に画像を描画する
        self.rect.center = (160, 520)
 

    # plyaerの動きを制御する
    def update(self):
        # キーが押されているかチェックされる
        pressed_keys = pygame.key.get_pressed()
        # 上キーが押されたら上に動くなど
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)

       # `self.rect.left > 0`を使用することで画面外にいけない
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
    
    # 描画する表面と、オブジェクトを入力
    def draw(self, surface):
        # 今回は四角形の表面となるのは画像なので、surfaseの代わりにself.imageを追加
        surface.blit(self.image, self.rect)     
 
         
P1 = Player()
E1 = Enemy()
 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    E1.move()
    
    # 背景画面を作成
    DISPLAYSURF.fill(WHITE)

    # プレイヤーと敵を描画
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
         
    pygame.display.update()
    FramePerSec.tick(FPS)
