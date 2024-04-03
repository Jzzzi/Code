import tushare as ts
import pandas as pd
import datetime

# 股票-代码字典
stock_dict = {
    '中国核电': '601985.SH',
    '华能水电':'600025.SH',
    '华能国际':'600011.SH',
}

# 接口设置
ts.set_token('91d216f0eb0287017fb3e0c085b60ec821aa71fe5aeaadaf89e91e2b')

# 获取昨天日期
today = datetime.date.today()
oneday = datetime.timedelta(days=1)
yesterday = today - oneday
# 把日期变成字符串
yesterday = yesterday.strftime('%Y%m%d')

# 初始化pro接口
pro = ts.pro_api()
pro = ts.pro_api()
for name in stock_dict.keys():
    code = stock_dict[name]
    data = pro.daily(ts_code=code, start_date='20230101', end_date=yesterday)
    data = data[::-1]
    data.to_csv(name+'.csv')
    print(name + '数据下载成功！')