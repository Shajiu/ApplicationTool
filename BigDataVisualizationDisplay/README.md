## BigDataVisualizationDisplay
数据大屏可视化

## 功能

便利性工具, 结构简单, 直接传数据就可以实现数据大屏

## 安装

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple flask
```

## 运行

```
cd big_screen;
python app.py;
```

* 甘肃省甘南州大数据云计算微服务平台中心 http://127.1.1.1:5000/        

* 迭部县大数据平台 http://127.1.1.1:5000/corp    

* 迭部县尼傲乡电商平台 http://127.1.1.1:5000/job    

## 示例

![Image text](https://github.com/Shajiu/Big-Data-Visualization-Display/blob/main/static/images/Deom.jpg)

## 使用

- 编辑 data.py 中的 SourceData 类（或者新增类，新增的话需要编辑 app.py 增加路由，请参考 CorpData/JobData）;
- 从任何地方读取你的数据，按照 SourceDataDemo 的数据格式，填充到 SourceData 类;
- 运行 python app.py 查看数据变更后的效果。
