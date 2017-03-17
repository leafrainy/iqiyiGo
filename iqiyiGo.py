#coding:utf8
# 爱奇艺追剧助手
# 2017-03-17
# leafrainy (leafrainy.cc)  

from bs4 import BeautifulSoup as bs
import requests
import time

#剧集名称
partName = "龙珠超"
#剧集链接
mainUrl = "http://www.iqiyi.com/lib/m_207436714.html"
#server酱sckey
sckey = "SCU819Tf2bf7e88b0d9c41806c434xxxxxxxx"
nowtime = time.strftime('%m-%d %H:%M:%S',time.localtime(time.time()))

#获取本地最新一集
def getLastPart():
	f = open('part.txt','r')
	lastPart = (f.readlines())[0]
	return lastPart

#获取线上最新一集
def getNewPart(url):
    s = requests.Session()
    allData = s.get(url)
    waitMovData = bs(allData.content,'lxml').find('div',{'class':'mod_album_lists clearfix'}).find('ul').find_all('a')
    newPart = str(waitMovData[len(waitMovData)-1].get_text()).split('-')[1]
    return newPart

#修改本地文件为最新一集
def updateTxt(num):
	f = open('part.txt','w')
	f.write(num)
	f.close()

#发送消息
def sendMsg(msg,sckey=sckey):
	msgUrl = "http://sc.ftqq.com/"+sckey+".send?text="+msg
	requests.get(msgUrl)

if __name__ =='__main__':

    newPart =getNewPart(mainUrl)
    lastPart = getLastPart()

    if newPart == lastPart:
	    print partName+"还没更新"
    if newPart > lastPart:
	    updateTxt(newPart)
	    sendMsg(partName+"第"+newPart+"集刚刚更新~"+nowtime)
	    print "更新了"
