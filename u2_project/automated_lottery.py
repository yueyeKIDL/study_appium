import time

import uiautomator2 as u2
import uiautomator2.ext.htmlreport as htmlreport
from uiautomator2.exceptions import UiObjectNotFoundError


def init():
    """初始化操作"""

    d.healthcheck()
    d.implicitly_wait(10)  # 设置全局等待时间
    hrp = htmlreport.HTMLReport(d, 'report')  # 日志输出
    hrp.patch_click()


def unlock_phone():
    """手机解锁"""

    print('开始解锁手机..')

    d.unlock()  # 打开屏幕

    # 解锁九宫格
    d.swipe_points([(0.218, 0.386), (0.211, 0.52), (0.238, 0.643), (0.516, 0.646), (0.761, 0.654)], duration=0.06)

    print('手机已解锁...')


def start_applet():
    """启动小程序"""

    print('启动小程序')

    # 启动微信
    d.app_start('com.tencent.mm', stop=True, wait=True)
    # d.session('com.tencent.mm')

    # 等待主界面【微信】文字显示
    d(text='微信').wait()

    # 下拉显示小程序栏
    d.swipe(0.519, 0.21, 0.43, 0.699, steps=8)

    time.sleep(1)
    d(text='活动抽奖').click()

    print('小程序已启动...')


def daily_sign():
    """每日签到"""

    print('开始签到...')

    try:
        d(text='每日签到').click(timeout=5)
        d(text='可竖向滚动').click()  # 签到
        d.press("back")
    except UiObjectNotFoundError:
        pass

    print('签到完成..')


def koi_draw():
    """锦鲤抽奖"""

    print('进入锦鲤抽奖...')

    d(text='幸运大礼').click()

    # 确保进入到锦鲤列表页面
    d(resourceId="com.tencent.mm:id/dl", text="幸运大礼").wait(timeout=15)

    # 点击第一个
    d.click(0.47, 0.233)

    # 确保进入到抽奖详情页面
    d(resourceId="com.tencent.mm:id/dl", text="抽奖详情").wait(timeout=15)

    # 点击抽奖按钮
    for _ in range(2):
        # 上滑直到暴露【点击抽奖】按钮，并点击该按钮
        d.swipe(0.47, 0.905, 0.533, 0.111, steps=30)
        time.sleep(1)  # 避免点击不稳定
        lottery_btn = d(text='点击抽奖', className='android.widget.Button')
        if lottery_btn.exists:
            lottery_btn.click()
            time.sleep(1)  # 避免点击不稳定
            break

    d.press('back')

    # 确保进入到锦鲤列表页面
    d(resourceId="com.tencent.mm:id/dl", text="幸运大礼").wait(timeout=15)

    d.press('back')

    print('已抽锦鲤大奖...')


def is_experience_applet():
    """处理体验小程序"""

    immediate_experience_btn = d(text="立即体验")
    if immediate_experience_btn.exists(timeout=1.3):
        immediate_experience_btn.click()
        d(text='允许').click()

        time.sleep(31)
        d.press('back')


def click_lottery_btn():
    """抽奖详情页面，点击抽奖按钮"""

    # 确保已进入到抽奖详情页面
    d(resourceId="com.tencent.mm:id/dl", text="抽奖详情").wait(timeout=15)

    for _ in range(2):

        # 上滑直到暴露【点击抽奖】按钮，并点击该按钮
        d.swipe(0.47, 0.905, 0.533, 0.511, steps=30)
        lottery_btn = d(text='点击抽奖', className='android.widget.Button')
        if lottery_btn.exists:
            lottery_btn.click()
            is_experience_applet()
            break
    d.press('back')


