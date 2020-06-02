import os

class FailedSample:
    def __init__(self,path):
        self.path=path                          #配置存储路径

    def save(self, data):
        # 判断文件路径是否存在，如不存在则抛出错误
        if not os.path.exists(self.path):
            raise FileExistsError("文件路径不存在")
        # 将数据写入文件中,已追加形式写入文件
        with open(self.path, 'a') as fp:
            print("开始写入失败样本")
            # 加上\n换行写入数据
            url=u = 'https://phyllis.nl/Biomass/AjaxView/' + data
            fp.write('样品：{}，url：{}'.format(str(data),url)+'\n')
        fp.close()

if __name__ == "__main__":                 #进行测试
    test_data = 'this is a test, save it'
    save_path = 'E:\\code\\file.txt'
    ds = FailedSample(save_path)
    ds.save(test_data)
