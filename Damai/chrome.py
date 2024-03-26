from selenium import webdriver
driver = webdriver.Chrome(executable_path='google-chrome')
# 打开登陆界面
print('打开登陆界面')
driver.get('https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F')
print('打开登陆界面成功')
# 进入到账号密码输入的嵌套页面
driver.switch_to.frame(driver.find_element('css selector','#alibaba-login-box'))
# 输入账号
driver.find_element('css selector','#fm-login-id').send_keys('18973738468')
# 输入密码
driver.find_element('css selector','#fm-login-password').send_keys('040725Liu')
driver.implicitly_wait(10)
driver.quit()