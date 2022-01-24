# notice-list
学工网通知爬取
写这个项目的原因是因为川农的学工网通知不能搜素，令人吐槽的是与之相对的教务处和学院的通知都可以搜索。<(＿　＿)>

正好在练习python的爬虫，就写了个小东西，那一堆混乱的文件可以不用看了，初次操作不太熟练，可以直接下载编译好的版本。https://github.com/moonmusicstone/notice-list/releases/tag/python

因为学工网通知用了JS跳转下一页，不同页面的url是相同的，所以使用 WebDriver 自动Microsoft Edge进行跳转，所以请确保下载压缩包解压后 msedgedriver.exe 和 通知爬取.exe 在同一路径下，不然会报错。

如果想要看源码的话 final.py 是最终的版本，其他的请忽略。(●'◡'●)链接放到下面了：
https://github.com/moonmusicstone/notice-list/blob/master/PythonApplication3/final.py
