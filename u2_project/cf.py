import time

import uiautomator2 as u2
from uiautomator2.exceptions import UiObjectNotFoundError


def unlock_phone():
    """手机解锁"""

    print('开始解锁手机..')

    d.unlock()  # 打开屏幕

    # 解锁九宫格
    d.swipe_points([(0.218, 0.386), (0.211, 0.52), (0.238, 0.643), (0.516, 0.646), (0.761, 0.654)], duration=0.06)

    print('手机已解锁...')


d = u2.connect('172.27.35.2')  # 连接设备
d.implicitly_wait(10)  # 设置全局等待时间
unlock_phone()

d.app_start('com.tencent.qt.sns', wait=True)

# 切换到活动banner
d(text="活动").click()

# 进入嘉年华活动
while True:
    d.swipe(0.407, 0.897, 0.48, 0.271, steps=12)
    if d(text="6.6嘉年华").exists:
        d(text="6.6嘉年华").click()
        break

time.sleep(4)  # 等待进入嘉年华页面

# 确保账号登录
while True:
    if not d(text="更改绑定").exists(timeout=10):
        d.press('back')
        d(text="6.6嘉年华").click()
    break

# 点击升一级按钮
d.swipe(0.613, 0.818, 0.601, 0.215, steps=12)
time.sleep(3)
d(text="javascript:DM.df.getClick(669951,'','DM.ld").click()
time.sleep(3)
d.press('back')

# 获取当前福气等级
level = int(d(textContains="当前福气等级").get_text().split('：')[1].strip())

# 获取滚动道具位置
x1, y1 = d(textContains="grade-prop", instance=1).center()
x2, y2 = d(textContains="grade-prop", instance=0).center()

# 领取福气等级对应的道具
for _ in range(level - 2):
    d.swipe(x1, y1, x2, y2, steps=12)

time.sleep(2)
d(textContains="grade-prop", instance=1).sibling(text='点击领取').click()
