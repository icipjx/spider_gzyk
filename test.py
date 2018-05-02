#encoding:utf-8
from pyquery import  PyQuery as pq
import re
import requests
import codecs

html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0"><a href="link2.html"><span class="b">first item 
<li class="item-1"><a href="link2.html"><span class="bold">second item</span></a></li>
</span></a></li>
</ul >
</div>
</div>
'''
doc = pq(html)
item = doc(".list")
item_1 = doc(".wrap")
# lis = item.find("a .bold")
lis = item.parents(".wrap")
# lis = item.children(".item-1")
# print item
# print item_1
item_2 = doc(".item-0")
# print item_2.text()
# item = str(item_2)
# print type(item)
# print(doc('li'))
dis_man = "用药常识、免疫力、养生、家庭护理、服药、吃药时间、药效、高温防中暑、急救电话、copd、不良习惯、老人"
pre_cold_man = "流行性感冒、流感、感冒、冬天、冬季、戴口罩、保暖、肺炎球菌疫苗"
away_harm_man = "抽烟、吸烟、烟民、戒烟、二手烟、雾霾、空气污染、煮妇肺"
dis_cog_man = "慢阻肺、慢性阻塞性肺病、慢性阻塞性肺疾病、COPD"
men_man = "心理、失眠、快乐、心态、心境、乐观、积极、生气、情绪、开心、抑郁"
eat_man = "蔬菜、水果、维生素、饮食、食品、食物、喝水、糖、盐、脂肪、膳食、营养、吃、喝"
sports_man = "老年人运动、健步走、步行、锻炼、太极拳"

dis_man_lists = dis_man.split("、")
pre_cold_man_lists = pre_cold_man.split("、")
away_harm_man_lists = away_harm_man.split("、")
dis_cog_man_lists = dis_cog_man.split("、")
men_man_lists = men_man.split("、")
eat_man_lists = eat_man.split("、")
sports_man_lists = sports_man.split("、")

manage_lists = list()
manage_lists.append(dis_man_lists)
manage_lists.append(pre_cold_man_lists)
manage_lists.append(away_harm_man_lists)
manage_lists.append(dis_cog_man_lists)
manage_lists.append(men_man_lists)
manage_lists.append(eat_man_lists)
manage_lists.append(sports_man_lists)
a_list = ["老年人运动好","吃多点蔬菜","慢阻肺病早知","吸烟有害身体健康","防范流行性感冒","增强免疫力","哈哈","太极拳"]
b =0
for a in a_list:
    for manage_list in manage_lists:
        for i in manage_list:
            if i in a:
                # print str(manage_list)
                b += 1
                break
# print b
# src = 'src="/ckfinder/userfiles/images/dasd.jpg "发生激烈的开房记录是的浪费空间上离开房间了开始减肥, src="/ckfinder/userfiles/images/&#21307;&#38498;(6).jpg"'
# art_html_str = re.sub('src="(.*?)/images', 'src="(\w+)/images',".",src)
# print art_html_str
# mage=["1","2"]
# print str(mage)

# pic = requests.get("http://www.gyfyy.com/ckfinder/userfiles/images/2(127).jpg")     #发出GET请求
# fp = open('./'+'1.jpg','wb')   #创建图片文件,以视频名字  命名
# fp.write(pic.content)     #将下载图片写入文件
# fp.close()      #关闭文件
# page = "http://www.gyfyy.com/cn/lists-52-52-568-17.html"
# def page_judge(page_now):
#     doc = pq(url=page_now)
#     a_items = doc('#main_list_AspNetPager1 a').items()
#     a_list = list()
#     for i in a_items:
#         a_list.append(str(i))
#         # print str(i)
#     nextpage_a = str(a_list[-2])
#     # print "xiayiye:" + str(aa[-2])
#     nextpage_href_unf = re.findall('href="(.*?)"',nextpage_a,re.S)
#     if len(nextpage_href_unf) != 0:
#         return "http://www.gyfyy.com" + nextpage_href_unf[0]
#     else:
#         return "null"
# print page_judge(page)
i=5
while i!=0:
    print i
    i -=1







