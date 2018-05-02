#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from pyquery import  PyQuery as pq
import random
import re
import requests
import csv
import codecs

#将关键字存入列表
bre_man = "家庭氧疗、呼吸操、呼吸锻炼、呼吸功能锻炼、呼吸训练、腹式呼吸、缩唇呼吸、全身操呼吸"
dis_man = "用药常识、免疫力、养生、家庭护理、服药、吃药时间、药效、高温防中暑、急救电话、copd、不良习惯、老人"
pre_cold_man = "流行性感冒、流感、感冒、冬天、冬季、戴口罩、保暖、肺炎球菌疫苗"
away_harm_man = "抽烟、吸烟、烟民、戒烟、二手烟、雾霾、空气污染、煮妇肺"
dis_cog_man = "慢阻肺、慢性阻塞性肺病、慢性阻塞性肺疾病、COPD"
men_man = "心理、失眠、快乐、心态、心境、乐观、积极、生气、情绪、开心、抑郁"
eat_man = "蔬菜、水果、维生素、饮食、食品、食物、喝水、糖、盐、脂肪、膳食、营养、吃、喝"
sports_man = "老年人运动、健步走、步行、锻炼、太极拳"

bre_man_lists = bre_man.split("、")
dis_man_lists = dis_man.split("、")
pre_cold_man_lists = pre_cold_man.split("、")
away_harm_man_lists = away_harm_man.split("、")
dis_cog_man_lists = dis_cog_man.split("、")
men_man_lists = men_man.split("、")
eat_man_lists = eat_man.split("、")
sports_man_lists = sports_man.split("、")

manage_lists = list()
manage_lists.append(bre_man_lists)
manage_lists.append(dis_man_lists)
manage_lists.append(pre_cold_man_lists)
manage_lists.append(away_harm_man_lists)
manage_lists.append(dis_cog_man_lists)
manage_lists.append(men_man_lists)
manage_lists.append(eat_man_lists)
manage_lists.append(sports_man_lists)

#分类目录
bre_man_path = "./bre_man/guangzhouyike.csv"
dis_man_path = "./dis_man/guangzhouyike.csv"
pre_cold_man_path = "./pre_cold_man/guangzhouyike.csv"
away_harm_man_path = "./away_harm_man/guangzhouyike.csv"
dis_cog_man_path = "./dis_cog_man/guangzhouyike.csv"
men_man_path = "./men_man/guangzhouyike.csv"
eat_man_path = "./eat_man/guangzhouyike.csv"
sports_man_path = "./sports_man/guangzhouyike.csv"



#######函数作用：写入csv
def csv_write(list,file_path):
    csvFile2 = open(file_path, 'ab')  # 设置newline，否则两行之间会空一行
    csvFile2.write(codecs.BOM_UTF8)
    ####将文章title和html写入csv文件
    writer = csv.writer(csvFile2)
    #####写入csv文件
    writer.writerow(list)
    csvFile2.close()


#####函数作用：将文章的title html photo解析出来，并写入对应目录下的文件；
###### 函数参数：一级版块包含文章href的html 以及 文章存入路径
def file_write(title_html,dir_path):
    #######若存在则爬取文章title href
    art_href_unf = title_html.attr('href')
    art_href = "http://www.gyfyy.com/cn/" + art_href_unf
    ##############文章标题
    print title
    #####文章链接
    print art_href
    doc = pq(url=art_href)
    time_1 = random.random()
    art_html = doc(".list_info_")
    art_html_str = str(art_html)
    #######获取图片下载链接
    try:
        img_lists = re.findall('src="(.*?)"',art_html_str,re.S)
        for img in img_lists:
            #######拼接图片下载链接
            img_url = "http://www.gyfyy.com" + img
            #######提取原来的图片名字
            img_name = re.findall("images/(.*?).jpg",img,re.S)
            print "loading:"+img_url
            # 发出GET请求，下载图片
            pic = requests.get(img_url)
            #将图片写入文件
            fp = open(dir_path +"images/" + img_name[0] + ".jpg", 'wb')  # 创建图片文件,以视频名字命名
            fp.write(pic.content)  # 将下载图片写入文件
            fp.close()  # 关闭文件
    except Exception, e:
        print e
    #######将html中的图片路径替换为“./images/####.jpg”
    art_photo_html_str = art_html_str.replace("/ckfinder/userfiles/", dir_path)
    # print art_photo_html_str
    article = list()
    file_path = dir_path + "guangzhouyike.csv"
    article.append(title)
    article.append(art_photo_html_str)
    #将文章标题和html写入csv文件
    csv_write(article, file_path)


