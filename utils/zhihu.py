#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import time
from PIL import Image

from conf import PC_HEADERS, CAPTCHA_PATH


FAKE_USER_INFO = ''' userInfo:{"viewport":[1280,628,1469178066603],"trace":[[0,0,1469178067787],[0,0,1469178068561],[0,0,1469178069677],[0,0,1469178070649],[0,0,1469178071424],[228,169,1469178071924],[224,172,1469178072431],[224,172,1469178072932],[224,172,1469178073433],[224,172,1469178073933],[224,172,1469178074434],[348,329,1469178074934],[348,329,1469178075435],[348,329,1469178075936],[348,329,1469178076436],[348,329,1469178076937],[348,329,1469178077439],[348,329,1469178077940],[391,117,1469178078440],[399,111,1469178078941],[399,111,1469178079442],[115,150,1469178079944],[115,150,1469178080445],[115,150,1469178080948],[115,150,1469178081451],[115,150,1469178081952],[567,145,1469178082452],[567,145,1469178082953],[567,145,1469178083458],[567,145,1469178083958],[567,145,1469178084461],[567,145,1469178084961],[567,145,1469178085461],[567,145,1469178085965],[567,145,1469178086467],[567,145,1469178086968],[479,105,1469178087469],[479,105,1469178087970],[479,105,1469178088470],[479,105,1469178088971],[479,105,1469178089472],[479,105,1469178089973],[479,105,1469178090474],[479,105,1469178090974],[479,105,1469178091475],[479,105,1469178091975],[479,105,1469178092475],[479,105,1469178092977],[479,105,1469178093478],[479,105,1469178093979],[289,150,1469178094482],[289,150,1469178094982],[289,150,1469178095483],[289,150,1469178095984],[289,150,1469178096485],[468,83,1469178096985],[471,83,1469178097488],[471,83,1469178097988],[471,83,1469178098489],[471,83,1469178098990],[471,83,1469178099490],[471,83,1469178099991],[546,62,1469178100491],[546,61,1469178100992],[651,28,1469178101492],[508,28,1469178101993],[477,7,1469178102494],[477,7,1469178102995],[477,7,1469178103496],[538,17,1469178103996],[545,37,1469178104497],[551,77,1469178104998],[551,77,1469178105498],[551,77,1469178105999],[514,94,1469178106500],[514,94,1469178107001],[475,127,1469178107501],[475,127,1469178108003],[475,127,1469178108504],[475,127,1469178109005],[475,127,1469178109507],[475,127,1469178110011],[475,127,1469178110511],[475,127,1469178111012],[475,127,1469178111512],[475,127,1469178112012],[475,127,1469178112513],[600,144,1469178113013],[600,144,1469178113513]],"register":{"submit":[["mouseenter",113,22,1469178112830],["mousedown",110,16,1469178113366]],"captcha":{"mouse":[["mouseenter",76,18,1469178081422],["mouseleave",67,31,1469178081976],["mouseenter",60,16,1469178105809],["click",23,33,1469178106624],["mouseleave",-16,66,1469178107068]],"keyborad":[["keydown",65,1469178106688],["keydown",83,1469178106748],["keydown",68,1469178106815],["keyup",65,1469178106823],["keydown",70,1469178106842],["keyup",83,1469178106895],["keyup",68,1469178106935],["keyup",70,1469178107021]]},"password":{"mouse":[["mouseenter",7,32,1469178100315],["click",55,18,1469178100660],["mouseleave",124,-3,1469178101195]],"keyborad":[["keydown",1469178100751],["keydown",1469178100802],["keydown",1469178100890],["keyup",1469178100913],["keydown",1469178100954],["keyup",1469178100985],["keyup",1469178101017],["keydown",1469178101106],["keyup",1469178101113],["keydown",1469178101138],["keydown",1469178101218],["keyup",1469178101249],["keydown",1469178101251],["keyup",1469178101293],["keyup",1469178101342],["keyup",1469178101398]]},"account":{"mouse":[["mouseenter",124,45,1469178101195],["mouseleave",-7,24,1469178102032],["mouseenter",7,13,1469178103754],["mouseleave",47,-94,1469178104309]],"keyborad":[["keydown",65,1469178102408],["keydown",83,1469178102520],["keydown",68,1469178102568],["keyup",65,1469178102611],["keydown",70,1469178102625],["keyup",83,1469178102675],["keyup",68,1469178102711],["keyup",70,1469178102787],["keydown",65,1469178102796],["keydown",83,1469178102876],["keydown",68,1469178102955],["keyup",65,1469178102960],["keydown",70,1469178102972],["keyup",83,1469178103028],["keyup",68,1469178103063],["keyup",70,1469178103135],["keydown",65,1469178103148],["keydown",83,1469178103220],["keydown",68,1469178103276],["keyup",65,1469178103309],["keydown",70,1469178103328],["keyup",83,1469178103371],["keyup",68,1469178103415],["keyup",70,1469178103455]]},"fullname":{"mouse":[["mouseenter",60,6,1469178104565],["click",60,14,1469178104955],["mouseleave",60,160,1469178105809]],"keyborad":[["keydown",65,1469178105006],["keydown",83,1469178105107],["keydown",68,1469178105143],["keyup",65,1469178105163],["keydown",70,1469178105166],["keyup",83,1469178105234],["keyup",68,1469178105286],["keyup",70,1469178105323]]}}}'''


def get_xsrf(session):
    index_url = 'http://www.zhihu.com'
    index_page = session.get(index_url, headers=PC_HEADERS)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    _xsrf = re.findall(pattern, html)
    return _xsrf[0]


def get_captcha(session, type='login'):
    t = str(int(time.time()*1000))
    captcha_url = 'http://www.zhihu.com/captcha.gif?r={0}&type={1}'.format(t, type)
    r = session.get(captcha_url, headers=PC_HEADERS)
    with open(CAPTCHA_PATH, 'wb') as f:
        f.write(r.content)
        f.close()
    im = Image.open(CAPTCHA_PATH)
    im.show()
    im.close()
    captcha = raw_input("please input the captcha\n>")
    return captcha


def is_login(session):
    url = "https://www.zhihu.com/settings/profile"
    login_code = session.get(url, allow_redirects=False).status_code
    if int(x=login_code) == 200:
        return True
    else:
        return False


def login(session, secret, account):
    post_url = 'http://www.zhihu.com/login/email'
    postdata = {
        '_xsrf': get_xsrf(session),
        'password': secret,
        'remember_me': 'true',
        'email': account,
    }
    r = session.post(post_url, data=postdata, headers=PC_HEADERS)
    if u'登录成功' not in r.text:
        postdata["captcha"] = get_captcha(session)
        r = session.post(post_url, data=postdata, headers=PC_HEADERS)
    session.cookies.save()
    return session


def signup(session, fullname, email, secret):
    post_url = 'http://www.zhihu.com/register/email'
    postdata = {
        '_xsrf': get_xsrf(session),
        'fullname': fullname,
        'password': secret,
        'account': email,
        'userinfo': FAKE_USER_INFO,
    }
    postdata["captcha"] = get_captcha(session, 'register')
    r = session.post(post_url, data=postdata, headers=PC_HEADERS)
    print r.text
