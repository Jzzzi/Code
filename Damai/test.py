from selenium import webdriver
from time import sleep
# 配置工作
options = webdriver.FirefoxOptions()
# Firefox配置profile
options.add_argument("-profile")
options.add_argument("/home/jzi/snap/firefox/common/.cache/mozilla/firefox/zm2epzur.selenium")
# 定义浏览器对象
driver = webdriver.Firefox(options=options)
# 隐藏爬虫特征
# with open('stealth.min.js', mode='r') as f:
#     js = f.read()
# driver.execute_script(
#     script={'source': js},)
# 打开登陆界面
driver.get('https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F')
# 进入到账号密码输入的嵌套页面
driver.switch_to.frame(driver.find_element('css selector','#alibaba-login-box'))
#输入账号
driver.find_element('css selector','#fm-login-id').send_keys('18973738468')
#输入密码
driver.find_element('css selector','#fm-login-password').send_keys('040725Liu')