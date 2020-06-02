from selenium import webdriver
import time
from setting import CHROMEPATH

class GetSample:

    def samplecollect(self,c, name):
        sample_list = []
        print('开始第{}爬取：{}'.format(c, name))   #用于计数，观察爬取次数。

        driver = webdriver.Chrome(CHROMEPATH)  #打开浏览器

        driver.maximize_window()
        driver.get('https://phyllis.nl/Browse/Standard/ECN-Phyllis')
        time.sleep(3)
        driver.find_element_by_id("searchbox").send_keys(name)       #将查询数据送去搜索栏中
        driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(5)

        id_text = driver.find_elements_by_xpath('//li[@class="jstree-leaf jstree-unchecked"]')
        for i in id_text:

            sample_list.append(i.get_attribute('id'))
        return sample_list                                              #返回提取的样品id列表

if __name__ == "__main__":                                     #进行测试
    url = 'http://www.baidu.com/'
    d = GetSample()
    bing_html = d.samplecollect(url)
    print(bing_html)