#####函数作用：判断存入一篇文章的路径;
##### 函数参数：关键词分类列表
def dir_path_jud(manage_list):
    if manage_list == dis_man_lists:
        path = "dis_man/"
    elif manage_list == bre_man_lists:
        path = "bre_man/"
    elif manage_list == pre_cold_man_lists:
        path = "pre_cold_man/"
    elif manage_list == away_harm_man_lists:
        path = "away_harm_man/"
    elif manage_list == dis_cog_man_lists:
        path = "dis_cog_man/"
    elif manage_list == men_man_lists:
        path = "men_man/"
    elif manage_list == eat_man_lists:
        path = "eat_man/"
    else :
        path = "sports_man/"
    return path

######函数作用：判断是否有下一页，若有则返回下一页url,若没有返回“null”;
###### 函数参数：当前页的url
def page_judge(page_now):
    doc = pq(url=page_now)
    a_items = doc('#main_list_AspNetPager1 a').items()
    a_list = list()
    for i in a_items:
        a_list.append(str(i))
        # print str(i)
    nextpage_a = str(a_list[-2])
    # print "xiayiye:" + str(aa[-2])
    nextpage_href_unf = re.findall('href="(.*?)"',nextpage_a,re.S)
    if len(nextpage_href_unf) != 0:
        return "http://www.gyfyy.com" + nextpage_href_unf[0]
    else:
        return "null"

if __name__ == '__main__':
    #将title article_html字段写入csv文件的第一行
    csv_title_list = list()
    csv_title_list.append("title")
    csv_title_list.append("article_html")
    csv_write(csv_title_list, bre_man_path)
    csv_write(csv_title_list, dis_man_path)
    csv_write(csv_title_list, pre_cold_man_path)
    csv_write(csv_title_list, away_harm_man_path)
    csv_write(csv_title_list, dis_cog_man_path)
    csv_write(csv_title_list, men_man_path)
    csv_write(csv_title_list, eat_man_path)
    csv_write(csv_title_list, sports_man_path)

    ####网站入口地址
    doc = pq(url="http://www.gyfyy.com/cn/list-4-4-52.html")
    #获得所有版块的url
    a_sec_html = doc('#main_left_dlMenu a').items()
    href_sec_list = list()


    #a_sec_html
    for a_html in a_sec_html:
        #####获得href属性值
        href_unf_sec = a_html.attr('href')
        #####拼接版块url
        href_sec = "http://www.gyfyy.com/cn/" + href_unf_sec
        #####将拼接完的版块url存入列表
        href_sec_list.append(href_sec)
    print href_sec_list
############################################
    ###有的版块没有超过两页 临时更改列表将href_sec_list改为href_sec_list_temp然后遍历
    href_sec_list_temp = ["http://www.gyfyy.com/cn/list-52-52-575.html","http://www.gyfyy.com/cn/list-52-52-603.html"]
#######################################
    #####遍历每个版块的文章
    for href_sec in href_sec_list:

        page_now = href_sec
        nextpage_flag = 1


        #####此处添加每一页的标题
        # #遍历下一页
        # #######
        # if 最后一页：
        #     break
        while(nextpage_flag == 1 ):
            doc = pq(url=page_now)
            #爬取title
            time_1 = random.random()
            titles_html = doc('.list_title_text a').items()
            for title_html in titles_html:
                # print title_html
                title = title_html.attr('title')
                ####核对title是否存在关键字
                for manage_list in manage_lists:
                    for i in manage_list:
                        if i in title:
                            path = dir_path_jud(manage_list)
                            dir_path = "./"+path
                            file_write(title_html, dir_path)
                            break
            ###当前页若有下一页
            if page_judge(page_now) == "null":
                nextpage_flag = 0
            else:
                page_now = page_judge(page_now)


