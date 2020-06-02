HOST ='localhost'           #数据库的一些参数配置
PORT =3306
USER ='root'
PASSWD ='412723'
DB ='biomass'
CHARSET ='utf8'
SQL = "INSERT INTO biomass_data(name,sample_id,type,class,special,data) VALUES (%s,%s,%s,%s,%s,%s)"


BIOMASSPATH=r"E:\code\biomass_collect\biomass_name.txt"          #生物质文件读取路径
FAILPATH=r"E:\code\biomass_collect\failed.txt"                   #请求失败的样品id保存路径
CHROMEPATH=r"C:\Users\肖合举\AppData\Local\Programs\Python\Python35\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"