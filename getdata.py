import requests


class GetData:

    def download(self, id):

        u = 'https://phyllis.nl/Biomass/AjaxView/' + id          #根据样品id构造url

        print("开始下载数据，样品id：{0}  url：{1}".format(id,u))

        trytimes = 3  # 重试的次数
        for i in range(trytimes):                             #对请求超时的爬虫进行多次重试
            try:


                response = requests.get(u, timeout=3)
                #	注意此处也可能是302等状态码
                if response.status_code == 200:
                    print("下载数据成功")
                    # 指定使用utf-8编码
                    response.encoding = 'utf-8'
                    return response.text                #请求成功后返回网页数据
                    break
            except:
                print('requests failed {} time'.format(i))



        # 如果请求成功，则返回网页数据，否则返回None

        return None


if __name__ == "__main__":                      #进行测试
    url = 'http://www.baidu.com/'
    d = GetData()
    baidu_html = d.download(url)
    print(baidu_html)
