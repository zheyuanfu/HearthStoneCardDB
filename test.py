# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import sys
from pyquery import PyQuery as query
import requests
import json

reload(sys)
sys.setdefaultencoding('utf-8')
#url = 'http://www.bilibili.com/video/part-twoelement-1.html#!page=' + str(page)
# url = u'https://www.bilibili.com/video/part-twoelement-1.html'
# url = u'http://www.imooc.com/'
# url = u'http://lol.qq.com/web201310/info-heros.shtml'
# url = u'http://www.qiushibaike.com/hot/page/1'
#url = u'http://db.duowan.com/lushi/card/list/eyJwIjoxLCJzb3J0IjoiaWQuZGVzYyJ9.html'
#user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
# headers = {'User-Agent' : user_agent}
urls = ('eyJwIjoxLCJzb3J0IjoiaWQuZGVzYyJ9', 'eyJwIjoyLCJzb3J0IjoiaWQuZGVzYyJ9',
       'eyJwIjozLCJzb3J0IjoiaWQuZGVzYyJ9', 'eyJwIjo0LCJzb3J0IjoiaWQuZGVzYyJ9',
       'eyJwIjo1LCJzb3J0IjoiaWQuZGVzYyJ9', 'eyJwIjo2LCJzb3J0IjoiaWQuZGVzYyJ9',
       'eyJwIjo3LCJzb3J0IjoiaWQuZGVzYyJ9', 'eyJwIjo4LCJzb3J0IjoiaWQuZGVzYyJ9',
       'eyJwIjo5LCJzb3J0IjoiaWQuZGVzYyJ9', 'eyJwIjoxMCwic29ydCI6ImlkLmRlc2MifQ_3__3_',
       'eyJwIjoxMSwic29ydCI6ImlkLmRlc2MifQ_3__3_', 'eyJwIjoxMiwic29ydCI6ImlkLmRlc2MifQ_3__3_',
       'eyJwIjoxMywic29ydCI6ImlkLmRlc2MifQ_3__3_', 'eyJwIjoxNCwic29ydCI6ImlkLmRlc2MifQ_3__3_',
       'eyJwIjoxNSwic29ydCI6ImlkLmRlc2MifQ_3__3_')
class hearthstone:
    def  __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        self.headers = {'User-Agent' : self.user_agent}
        self.cards = []
        self.enable = False
    def getPage(self, pageIndex):
        url = 'http://db.duowan.com/lushi/card/list/' + str(urls[pageIndex]) + '.html'
        request = urllib2.Request(url, headers=self.headers)
        response = urllib2.urlopen(request)
        html = unicode(response.read(), 'utf-8')
        return html

    def getPageItems(self, pageIndex):
        html = self.getPage(self, pageIndex)
        if not html:
            print "page loading failed..."
            return None
        pat = '<td[\s\S]*?.png">([\s\S]*?)</a>[\s\S]*?skill">([\s\S]*?)</td>[\s\S]*?txt">([\s\S]*?)' \
          '</td>[\s\S]*?<td>([\s\S]*?)</td>[\s\S]*?<td>([\s\S]*?)</td>[\s\S]*?' \
          '<td>([\s\S]*?)<img[\s\S]*?<td>([\s\S]*?)<img[\s\S]*?<td>([\s\S]*?)<img[\s\S]*?</td>'
        pattern = re.compile(pat)
        items = re.findall(pattern, html)
        cardInfo = []
        for item in items:
            haveSkill = re.search('[\S]', item[1])
            skill = ''
            if haveSkill:
                skillPat = '<a[\s\S]*?="([\s\S]*?)"><img[\s\S]*?</a>'
                skillDes = re.findall(skillPat, item[1])
                # skill = unicode(skillDes[0], 'utf-8').encode('utf-8')
                skill = skillDes[0].encode('utf-8')
            cardInfo.append(item[0], skill, item[2], item[3], item[4], item[5], item[6], item[7])
            # print item[0], skill, item[2], item[3], item[4], item[5], item[6], item[7]
        return cardInfo

    def loadPage(self):
        if self.enable == True:
            if len(self.cards) < 2:
                pageCard = self.getPageItems(self.pageIndex)
                if pageCard:
                    self.cards.append(pageCard)
                    self.pageIndex += 1

def main():
    '''
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = unicode(response.read(), 'utf-8')
    # print response.read()
    # print html
    '''

    '''
    f = open("CardInfo.html",'w')
    file = open('CardInfo.txt', 'w')
    f.write(html.encode('utf-8'))
    file.write(html.encode('utf-8'))
    f.close()
    file.close()
    '''
    '''
    # pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
    #                      'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    # items = re.findall(pattern, html)
    # print len(items)
    # for item in items:
    #     print item[0], item[1], item[2], item[3], item[4]
    '''

    '''
    #qiushibaike hadn written spyder
    # pat = '<div class="content">[\s\S]*?span>([\s\S]*?)</span>'
    # pat = '<div[\s\S]*?h2>([\s\S]*?)</h2>[\s\S]*?content"><span>([\s\S]*?)</span>[\s\S]*?number">' \
    #       '([\s\S]*?)</i>[\s\S]*?number">([\s\S]*?)</i>'
    pat = '<div[\s\S]*?h2>([\s\S]*?)</h2>[\s\S]*?content">[\s\S]*?' \
          '<span>([\s\S]*?)</span>' \
          '([\s\S]*?)' \
          'number">([\s\S]*?)</i>[\s\S]*?' \
          'number">([\s\S]*?)</i>[\s\S]*?'
    pattern = re.compile(pat)
    items = re.findall(pattern, html)
    print len(items)
    for item in items:
        haveImg = re.search("img", item[2])
        if haveImg:
            imgPat = '[\s\S]*?alt="([\s\S]*?)" />[\s\S]*?'
            img = re.findall(imgPat, item[2])
            print item[0], item[1], img[0], item[3], item[4]
        else:
            print item[0], item[1], item[3], item[4]
    '''
    '''
    #hearthstone card db
    pat = '<td[\s\S]*?.png">([\s\S]*?)</a>[\s\S]*?skill">([\s\S]*?)</td>[\s\S]*?txt">([\s\S]*?)' \
          '</td>[\s\S]*?<td>([\s\S]*?)</td>[\s\S]*?<td>([\s\S]*?)</td>[\s\S]*?' \
          '<td>([\s\S]*?)<img[\s\S]*?<td>([\s\S]*?)<img[\s\S]*?<td>([\s\S]*?)<img[\s\S]*?</td>'
    pattern = re.compile(pat)
    items = re.findall(pattern, html)
    print len(items)
    for item in items:
        haveSkill = re.search('[\S]', item[1])
        skill = ''
        if haveSkill:
            skillPat = '<a[\s\S]*?="([\s\S]*?)"><img[\s\S]*?</a>'
            skillDes = re.findall(skillPat, item[1])
            # skill = unicode(skillDes[0], 'utf-8').encode('utf-8')
            skill = skillDes[0].encode('utf-8')
        print item[0], skill, item[2], item[3], item[4], item[5], item[6], item[7]
    '''

if __name__ == '__main__':
    main()













