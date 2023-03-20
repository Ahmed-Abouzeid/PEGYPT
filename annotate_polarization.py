import pandas as pd
import numpy as np
import regex as re


df = pd.read_excel("annotated_polarized.xlsx", usecols=["index", "id", "text", "polarization", "propaganda"])

c = 0
for e, text in enumerate(df["text"]):
    print(df["index"][e], text, df["polarization"][e])
    print('--------------------------------------')
#     qqqq = re.findall(r"انزلوا يا مصريين", text)
#     qqqqq = re.findall(r"الأشرار", text)
#     qqqqqq = re.findall(r"نازلين نجيب حق الشهيد", text)
#     l = re.findall(r"الخرفان", text)
#     ll = re.findall(r"تحيا مصر", text)
#     lll = re.findall(r"نازل_ادي_حق_بلادي", text)
#     llll = re.findall(r"صوتي رصاصه", text)
#     lllll = re.findall(r"يناشد الجماهير", text)
#     llllll = re.findall(r"نازلين_نكمل_المشوار", text)
#     a = re.findall(r"انزل ماتخفش", text)
#     aaa = re.findall(r"الانتخابات_فرحتنا", text)
#     v = re.findall(r"صوتك أمانه", text)
#     aa = re.findall(r"فضيحة للجزيرة", text)
#     vv = re.findall(r"الله_اكبر_ياجيشنا", text)
#     vvv= re.findall(r"مش_خايفين_و_هننزل", text)
#     vvvv = re.findall(r"لميس_الحديدي", text)
#     ttt = re.findall(r"معتز عبدالفتاح", text)
#
#     vvvvv = re.findall(r"أغنية", text)
#     vvvvvv = re.findall(r"رئيسنا", text)
#     t = re.findall(r"ضد الارهاب", text)
#     tt = re.findall(r"ارهابي خائن", text)
#     m = re.findall(r"المعركة_مستمرة", text)
#     mm = re.findall(r"الشعب_هيقول_كلمته", text)
#     mmm = re.findall(r"حزب_النور_يشارك", text)
#     mmmm = re.findall(r"تناديك لأن صوتك", text)
#     mmmmm = re.findall(r"مصر_تتحدى", text)
#     mmmmmm = re.findall(r"اثبتوا انكم مصريين", text)
#     mmmmmmm = re.findall(r"اختار رئيسك", text)
#     mmmmmmmm = re.findall(r"خروف", text)
#     mmmmmmmmm = re.findall(r"يوم الامتحان يكرم", text)
#     mmmmmmmmmm = re.findall(r"الخوارج", text)
#     mmmmmmmmmmm = re.findall(r"عملا", text)
#     o = re.findall(r"تتحول لسوريا", text)
#     oo = re.findall(r"استقرار", text)
#     ooo = re.findall(r"طوابير اللاجئين", text)
#     oooo = re.findall(r"بشعبها وجيشها", text)
#     ooooo = re.findall(r"نازلين نحتفل", text)
#     oooooo = re.findall(r"أعداء مصر", text)
#     r = re.findall(r"نازلين نكمل المشوار", text)
#     rr = re.findall(r"نازلين - نكمل- المشوار", text)
#     rrr = re.findall(r"نازلين _ نكمل _ المشوار", text)
#     rrrr = re.findall(r"صوتك بيحمى", text)
#     rrrrr = re.findall(r"علشان نحمي مصر", text)
#     rrrrrr = re.findall(r"جنودنا في الميدان واحنا نازلين", text)
#     rrrrrrr = re.findall(r"انزل_شارك", text)
#     rrrrrrrr = re.findall(r"بين_السطور", text)
#     rrrrrrrrr = re.findall(r"صوتك_يصنع_الفرق", text)
#     rrrrrrrrrr = re.findall(r"نازلين_ نكمل _ المشوار", text)
#     rrrrrrrrrrr = re.findall(r"انزل يا مصري", text)
#     rrrrrrrrrrrr = re.findall(r"الخنزيرة", text)
#     rrrrrrrrrrrrr = re.findall(r"شعب مصر الأصيل", text)
#     rrrrrrrrrrrrrr = re.findall(r"يدلي بصوته", text)
#     rrrrrrrrrrrrrrr = re.findall(r"تدلى بصوتها", text)
#
#     g = re.findall(r"نازلين - نكمل - المشوار", text)
#     gg = re.findall(r"نازلين -نكمل - المشوار", text)
#     ggg = re.findall(r"نازلين-نكمل-المشوار", text)
#     gggg = re.findall(r"غالبية الشعب تقف خلف", text)
#     ggggg = re.findall(r"خرفان", text)
#     k = re.findall(r"علشان نحمي مصر", text)
#     kk = re.findall(r"نبنى بلدنا", text)
#     kkk = re.findall(r"الاخوان الارهابيين", text)
#
#     l_m = re.findall(r"يشارك في #الانتخابات_الرئاسية", text)
#     l_mm = re.findall(r"يشارك في #السيسي رئيسي وافتخر", text)
#     l_mmm = re.findall(r"الجزيرة الكاذبة", text)
#     l_mmmm = re.findall(r"وتركيا وقطر", text)
#     l_mmmmm = re.findall(r"يشاركون فى الانتخابات الرئاسية", text)
#     l_mmmmmm = re.findall(r"هانزل غصب عنك", text)
#
#
#
#
#
#
#
#
#     b = re.findall(r"الزم_بيتك", text)
#     u = re.findall(r"انتخابات_هز_الوسط", text)
#     f = re.findall(r"مدد يا سيدى السيسى", text)
#     ff = re.findall(r"الخراب الكامل", text)
#     fff = re.findall(r"دمه يلطش معتز عبدالفتاح", text)
#     ffff = re.findall(r"يسعى لتجميل المشهد", text)
#     fffff = re.findall(r"وصلات رقص", text)
#
#     ffffff = re.findall(r"عايزين نعرف مشوار ايه", text)
#     ffffffff = re.findall(r"انزل كمل انت المشوار", text)
#     fffffff = re.findall(r"استغلال", text)
#     fffffffff = re.findall(r"فقراء", text)
#
#
#
#     n = re.findall(r"رقاصات", text)
#     nn = re.findall(r"تريقة على #الانتخابات_الرئاسية", text)
#     nnn = re.findall(r"والي مش هيشارك", text)
#     nnnn = re.findall(r"منسمعش ديك ام صوتك تانى", text)
#     nnnnn = re.findall(r"كان نفسى انزل معاكوا", text)
#     nnnnnn = re.findall(r"ماتنزلش", text)
#     nnnnnnn = re.findall(r"حازم حسنى", text)
#     nnnnnnnn = re.findall(r"المجلس الثوري المصري", text)
#     uu = re.findall(r"شيطانك_بيقولك_تعمل_ايه", text)
#     uuu = re.findall(r"الإنقلاب", text)
#     uuuu = re.findall(r"التعريص", text)
#     uuuuu = re.findall(r"انتخابات_بدم_الشباب", text)
#     uuuuuu = re.findall(r"قبل أن تنزل في الانتخابات", text)
#     uuuuuuu = re.findall(r"انا_مقاطع_الانتخابات", text)
#
#
#
#     d = re.findall(r"السيسي قاتل", text)
#     dd = re.findall(r"بلحة", text)
#     ddd = re.findall(r"معتقل سياسي", text)
#     y = re.findall(r"متنزلش", text)
#     yy = re.findall(r"صوتك_مالوش_لازمة", text)
#     yyy = re.findall(r"المسرحية", text)
#     yyyy = re.findall(r"مسرحية", text)
#     #s = re.findall(r"صهيوني", text)
#     hawkes_simulation = re.findall(r"الخسيسي", text)
#     sss = re.findall(r"مسرحية", text)
#     ssss = re.findall(r"ليه_هاتقاطع_الانتخابات", text)
#     sssss = re.findall(r"مهزلة الانتخابات", text)
#     j = re.findall(r"قلاب", text)
#     jj = re.findall(r"سجون", text)
#     jjj = re.findall(r"معتقلين", text)
#     jjjj = re.findall(r"مهزلة", text)
#
#     h = re.findall(r"انتخابات هز الوسط", text)
#     hh = re.findall(r"بترقصوا", text)
#     hhh = re.findall(r"وسطك أمانه", text)
#     hhhh= re.findall(r"ياريت تناديلي ابن الوسخة اللي طالع بالهاش دة", text)
#     hhhhh= re.findall(r"صباع مطرحه فوسفور و صباع مطرحه بصمه !! منتهى البؤس", text)
#     hhhhhh= re.findall(r"يا أخي آلهي ما ترجع", text)
#     hhhhhhh= re.findall(r"اتفضل يا خويا كمله..كمله للآخر", text)
#     hhhhhhhh= re.findall(r"انتخابات العواجيز", text)
#     hhhhhhhhh= re.findall(r"ترقص", text)
#     hhhhhhhhhh = re.findall(r"هنجيب بهارات من العطار", text)
#     hhhhhhhhhhh = re.findall(r"هاتك يا اغاني و تسقيف", text)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     if (oo != [] or o != [] or ooo != [] or oooo != [] or ooooo != []or oooooo != [] or g != [] or gg != [] or ggg  != []
#         or gggg != []  or ggggg != [] or k != [] or kk != [] or kkk!= []
#         or t != [] or  tt != [] or ttt != [] or a!= [] or aa != [] or v != [] or vv != [] or vvv != [] or vvvv != [] or vvvvv != [] or vvvvvv != [] or aaa != [] or qqqq != [] or qqqqq != [] or qqqqqq != [] or l != []
#         or ll != [] or lll != [] or llll != [] or lllll != [] or llllll != [] or  m != []
#     or  mm != [] or  mmm != [] or  mmmm != [] or  mmmmm != [] or  mmmmmm != []or  mmmmmmm != [] or  mmmmmmmm != []
#     or  mmmmmmmmm != [] or  mmmmmmmmmm != [] or  mmmmmmmmmmm != []\
#         or r != [] or rr != [] or rrr != [] or rrrr != [] or rrrrr != [] or rrrrrr != [] or rrrrrrr != [] or rrrrrrrr != []\
#             or rrrrrrrrr != [] or rrrrrrrrrr != []or rrrrrrrrrrr != [] or rrrrrrrrrrrr != [] or rrrrrrrrrrrrr != [] \
#             or rrrrrrrrrrrrrr != [] or rrrrrrrrrrrrrrr != [] or l_m != [] or l_mm != [] or l_mmm  != [] or l_mmmm != [] or l_mmmmm != [] or l_mmmmmm != [])   \
#             and (y == []  and b == [] and d == [] and dd == [] and ddd == [] and yy == [] and yyy == []  and yyyy == [] and
#                  j == [] and jj == []and jjj == [] and jjjj == []and sssss == [] and ssss == [] and sss == [] and hawkes_simulation == []
#                  and n == [] and nn == [] and nnn == [] and nnnn == [] and nnnnn == [] and nnnnnn == [] and nnnnnnn == []
#                  and nnnnnnnn == [] and u == [] and uu == [] and uuu == [] and uuuu == [] and uuuuu == [] and uuuuuu == []
#                  and uuuuuuu == [] and f == [] and ff == [] and fff == [] and ffff == []and fffff == [] and ffffff == []
#                  and ffffffff == [] and fffffff == [] and fffffffff == [] and h == [] and hh == [] and hhh == [] and hhhh == [] and
#                  hhhhh == [] and hhhhhh == [] and hhhhhhh == [] and hhhhhhhh == [] and hhhhhhhhh == [] and hhhhhhhhhh == [] and hhhhhhhhhhh == []):
#         c += 1
#         df["polarization"][e] = 1
#     elif j != [] or jj != [] or jjj != [] or jjjj != [] or sssss != [] or ssss != [] or sss!= [] or hawkes_simulation != []  or y != []  or b != [] \
#             or d != [] or dd != [] or ddd != [] or yy != [] or yyy != []  or yyyy != [] or n != [] or nn != [] or nnn != [] \
#             or nnnn != [] or nnnnn != [] or nnnnnn != [] or nnnnnnn != [] or nnnnnnnn != [] or u != [] or uu != []\
#             or uuu != [] or uuuu != [] or uuuuu != [] or uuuuuu != []or uuuuuuu != []\
#             or f != [] or ff != [] or fff != [] or ffff != []or fffff != [] or ffffff != [] or \
#             ffffffff != [] or fffffff != [] or fffffffff != [] or h != [] or hh != [] or hhh != [] or hhhh != [] or \
#                  hhhhh != [] or hhhhhh != [] or hhhhhhh != [] or hhhhhhhh != [] or hhhhhhhhh != [] or hhhhhhhhhh != [] or hhhhhhhhhhh != []:
#         df["polarization"][e] = -1
#         c += 1
#
#     if df["index"][e] in [1591, 1575, 1505, 1504, 1503, 1502, 1500, 1498, 1497, 1484, 1415, 1428, 473, 478, 5563, 5562, 5555, 5779, 5777, 5776, 5768, 5703, 5704, 5773]:
#         df["polarization"][e] = 0
#         c += 1
#
#     elif df["index"][e] in [5739, 5736, 5733, 5730, 5717, 5706, 5863, 5862, 5773, 5556, 5499, 5525, 5541, 5495, 5489, 5482, 1352, 1332, 1382, 1495]:
#         df["polarization"][e] = -1
#         c+= 1
#     elif df["index"][e] in [1564, 1552, 1545, 1466, 1434, 1408, 1399, 1389, 1311, 5849, 5616,5615, 5614,5576, 5505, 5485, 5480, 5469, 5303, 5137, 5071, 4980, 4933, 4905, 4753, 4447, 2664, 2559, 2407, 2244, 5480, 5484, 5485, 5486, 5492, 5496, 5498, 5500, 5501, 5503, 5505, 5506, 5507, 5511, 5517, 5521, 5532, 5536, 5542, 5543, 5550, 5551, 5554, 5557, 5561, 5566, 5567, 5794, 5762, 5765, 5770, 5772, 5775, 5778, 5786, 6860, 5852,5849,5846,5843,5840,5838,5837,5834,5699,5702,5707,5709,5719,5721,5731,5740,5742,5743,5744,5745,5747,5748]:
#         df["polarization"][e] = 1
#         c+= 1
# df.to_excel("annotated_polarized.xlsx")
# print(c)
    #print(df["index"][e], text)
    #print('-----------------------------------')



