import itchat
import pandas as pd
from pyecharts import Pie, Map, Style, Page, Bar
import os

os.makedirs("./photo/",exist_ok=True)

# 根据key值得到对应的信息
def get_key_info(friends_info, key):
    return list(map(lambda friend_info: friend_info.get(key), friends_info))

def headImg():
    itchat.auto_login(hotReload=False)
    friends = itchat.get_friends(update=True)
    # itchat.get_head_img() 获取到头像二进制，并写入文件，保存每张头像
    for count, f in enumerate(friends):
        # 根据userName获取头像
        img = itchat.get_head_img(userName=f["UserName"])
        imgFile = open("photo/" + str(count)+ ".jpg", "wb")
        imgFile.write(img)
        imgFile.close()

# 获得所需的微信好友信息
def get_friends_info():
    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends()
    friends_info = dict(
        # 省份
        province=get_key_info(friends, "Province"),
        # 城市
        city=get_key_info(friends, "City"),
        # 昵称
        nickname=get_key_info(friends, "Nickname"),
        # 性别
        sex=get_key_info(friends, "Sex"),
        # 签名
        signature=get_key_info(friends, "Signature"),
        # 备注
        remarkname=get_key_info(friends, "RemarkName"),
        # 用户名拼音全拼
        pyquanpin=get_key_info(friends, "PYQuanPin")
    )
    for f in friends:
        print(f)
        # print(get_key_info(f,"City"))
        # print(get_key_info(f,"Nickname"))
        # print(get_key_info(f,"Sex"))
        # print(get_key_info(f,"Signature"))
        # print(get_key_info(f,"RemarkName"))
        # print(get_key_info(f,"PYQuanPin"))
    return friends_info


import matplotlib.pyplot as plt


def getSex():
    itchat.login()
    friends = itchat.get_friends(update=True)
    sex = dict()
    for f in friends:
        if f["Sex"] == 1:  # 男
            sex["man"] = sex.get("man", 0) + 1
        elif f["Sex"] == 2:  # 女
            sex["women"] = sex.get("women", 0) + 1
        else:  # 未知
            sex["unknown"] = sex.get("unknown", 0) + 1
    # 柱状图展示
    for i, key in enumerate(sex):
        plt.bar(key, sex[key])
    plt.savefig("getsex.png")  # 保存图片
    plt.ion()
    plt.pause(5)
    plt.close()  # 图片显示5s，之后关闭
    # plt.show() #不建议用show，show是堵塞式


# 省份分析
def analysisProvince():
    friends_info = get_friends_info()
    df = pd.DataFrame(friends_info)
    province_count = df.groupby('province', as_index=True)['province'].count().sort_values()
    temp = list(map(lambda x: x if x != '' else '未知', list(province_count.index)))
    # 画图
    page = Page()
    style = Style(width=1100, height=600)
    style_middle = Style(width=900, height=500)
    attr, value = temp, list(province_count)
    chart1 = Map('好友分布(中国地图)', **style.init_style)
    chart1.add('', attr, value, is_label_show=True, is_visualmap=True)
    page.add(chart1)
    chart2 = Bar('好友分布柱状图', **style_middle.init_style)
    chart2.add('', attr, value, is_stack=True, is_convert=True,
               label_pos='inside', is_legend_show=True, is_label_show=True)
    page.add(chart2)
    page.render('analysisProvince.html')


# 具体省份分析
def analysisCity(province):
    friends_info = get_friends_info()
    df = pd.DataFrame(friends_info)
    temp1 = df.query('province == "%s"' % province)
    city_count = temp1.groupby('city', as_index=True)['city'].count().sort_values()
    attr = list(map(lambda x: '%s市' % x if x != '' else '未知', list(city_count.index)))
    value = list(city_count)
    # 画图
    page = Page()
    style = Style(width=1100, height=600)
    style_middle = Style(width=900, height=500)
    chart1 = Map('%s好友分布' % province, **style.init_style)
    chart1.add('', attr, value, maptype='%s' % province, is_label_show=True,
               is_visualmap=True, visual_text_color='#000')
    page.add(chart1)
    chart2 = Bar('%s好友分布柱状图' % province, **style_middle.init_style)
    chart2.add('', attr, value, is_stack=True, is_convert=True, label_pos='inside', is_label_show=True)
    page.add(chart2)
    page.render('analysisCity.html')


if __name__ == '__main__':

    # getSex()
    # get_key_info()
    # get_friends_info()
    analysisProvince()
    analysisCity("山东")
    # headImg()
