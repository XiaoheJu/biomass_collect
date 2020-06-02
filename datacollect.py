from bs4 import BeautifulSoup
import pymysql
from getdata import GetData
from getsample import GetSample
from setting import HOST,PORT,USER,PASSWD,DB,CHARSET,SQL,BIOMASSPATH,FAILPATH
from failedsample import FailedSample


db = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET) #连接数据库
sql =SQL
cursor = db.cursor()  #创建cursor对象，用来执行sql语句


p_analy = ['Moisture content', 'Ash content', 'Volatile matter', 'Fixed carbon']       #用于进行数据分类
u_analy = ['Carbon', 'Hydrogen', 'Oxygen', 'Nitrogen', '	Sulphur', 'Total (with halides)']
h_value = ['Net calorific value (LHV)', 'Gross calorific value (HHV)', 'HHVMilne']
type_list = ['dry', 'daf']


get_data=GetData()                      #初始化各个功能组件
get_sample=GetSample()
failedsample=FailedSample(FAILPATH)


with open(BIOMASSPATH,'r') as f:   #打开生物质文件，获取爬取的目标名称
    d=f.read()
names=d.split(',')                     #将其处理为列表，以便于循环。
c=1                         #用于爬虫计数
for name in names:
    sample_list=get_sample.samplecollect(c,name)
    c=c+1


    for i in sample_list:
        p=get_data.download(i)
        if p is None:                               #爬取失败后将样品id存储在本地文件中
            print('下载数据失败')
            failedsample.save(i)

            continue
        soup = BeautifulSoup(p, 'html.parser')              #提取页面中的数据
        sample_name = soup.find(name='h3').text
        trs = soup.find_all(name='tr')
        for tr in trs:
            tr_soup = BeautifulSoup(str(tr), "html.parser")
            tds = tr_soup.find_all('td')
            try:
                # print(len(tds))

                # print(tds[2].text)
                if len(tds) == 13:
                    if tds[2].text in p_analy:
                        for t in type_list:
                            if t == 'dry':
                                # dr_p_list.update({tds[2].text: tds[5].text})
                                s = (name,sample_name, 'dry', 'Proximate analysis', tds[2].text, tds[5].text)
                                print(s)
                                cursor.execute(sql, s)
                                db.commit()                                            #保存在数据库中
                            if t == 'daf':
                                # da_p_list.update({tds[2].text: tds[6].text})
                                s = (name,sample_name, 'daf', 'Proximate analysis', tds[2].text, tds[6].text)
                                print(s)
                                cursor.execute(sql, s)
                                db.commit()

                    if tds[2].text in u_analy:
                        for t in type_list:
                            if t == 'dry':
                                # dr_u_list.update({tds[2].text: tds[5].text})
                                # dr_p_list.update({tds[2].text: tds[5].text})
                                s = (name,sample_name, 'dry', 'Ultimate analysis (macroelements)', tds[2].text, tds[5].text)
                                print(s)
                                cursor.execute(sql, s)
                                db.commit()
                            if t == 'daf':
                                # da_u_list.update({tds[2].text: tds[6].text})
                                s = (name,sample_name, 'daf', 'Ultimate analysis (macroelements)', tds[2].text, tds[6].text)
                                print(s)
                                cursor.execute(sql, s)
                                db.commit()

                    if tds[2].text in h_value:
                        for t in type_list:
                            if t == 'dry':
                                # dr_h_list.update({tds[2].text: tds[5].text})
                                # dr_p_list.update({tds[2].text: tds[5].text})
                                s = (name,sample_name, 'dry', 'Heating value', tds[2].text, tds[5].text)
                                print(s)
                                cursor.execute(sql, s)
                                db.commit()
                            if t == 'daf':
                                # da_h_list.update({tds[2].text: tds[6].text})
                                s = (name,sample_name, 'daf', 'Heating value', tds[2].text, tds[6].text)
                                print(s)
                                cursor.execute(sql, s)
                                db.commit()

                    # da.update({tds[2].text: tds[6].text})

                    # dr.update({tds[2].text: tds[5].text})

                    # biomass_data.update({'dry': dr, 'daf': da})

                    # print('{},{},{}'.format(tds[2].text, 'dry :'+tds[5].text, 'daf :'+tds[6].text))




            except Exception as e:
                print(e)
db.close()       #爬取完成后关闭数据库
