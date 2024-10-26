## 参考
* https://coderslegacy.com/python/python-pygame-tutorial/

## Game loop begins
* 全てのゲームイベントが発生し、更新され、画面に描画される場所
* 初期設定 → 初期化 → ゲームループの開始
* ゲームループはQUIT typeのイベントが発生するまで何度もループされる
* `pygame.display.update()関数`が呼び出されるまで、ゲームの変更は実装されない
    * ゲームループ内に置く


## sys ライブラリについて
* https://qiita.com/jp0003menegi/items/fbf407af7d294c09481a

## pygameのイベントオブジェクト
* ユーザーがマウスをクリックするなどの特定のアクションを実行した時に発生する
* `pygame.event.get()関数`を呼び出して、発生したイベントを確認可能


```py
# pygame.localsのモジュールをインポート
# sysライブラリは使用しているPFを調べるときや、スクリプトの起動パラメータを取得するために利用
# pytho実行時に、sys.argvなどで引数を渡せる
import pygame, sys
from pygame.locals import *

# pygameの初期化
pygame.init()

#Game loop begins
# 全てのゲームイベントが発生し、更新され、画面に描画される場所
# 初期設定 → 初期化 → ゲームループの開始
# ゲームループはQUIT typeのイベントが発生するまで何度もループされる
while True:
      # Code
      # More Code
    for event in pygame.event.get():
        if event.type == QUIT:
            # pygameうぃんどうとpythonスクリプトを閉じる
            pygame.quit()
            # 単純にsys.exitだけをするとIDEがハングする可能性がある
            sys.exit()
    pygame.display.update()

# 表示画面の作成
DISPLAYSURF = pygame.display.set_mode((300,300))

# 色
color1 = pygame.Color(0, 0, 0)         # Black
color2 = pygame.Color(255, 255, 255)   # White
color3 = pygame.Color(128, 128, 128)   # Grey
color4 = pygame.Color(255, 0, 0)       # Red

# 1sあたりのフレーム数
# 映画は 1 秒あたり 24 フレームで再生されます。これより低い値では明らかにカクカクしますが、100 を超える値では、物体の動きが速すぎて見えなくなる可能性がある
# ゲームの設計方法に応じてゲームごとに異なりますが、30 ～ 60 の間の値を目指す必要があります
FPS = pygame.time.Clock()
FPS.tick(30)

# 衝突検出
object1 = pygame.Rect((20, 50), (50, 100))
object2 = pygame.Rect((10, 10), (100, 100))
 
print(object1.colliderect(object2))
```

# 動かす時
* ⛔️devcontainerで動かない
* そのままcontainerでpygameをインストールして動かすことはできなかった
* エラーは吐いていないようだったが、シミュレーターが出てこなかった
* そこで以下の記事に従って、venvで仮想環境を作成し、対応することにした
    * https://qiita.com/yasushiiwata/items/f1fb3e2e987144f21b6d
    * 詳細不明