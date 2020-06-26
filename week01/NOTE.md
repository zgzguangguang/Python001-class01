学习笔记
1、手动爬取，不借助任何scrapy，用到的库是requests，不建议使用urllib库，解析网页用到的库是bs4,xpath
2、使用scrapy爬取，starturl开始，一层一层的爬取，借助items,pipeline保存爬取到的内容