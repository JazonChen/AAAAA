# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:29:14 2018

@author: Administrator
"""
'''
练习10：
1.获取2300所学校的编码
2.获取31所城市的编码
3.获取142000数据，31/10，每个组有三个城市数据，后面组装在一起
4.将14200数据使用spark统计
'''
'''第一步'''
ls=open('all_school.txt',encoding='utf-8').readlines()
schoolls=[]

for line in ls:
    schoolls.append(line.split('-jianjie-')[1].split('.')[0])
 

import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'}

import json

f=open('北京理科.txt','a',encoding='utf-8')
for schoolid in schoolls:
        m='id={}&type=2&city=11&state=1'.format(schoolid).encode()
        req=r.Request(url,data=m,headers=headers)
        data=r.urlopen(req).read().decode('utf-8','ignore')
        
        if data.startswith('{'):
            data=json.loads(data)
            if data['status']==1:
                j=len(data['data'])
                s=int(0)
                for i in range(0,j-1):
                    n=int(data['data'][i]['plan'])
                    s=s+n
                k=str(data['data'][0]['school'])
                f.write(str(k)+'：'+str(s)+'\n')
                print('成功爬取序号为'+schoolid+'学校')
        else:
            print('出错')
f.close()

'''第二步'''
f1=open('北京理科.txt',encoding='utf-8')
f2=open('北京理科（已排序）.txt','w',encoding='utf-8')
w=f1.readlines()
ls0=[]
ls1=[]
for line in w:
    ls0.append(line.split('：')[0])
    ls1.append(int(line.split('：')[1]))  
mydict=dict(zip(ls1,ls0))
a=sorted(mydict.items(),key=lambda item:item[1])
for k in a:
    f2.write(str(k)+'\n')
    
f1.close()
f2.close()
    
'''第三步'''
f1=open('北京理科（已排序）.txt',encoding='utf-8')
f2=open('北京理科echarts数据.txt','w',encoding='utf-8')
w=f1.readlines()
ls0=[]
ls1=[]
for line in w:
    ls0.append(line.split('(')[1].split(',')[0])
    ls1.append(line.split(', \'')[1].split('\')')[0])
a=ls0
b=ls1
f2.write(str(a)+'\n'+str(b))

f1.close()
f2.close()






    






























