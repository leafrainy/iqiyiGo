# iqiyiGo
爱奇艺追剧助手，更新剧集自动发送提醒到微信
# 环境依赖
1.Mac OS X EI Capitan 10.11.6

2.python 2.7.10

3.需要安装  bs4,lxml
```
sudo pip install bs4
sudo pip install lxml
```

# 使用方式
1.注册server酱，获取sckey，达到微信提醒的目的

地址 http://sc.ftqq.com/  登陆后获取

![](https://ww3.sinaimg.cn/large/006tKfTcly1fdq7y9b3e9j30ih08odge.jpg)

替换代码中的sckey

2.修改剧集名称
```
partName = "龙珠超"
```
3.修改剧集链接
```
mainUrl = "http://www.iqiyi.com/lib/m_207436714.html"
```
剧集链接获取方式

![](https://ww2.sinaimg.cn/large/006tKfTcly1fdq8dqgo8bj30gm03edh2.jpg)

![](https://ww3.sinaimg.cn/large/006tKfTcly1fdq8eblhf9j30mu0d3tfi.jpg)

![](https://ww1.sinaimg.cn/large/006tKfTcly1fdq8emrbs2j30hp0ewwju.jpg)

4.丢个定时文件执行就好啦~~
