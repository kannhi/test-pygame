# 必要ライブラリのインポート
import pygame, sys
from pygame.locals import *
import random, time

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
SPEED = 5
SCORE = 0

# フォントの定義
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
# Game Overの文字の定義
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

# ディスプレイ
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
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

    #   def draw(self, surface):
    #     surface.blit(self.image, self.rect)


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
    def move(self):
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

    # # 描画する表面と、オブジェクトを入力
    # def draw(self, surface):
    #     # 今回は四角形の表面となるのは画像なので、surfaseの代わりにself.imageを追加
    #     surface.blit(self.image, self.rect)


P1 = Player()
E1 = Enemy()

# spriteのグループを作成
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)


INC_SPEED = pygame.USEREVENT + 1
# inc_speedイベントオブジェクトを1000msに1回ずつ呼び出す
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5


        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # P1.move()
    # E1.move()

    DISPLAYSURF.blit(background, (0,0))
    # Game Overと違って動的な値のため、ループ内で定義している
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    # # 背景画面を作成
    # DISPLAYSURF.fill(WHITE)

    # plyaer、enemyクラスで定義していた、drawはこちらで定義する形に変更
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # 1つ目の引数は固有値、二つ目はグループ値(敵が1000対いてもこれで一括で動作を決められる)
    # 1つ目と2つ目の衝突検知
    if pygame.sprite.spritecollideany(P1, enemies):

        # 音源データ
        # pygame.mixer.Sound('crash.wav').play()
        # time.sleep(0.5)

        # 画面を赤く塗りつぶす
        DISPLAYSURF.fill(RED)
        # 背景の後にやらなければ、塗りつぶされてしまう
        DISPLAYSURF.blit(game_over,(30,250))
        pygame.display.update()
        for entity in all_sprites:
                # 最後に全てのspriteをkillする
                entity.kill()
        time.sleep(15)
        pygame.quit()
        sys.exit()


    # # プレイヤーと敵を描画
    # P1.draw(DISPLAYSURF)
    # E1.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)
