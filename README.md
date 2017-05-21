# md2blog
静态网站生成

## 主要功能
把markdown转换成网页形式
## 使用要求
1. markdown 文件名是 yyyy-MM-dd-filename.md 形式

## 使用方法
1. 在 config.py 中设置好 src_path 和 dest_path
2. 执行 `python convert.py`
3. 在 nginx 或 apache 中把 root 指向 dest_path

## todo 

首页,下一页链接
评论模块
