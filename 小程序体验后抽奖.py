import time

import uiautomator2 as u2

d = u2.connect('172.27.35.2')  # 连接设备
# d.app_start('com.tencent.mm', stop=True, wait=True)
# d(resourceId="com.tencent.mm:id/cns", text="我").click()
# d(resourceId="android:id/title", text="支付").click()
# d(resourceId="com.tencent.mm:id/atb").click()  # 上传身份证
# d(text="钱包").click()
# d(resourceId="com.tencent.mm:id/dxt", text="零钱").click()
# d(resourceId="com.tencent.mm:id/e3i").click()  # 充值

#
# d(resourceId="com.tencent.mm:id/gwo").send_keys('2.3666')
# d(resourceId="com.tencent.mm:id/cxi").click()  # 付款

# d.unlock()
#
# # 解锁九宫格
# d.swipe_points([(0.218, 0.386), (0.211, 0.52), (0.238, 0.643), (0.516, 0.646), (0.761, 0.654)], duration=0.06)

# d.app_start('com.app.nexdo', stop=True, wait=True)
# d.toast.show('哈哈哈哈哈哈哈666',duration=5)

for _ in range(1):
    # time.sleep(3)
    d.press("volume_mute")
