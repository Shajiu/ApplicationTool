# -*- coding: utf-8 -*-
# @Author  : Shajiu
# @FileName: data.py
# @Time    : 2021/8/22 17:19
import json

class SourceDataDemo:

    def __init__(self):
        self.title = '甘肃省甘南州大数据云计算微服务平台中心'      #大数据可视化展板通用模板
        self.counter = {'name': '2021年总收入情况', 'value': 12581189}
        self.counter2 = {'name': '2021年总支出情况', 'value': 3912410}
        self.echart1_data = {
            'title': '2021年部门预算',
            'data': [
                {"name": "项目支出", "value": 500000},
                {"name": "公共服务", "value": 2076941},
                {"name": "社会保障", "value": 311289},
                {"name": "医疗卫生", "value": 110466},
                {"name": "工资福利", "value": 1564109.27},
                {"name": "商品服务", "value": 1564109.27},
                {"name": "政府购买", "value": 5000000},
            ]
        }
        self.echart2_data = {
            'title': '人口数量',
            'data': [
                {"name": "合作市", "value": 112173},
                {"name": "夏河县", "value": 86355},
                {"name": "玛曲县", "value": 57076},
                {"name": "碌曲县", "value": 35871},
                {"name": "迭部县", "value": 52192},
                {"name": "卓尼县", "value": 95387},
                {"name": "临潭县", "value": 127387},
                {"name": "舟曲县", "value": 125367},
            ]
        }
        self.echarts3_1_data = {
            'title': '年龄分布',
            'data': [
                {"name": "0-14岁", "value": 154681},
                {"name": "15-59岁", "value": 450363},
                {"name": "60岁及以上", "value": 86764}
            ]
        }
        self.echarts3_2_data = {
            'title': '受教育程度',
            'data': [
                {"name": "大学文化", "value": 100432},
                {"name": "高中文化", "value": 51155},
                {"name": "初中文化", "value": 97493},
                {"name": "小学文化", "value": 301641}
            ]
        }
        self.echarts3_3_data = {
            'title': '城乡人口',
            'data': [
                {"name": "城镇", "value": 292435},
                {"name": "乡村", "value": 399373}
            ]
        }
        self.echart4_data = {
            'title': '时间趋势',
            'data': [
                {"name": "安卓", "value": [3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 4]},
                {"name": "IOS", "value": [5, 3, 5, 6, 1, 5, 3, 5, 6, 4, 6, 4, 8, 3, 5, 6, 1, 5, 3, 7, 2, 5, 8]},
            ],
            'xAxis': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '11', '12', '13', '14', '15', '16', '17',
                      '18', '19', '20', '21', '22', '23', '24'],
        }
        self.echart5_data = {
            'title': '市县级TOP',
            'data': [
                {"name": "合作市", "value": 2},
                {"name": "夏河县", "value": 3},
                {"name": "卓尼县", "value": 3},
                {"name": "临潭县", "value": 9},
                {"name": "玛曲县", "value": 15},
                {"name": "迭部县", "value": 18},
                {"name": "舟曲县", "value": 20},
                {"name": "碌曲县", "value": 13},
            ]
        }
        self.echart6_data = {
            'title': '区域面积占比',
            'data': [
                {"name": "合作市", "value": 2670, "value2": 20, "color": "01", "radius": ['59%', '70%']},
                {"name": "夏河县", "value": 6274, "value2": 30, "color": "02", "radius": ['49%', '60%']},
                {"name": "卓尼县", "value": 5694, "value2": 35, "color": "03", "radius": ['39%', '50%']},
                {"name": "玛曲县", "value": 10191, "value2": 40, "color": "04", "radius": ['29%', '40%']},
                {"name": "临潭县", "value": 1557.5, "value2": 50, "color": "05", "radius": ['20%', '30%']},
                {"name": "碌曲县", "value": 5299, "value2": 50, "color": "05", "radius": ['20%', '30%']},
                {"name": "迭部县", "value": 5108, "value2": 50, "color": "05", "radius": ['20%', '30%']},
                {"name": "舟曲县", "value": 3010, "value2": 50, "color": "05", "radius": ['20%', '30%']},
            ]
        }
        '''--------------------------------------------------'''
        self.map_1_data = {
            'symbolSize': 100,
            'data': [
                {'name': '海门', 'value': 239},
                {'name': '鄂尔多斯', 'value': 231},
                {'name': '招远', 'value': 203},
            ]
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        echart = {
            'symbolSize': data.get('symbolSize'),
            'data': data.get('data'),
        }
        return echart


class SourceData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        self.title = '甘肃省甘南州大数据云计算微服务平台中心'

class CorpData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        with open('corp.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        self.title = data.get('title')
        self.counter = data.get('counter')
        self.counter2 = data.get('counter2')
        self.echart1_data = data.get('echart1_data')
        self.echart2_data = data.get('echart2_data')
        self.echarts3_1_data = data.get('echarts3_1_data')
        self.echarts3_2_data = data.get('echarts3_2_data')
        self.echarts3_3_data = data.get('echarts3_3_data')
        self.echart4_data = data.get('echart4_data')
        self.echart5_data = data.get('echart5_data')
        self.echart6_data = data.get('echart6_data')
        self.map_1_data = data.get('map_1_data')

class JobData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        with open('job.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        self.title = data.get('title')
        self.counter = data.get('counter')
        self.counter2 = data.get('counter2')
        self.echart1_data = data.get('echart1_data')
        self.echart2_data = data.get('echart2_data')
        self.echarts3_1_data = data.get('echarts3_1_data')
        self.echarts3_2_data = data.get('echarts3_2_data')
        self.echarts3_3_data = data.get('echarts3_3_data')
        self.echart4_data = data.get('echart4_data')
        self.echart5_data = data.get('echart5_data')
        self.echart6_data = data.get('echart6_data')
        self.map_1_data = data.get('map_1_data')