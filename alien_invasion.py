
import pygame
from settings import Settings
from ship import  Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # 初始化创建一个屏幕对象
    pygame.init()
    # 初始化了飞船速度、游戏框外观等等
    ai_settings = Settings()
    # 绘制一个屏幕
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_hight)
    )
    # 窗口的标题
    pygame.display.set_caption("Alien Invasion")

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
        gf.check_events(ai_settings,screen,ship,bullets)
        # 调整飞船的位置
        ship.update()
        #删除已经消失的子弹
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings,aliens)
        # 输出写入花费的时间比图形绘制到窗口花费的时间更多
        # print(len(bullets))
        # 让最近绘制的屏幕可见
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
