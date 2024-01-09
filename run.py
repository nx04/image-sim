# encoding: utf-8
"""
@author: xiao nian
@contact: xiaonian030@163.com
@date: 2024-01-08
"""
__copyright__ = "Copyright (c) (2022-2024) XN Inc. All Rights Reserved"
__author__ = "Xiao Nian"
__date__ = "2024-01-09 11:54:24"
__version__ = "1.0.0"
from service.cosine_similarity import get_similarity

if __name__ == '__main__':
    print('>> 程序加载完成！')

    image_url_one = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fsafe-img.xhscdn.com%2Fbw%2Fd9dfbe33-1723-4d31-8c84-38b689e01d08%3FimageView2%2F2%2Fw%2F1080%2Fformat%2Fjpg&refer=http%3A%2F%2Fsafe-img.xhscdn.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1707369761&t=7d38e1c02e10085974a88806de9ea5a3'

    image_url_two = 'https://img1.baidu.com/it/u=3389309954,3901885263&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=667'

    sim = get_similarity(image_url_one, image_url_two)
    print('两张图片的相似度：', sim)