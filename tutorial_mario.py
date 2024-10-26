import pygame;

pygame.init();

# 背景設定
WIDTH, HEIGHT = 400, 300
WINDOWS = pygame.display.set_mode((WIDTH, HEIGHT))

# 多分マリオの初期位置
mx, my, vy = 50, 250, 0

# ?
on_ground = False

enemies = [
    {
    'rect': pygame.Rect(250,250,20,20),
    # ?
    'dir': -2
    },
    {
    'rect': pygame.Rect(200,250,20,20),
    'dir': -1
    },
    {
    'rect': pygame.Rect(350,250,20,20),
    'dir': -2
    },
]

clock = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        # 条件式がtrueの時、exit関数でウィンドウが閉じられ、そうでない時は0を返す
        exit() if e.type == pygame.QUIT else 0

    keys = pygame.key.get_pressed()
    # →key、←keyで位置を動かす
    mx+=(keys[pygame.K_RIGHT]-keys[pygame.K_LEFT])*5

    # -=15は15減算数されるよという意味
    # keyが押されていて、on_groundの時、vy-=15が実行されるということ(ジャンプ)
    # K_SPACEが押されていなくて、on_groundでないときは、マリオのy座標にvy(ジャンプした距離)が足されて、マリオが徐々に動いていくようになる
    if keys[pygame.K_SPACE] and on_ground:
        vy -= 15
    vy+=1
    my+=vy
    on_ground = False

    if my >= 250:
        my,vy,on_ground = 250, 0, True
    for enemy in enemies:
        # 敵を想定した方向に動かす
        enemy['rect'].x+=enemy['dir']

        # 敵が枠から出た時は、逆方向に動くようにする
        if enemy['rect'].left <= 0 or enemy['rect'].right > WIDTH:
            enemy['dir'] *= -1

        # マリオとぶつかったら、敵が消える
        if enemy['rect'].colliderect(pygame.Rect(mx, my, 20, 20)) and vy > 0:
            enemies.remove(enemy)
            vy = -10

        WINDOWS.fill((135, 206, 235))
        # 表示ウィンドウ、色、視覚の位置を定義して、オブジェクトのrectを呼び出している
        pygame.draw.rect(WINDOWS, (255, 0, 0),(mx, my, 20,20))
        [pygame.draw.rect(WINDOWS,(0, 255, 0), enemy['rect']) for enemy in enemies]

        # サーフェス全体を更新して画面に描写する
        pygame.display.flip()
        # 1sあたりのフレーム
        clock.tick(30)