
import pygame
from settings import Settings
from ship import  Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
def run_game():
    # 初始化创建一个屏幕对象
    pygame.init()
    # 初始化了飞船速度、游戏框外观等等
    ai_settings = Settings()
    # 绘制一个屏幕
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_hight)
    )
    screen.get_rect()
    # 窗口的标题
    pygame.display.set_caption("Alien Invasion")

    #创建play按钮
    play_button = Button(ai_settings,screen,"Play")
    #创建一个用户存储游戏统计信
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    #外星人编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen,ship, aliens)

    # 开始游戏主循环
    while True:
        # 监控键盘和鼠标
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

        if stats.game_active:
            # 调整飞船的位置
            ship.update()
            #删除已经消失的子弹
            gf.update_bullets(ai_settings,screen, stats,sb , ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
            # 输出写入花费的时间比图形绘制到窗口花费的时间更多
            # print(len(bullets))
        # 让最近绘制的屏幕可见
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets, play_button)

run_game()