def go_lottery():
    """抽奖走起GOGOGO！"""

    print('开始商品抽奖...')

    while True:  # 循环下滑操作

        # 确保回到活动抽奖页面
        d(resourceId="com.tencent.mm:id/dl", text="活动抽奖").wait(timeout=15)

        d.swipe(0.453, 0.832, 0.442, 0.482, steps=25)

        try:
            # 选择一个抽奖产品
            d(className='android.widget.Image', instance=1).click()
        except UiObjectNotFoundError:
            pass

        # 退出误点的广告
        if d(resourceId="com.tencent.mm:id/don").exists(timeout=1):
            d.press('back')

        # 抽奖！
        click_lottery_btn()

        # 抽奖完成
        if d(text="自助福利").exists:
            break  # 退出下滑操作

    # 滑动到顶端刷新
    d(scrollable=True).scroll.toBeginning()
    time.sleep(5)

    for _ in range(3):  # 滑动并点击漏掉的抽奖

        # 确保回到活动抽奖页面
        d(resourceId="com.tencent.mm:id/dl", text="活动抽奖").wait(timeout=15)

        d.swipe(0.453, 0.832, 0.442, 0.482, steps=25)

        try:
            # 选择一个抽奖产品
            d(className='android.widget.Image', instance=1).click()
        except UiObjectNotFoundError:
            pass

        # 退出误点的广告
        if d(resourceId="com.tencent.mm:id/don").exists(timeout=1):
            d.press('back')

        # 抽奖！
        click_lottery_btn()

    print('商品抽奖完成...')


def open_red_envelope():
    """开红包"""

    print('领取红包...')

    try:
        d(text="每日红包").click(timeout=1)
        d(text="¥1.88").click()

        # 点击开红包
        time.sleep(2)
        d.click(0.506, 0.594)
        d.press('back')
    except UiObjectNotFoundError:
        pass

    print('红包已领取...')


def get_free_prize_draw():
    """领取免费抽奖次数"""

    d(text="领取免费次数").click()
    to_watch_btn = d(text="去观看")
    if to_watch_btn.exists(timeout=2):
        to_watch_btn.click()
        d.press('volume_mute')  # 静音
        time.sleep(31)  # 观看广告时长
        try:
            d(text="关闭").click()
        except UiObjectNotFoundError:
            pass

    d.press('volume_mute')  # 取消静音

    # 点击待领取按钮
    waiting_received_btn = d(text="待领取")
    while True:
        if waiting_received_btn.exists(timeout=1):
            waiting_received_btn.click()
            time.sleep(1)
        else:
            break

    d.click(0.069, 0.905)  # 点击空白处，关闭【领取免费次数】页面


def lucky_wheel_draw():
    """幸运大转盘抽奖GO！"""

    while True:
        time.sleep(.5)
        d.click(0.49, 0.488)

        if d(textContains='抽奖次数已用完').exists(timeout=1) or d(text="获取更多幸运币").exists(timeout=1):
            break

        time.sleep(6)  # 等待抽奖格子转动时长

        if d(text="再来一次").exists:
            d(text="再来一次").click()
        else:
            d(text="").click()


def lucky_snatch_treasure():
    """幸运夺宝"""

    print('进入幸运夺宝...')

    # 确保进入到活动抽奖页面
    d(resourceId="com.tencent.mm:id/dl", text="活动抽奖").wait(timeout=15)

    # 滑动到顶端，进入幸运夺宝
    d(scrollable=True).scroll.toBeginning()
    time.sleep(5)
    d(text='幸运夺宝').click()

    # 领取免费抽奖次数
    get_free_prize_draw()

    # 幸运大转盘抽奖GO！
    lucky_wheel_draw()

    print('大转盘抽奖完成...')


def all_quit():
    """退出微信等操作"""
    pass

    # d.press('volume_mute')  # 取消静音
    # d.app_stop('com.tencent.mm')
    # d.screen_off()


def main():
    init()  # 初始化操作
    unlock_phone()  # 手机解锁
    start_applet()  # 启动小程序
    daily_sign()  # 每日签到功能
    koi_draw()  # 锦鲤抽奖
    go_lottery()  # 抽奖功能
    open_red_envelope()  # 领取每日红包
    lucky_snatch_treasure()  # 幸运夺宝
    all_quit()  # 退出


if __name__ == '__main__':
    d = u2.connect('172.27.35.2')  # 连接设备
    main()
