**本程序运行环境：`python3.5.4`**

**说明：**
从网站下载的LeaRun敏捷后台开发框架_6.3.4
将相关文件整合到`django`框架中,版本为2.0.7

整合花了大量时间,菜单一直没搞出来。后来才发现index.js有问题，修改了一下！
注意：左侧的菜单已经集成到index.html中

如果需要删除无用的，请修改index.js

运行方式：使用Pycharm直接运行即可。

或者使用命令
`python manage.py runserver`

备注：

这是一个空的后台模板，自带多选项卡效果(重点)。

网上找了好多后台模板，很多都没有带多选项卡的。
即使有的，整合到django框架，非常麻烦！

只有LeaRun框架，整合才比较简单！特别是多选项卡效果。

首页有一些图表,我给删除了。需要用的话，推荐使用Highcharts
参考链接
http://www.py3study.com/Article/details/id/317.html

效果如下：

![Image text](https://github.com/py3study/bmt/blob/master/效果图.png)