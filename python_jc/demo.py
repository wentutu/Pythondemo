# -*- coding:utf-8 -*-
content = "我是中文"
content_unicode = content.decode("utf-8")
content_gbk = content_unicode.encode("gbk")
print content_gbk