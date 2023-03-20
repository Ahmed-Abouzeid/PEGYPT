import pandas as pd
import numpy as np
import regex as re
import requests


df = pd.read_excel("annotated_polarized_edited.xlsx", usecols=["index", "id", "text", "polarization", "propaganda"])

c = 0
for e, text in enumerate(df["text"]):


    a = re.findall(r"الأشرار", text)
    a10 = re.findall(r"شهيد", text)
    a11 = re.findall(r"حق بلدنا", text)
    a12 = re.findall(r"بشكل مبهر", text)
    a13 = re.findall(r"صوتي لبطل", text)
    a14 = re.findall(r"أنقذ", text)
    a15 = re.findall(r"انقذ", text)

    a16 = re.findall(r"فنان", text)
    a17 = re.findall(r"انتخابات_بدم_الشباب", text)

    b = re.findall(r"حق الشهيد", text)
    cc = re.findall(r"صوتي رصاصه", text)
    d = re.findall(r"خائن", text)
    f = re.findall(r"اثبتوا انكم مصريين", text)
    g = re.findall(r"عملا", text)
    h = re.findall(r"تتحول لسوريا", text)
    i = re.findall(r"استقرار", text)
    j = re.findall(r"طوابير اللاجئين", text)
    k = re.findall(r"أعداء مصر", text)
    l = re.findall(r"علشان نحمي مصر", text)
    m = re.findall(r"الخراب الكامل", text)
    o = re.findall(r"حرب اهلية", text)
    p = re.findall(r"تحارب جيشك", text)
    q = re.findall(r"قتلى الشرطة والجيش", text)
    r = re.findall(r"قتلى الشرطة", text)
    s = re.findall(r"قتلى الجيش", text)
    t = re.findall(r"حق الشهداء", text)
    u = re.findall(r"حق الشهيد", text)
    v = re.findall(r"عملا", text)
    w = re.findall(r"والنوشتاء", text)
    x = re.findall(r"تبقي اد الدنيا", text)
    y = re.findall(r"من أجل الأمن", text)
    z = re.findall(r"حماية للوطن", text)
    zz = re.findall(r"المؤامرات", text)
    zzz = re.findall(r"الخائنين", text)
    zzzz = re.findall(r"حق شهدائنا", text)
    zzzzz = re.findall(r"رد الجميل", text)
    zzzzzz = re.findall(r"عميل لأمريكا", text)
    zzzzzzz = re.findall(r"لخائن", text)
    zzzzzzzz = re.findall(r"وخونه", text)
    zzzzzzzzz = re.findall(r"دعم الاستقرار", text)
    zzzzzzzzzz = re.findall(r"علشان نبني مصر", text)
    zzzzzzzzzzz = re.findall(r"عملاء", text)
    zzzzzzzzzzzz = re.findall(r"خونة", text)
    zzzzzzzzzzzzz = re.findall(r"الله تعالى يقول", text)

    aa = re.findall(r"أعداء مصر", text)
    bb = re.findall(r"رب العالمين", text)
    ccc = re.findall(r"وعي الشعب المصري", text)
    dd = re.findall(r"#مرسي", text)
    ee = re.findall(r"حافظ على أرضك", text)
    ff = re.findall(r"وعرضك", text)
    gg = re.findall(r"مثلث الشر", text)
    hh = re.findall(r"مستقبل أفضل", text)
    ii = re.findall(r"مسيرة التنمية", text)
    jj = re.findall(r"تعمير مصر", text)
    kk = re.findall(r"هنكمل بناء", text)
    ll = re.findall(r"استشهد عشانك", text)
    mm = re.findall(r"نازل اجيب حق", text)
    nn = re.findall(r"علشان نفرح", text)

    pp = re.findall(r"التصويت بحرية", text)
    qq = re.findall(r"يحيا الرئيس", text)
    rr = re.findall(r"نازل اكمل البناء", text)
    ss = re.findall(r"القضاء على الارهاب", text)
    tt = re.findall(r"نازلين عشان نجبر العالم", text)
    uu = re.findall(r"جنودنا فى سينا", text)
    vv = re.findall(r"شكر للرئيس السيسي", text)
    xx = re.findall(r"الله غاضب", text)

    ww = re.findall(r"عشان خاطر مصر", text)
    yy = re.findall(r"ممول", text)
    yyy = re.findall(r"ناشط عميل", text)
    yyyy = re.findall(r"النشطاء", text)
    yyyyy = re.findall(r"والمرتزقه", text)

    aaa = re.findall(r"بلدك تحافظ", text)
    bbb = re.findall(r"صوتك أمانة", text)
    cccc = re.findall(r"الإرهاب", text)
    ddd = re.findall(r"مع_معتز", text)

    eeee = re.findall(r"ضباطنا", text)
    ffff = re.findall(r"وجنودنا", text)
    gggg = re.findall(r"عشان حلمنا", text)
    hhhh = re.findall(r"عشان ولادنا", text)
    iiii = re.findall(r"استشهد", text)
    all = re.findall(r"كلام الله", text)
    all2 = re.findall(r"صوتك_رصاصة", text)
    all3 = re.findall(r"واجب_وطني", text)
    all4 = re.findall(r"مواجهة التطرف", text)
    all5 = re.findall(r"الشهداء", text)
    all6 = re.findall(r"اعداء مصر", text)
    all7 = re.findall(r"الاعداء", text)
    all8 = re.findall(r"الخونه", text)
    all9 = re.findall(r"علي الطريق الصحيح", text)

    x0 = re.findall(r"مصر من الفتن", text)
    x1= re.findall(r"من كل بيت طلعت تنادى", text)
    x2= re.findall(r"ثقه في الله", text)
    x3= re.findall(r"لاقبال الكبير", text)
    x4= re.findall(r"المعادية للوطن", text)
    x5= re.findall(r"فتمسكم النار", text)
    x6= re.findall(r"لازم ننزل", text)
    x7= re.findall(r"يا ليله العيد", text)
    x8= re.findall(r"ارفع راس الوطن", text)
    x9= re.findall(r"من اجل بقاء الوطن", text)

    y0= re.findall(r"صهيوني", text)
    y1= re.findall(r"نزولك خيانه", text)
    y2= re.findall(r"للشهداء", text)
    y3= re.findall(r"مرسي رائيسي", text)
    y4= re.findall(r"مرسي رئيسي", text)
    y5= re.findall(r"وبشر الصابرين", text)
    y6= re.findall(r"لنا الله", text)
    y7= re.findall(r"ما تشيلش ذنب", text)
    y8= re.findall(r"وبشر الصابرين", text)
    y9= re.findall(r"تنفيذ حكم الإعدام", text)




    all10 = re.findall(r"حق شهداء", text)
    all11 = re.findall(r"بناء مصر", text)
    all12 = re.findall(r"ضحوا بحياتهم", text)
    all13 = re.findall(r"ستفوق نسبة حضور", text)
    all14 = re.findall(r"اغنية", text)
    all15 = re.findall(r"أغنية", text)
    all16 = re.findall(r"اغنيه", text)
    all17 = re.findall(r"اغنية", text)
    all18 = re.findall(r"الانتخابات_فرحتنا", text)
    all19 = re.findall(r"حس وطني", text)
    all20 = re.findall(r"نازلين بالملايين", text)
    all21 = re.findall(r"دينك", text)
    all22 = re.findall(r"أمام تضحيات", text)
    all23 = re.findall(r"داليا زيادة", text)
    all24 = re.findall(r"يزيد المصريين إصرار", text)
    all25 = re.findall(r"يحقق الأمان", text)
    all26 = re.findall(r"يمسح دموع", text)
    all27 = re.findall(r"إختيار رئيسهم بحرية", text)
    all28 = re.findall(r"حملت زوجها على ظهرها", text)

    all29 = re.findall(r"الحدث الديمقراطي", text)
    all30 = re.findall(r"خدمة بلده", text)
    all31 = re.findall(r"ضرورة المشاركة الإيجابية", text)
    all32 = re.findall(r"المفتي", text)
    all33 = re.findall(r"يحث المصريين", text)
    all34 = re.findall(r"عميل صهيوني", text)
    all35 = re.findall(r"صوتك لمصر بكرة", text)
    all36 = re.findall(r"على الحدود", text)
    all37 = re.findall(r"مسيرة حاشدة", text)
    all38 = re.findall(r"صورة حضارية", text)
    all39 = re.findall(r"تحقيق اراد", text)
    all40 = re.findall(r"هنعمرها", text)
    all41 = re.findall(r"نبنيها", text)
    all42 = re.findall(r"البناء والتنميه", text)
    urltoto = re.findall(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", text)

    # whole_urls = []
    # for url in urltoto:
    #     f_url = url[0].replace('http://', '').replace('https://', '')
    #     try:
    #         f_url = requests.head('https://' + f_url).headers['location']
    #     except:
    #         f_url = requests.head('http://' + f_url).headers['location']
    #     whole_urls.append(f_url)
    # no_invest_tweet_flage = True
    # num_check = 0
    # for url in whole_urls:
    #     if (re.findall(r"twitter.com", url) != [] and (re.findall(r"video", url) != [])) or (re.findall(r"twitter.com", url) != [] and re.findall(r"photo", url) != []) or re.findall(r"twitter.com", url) == []:
    #         num_check += 1
    # if num_check > 0:
    #     no_invest_tweet_flage = False
    # if no_invest_tweet_flage or whole_urls == []:
    #     no_invest_counter += 1
    #     print("-------------------------------")
    #     print(e, df["id"][e], text, whole_urls)
    #     print("-------------------------------")



    if (a != [] or a10 != [] or a11 != [] or a12 != [] or a13 != []or a14 != [] or a15 != [] or a16 != [] or b != [] or cc != [] or d != [] or f != [] or g != [] \
            or h != [] or i != [] or j != [] or k != [] or l != [] or m != []\
            or o != [] or p != [] or q != [] or r != [] or s != [] \
            or t != [] or u != [] or w != [] or x != [] or y != [] or z != []\
            or zz != [] or zzz != [] or zzzz != [] or zzzzz != [] or zzzzzz != [] \
            or zzzzzzz != [] or zzzzzzzz != [] or zzzzzzzzz != [] or zzzzzzzzzzz != [] \
            or zzzzzzzzzzzz != [] or zzzzzzzzzzzzz != [] or aa != [] or bb != [] or ccc != [] or dd != [] or ee != [] or ff != [] or gg != [] \
            or hh != [] or ii != [] or jj != [] or kk != [] or ll != [] or mm != [] or pp!= [] or qq != [] or rr != [] or ss != [] \
            or tt != [] or uu != [] or vv != [] or xx != []\
            or nn != [] or ww != [] or yy != [] or yyy != [] or yyyy != []or yyyyy != [] \
            or aaa != [] or bbb != [] or cccc != [] or ddd != [] or eeee != [] or ffff != [] or gggg != [] \
            or hhhh != [] or iiii != []  or all != [] or all2 != [] or all3 != []or all4 != []\
            or all5 != [] or all6 != []  or all7 != []or all8 != []  or all9 != [] or all10 != [] or all11 != []\
            or all12 != [] or all13 != [] or all4 != [] or all15 != [] or all16 != [] or all17 != [] or all18 != [] \
            or all19 != [] or all20 != [] or all21 != [] or all22 != [] or all23 != [] or all24 != [] or all25 != []\
            or  all26 != []or all27 != [] or all28 != [] or all29 != [] or all30 != [] or all31 != [] or all32 != [] or all33 != [] or all34 != [] \
            or all35 != [] or all36 != [] or all37 != [] or all38 != []
    or all39 != [] or all42 != [] or all40 != [] or all41 != [] or a17 != []
    or x0 != [] or x1 != [] or x2 != [] or x3 != [] or x4 != [] or x5 != [] or x6 != [] or x7 != [] or x8 != [] or x9 != []
    or y0 != [] or y1 != [] or y2 != [] or y3 != [] or y4 != []
        or y5 != [] or y6 != [] or y7 != [] or y8 != [] or y9 != []
    ) and df["propaganda"][e] not in [0.0, 1.0]:
        df["propaganda"][e] = 1
        print(df["index"][e], text, 'bias:' + str(df["polarization"][e]), 'propaganda:' + str(df["propaganda"][e]))
        print('--------------------------------------')
        c += 1
    elif (urltoto == [] or df["polarization"][e] == 0) and df["propaganda"][e] not in [0.0, 1.0] and df["polarization"][e] == -1.0:
        df["propaganda"][e] = 0

        c += 1
    #elif urltoto != [] and (df["propaganda"][e] not in [0.0, 1.0] and df["polarization"][e] in [-1.0, 0.0, 1.0]) :
        # print(df["index"][e], text, 'bias:' + str(df["polarization"][e]), 'propaganda:' + str(df["propaganda"][e]))
        # print('--------------------------------------')
        #c += 1
    # (a == [] and b == [] and cc == [] and d == [] and f == [] and g == [] \
    #         and h == [] and i == [] and j == [] and k == [] and l == [] and m == []\
    #         and o == [] and p == [] and q == [] and r == [] and s == [] \
    #         and t == [] and u == [] and w == [] and x == [] and y == [] and z == []\
    #         and zz == [] and zzz == [] and zzzz == [] and zzzzz == [] and zzzzzz == [] \
    #         and zzzzzzz == [] and zzzzzzzz == [] and zzzzzzzzz == [] and zzzzzzzzzzz == [] \
    #         and zzzzzzzzzzzz == [] and zzzzzzzzzzzzz == [] and aa == [] and bb == [] and ccc == [] and dd == [] and ee == [] and ff == [] and gg == [] \
    #         and hh == [] and ii == [] and jj == [] and kk == [] and ll == [] and mm == [] and pp== [] and qq == [] and rr == [] and hawkes_simulation == [] \
    #         and tt == [] and uu == [] and vv == [] and xx == []\
    #         and nn == [] and ww == [] and yy == [] and yyy == [] and yyyy == []and yyyyy == [] \
    #         and aaa == [] and bbb == [] and cccc == [] and ddd == [] and eeee == [] and ffff == [] and gggg == [] \
    #         and hhhh == [] and iiii == [] and urltoto == [] and all == [] and all2 == [] and all3 == []and all4 == []\
    #         and all5 == []and all6 == []  and all7 == []and all8 == []  and all9 == [] and all10 == [] and all11 == []\
    #         and all12 == [] and all13 == []and all14 == [] and all15 == [] and all16 == [] and all17 == [] and all18 == []\
    #         and all19 == [] and all20 == [] and all21 == [] and all22 == [] and all23 == [] and all24 == [] and all25 == []\
    #         and all26 == []and all27 == [] and all28 == [] and all29 == [] and all30 == [] and all31 == [] and all32 == [] and all33 == [] and all34 == [] \
    #         and all35 == [] and all36 == [] and all37 == [] and all38 == []
    # and all39 == [] and all42 == [] and all40 == [] and all41 == [])  or (df["polarization"][e] == 0)

#df.to_excel("annotated_propaganda.xlsx")
print(c)

    #print(df["index"][e], text)
    #print('-----------------------------------')



