# encoding: utf-8
"""
图片处理
@author: xiao nian
@contact: xiaonian030@163.com
@date: 2024-01-09 12:50
"""

__copyright__ = "Copyright (c) (2022-2024) XN Inc. All Rights Reserved"
__author__ = "Xiao Nian"
__date__ = "2024-01-09 12:50:24"
__version__ = "1.0.0"

from my_fake_useragent import UserAgent
import requests
import numpy as np
import cv2
from numpy import average, dot, linalg


def get_image_stream(image_url):
    """
    获取在线图片流数据
    """
    ua = UserAgent(family='chrome')
    headers = {"User-Agent": ua.random()}
    response = requests.request(
        method='GET',
        url=image_url,
        headers=headers,
        stream=True)
    if response.status_code == 200:
        return response.content
    else:
        return ''


def get_image_array(image_stream, shape, gray=True):
    image_array = np.asarray(bytearray(image_stream), dtype="uint8")
    image_code = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # 缩放
    image_resize = cv2.resize(image_code, shape)

    if gray:
        # 转换为灰度图
        image_gray_value = cv2.cvtColor(image_resize, cv2.COLOR_BGR2GRAY)
    else:
        image_gray_value = image_resize

    return image_gray_value


def get_similarity_by_array(image_array_one, image_array_two):
    image_array = [image_array_one, image_array_two]
    vectors = []
    norms = []
    for image in image_array:
        vector = []
        for pixel_tuple in image:
            vector.append(average(pixel_tuple))
        vectors.append(vector)

        # linalg=linear（线性）+algebra（代数），norm则表示范数
        # 求图片的范数
        norms.append(linalg.norm(vector, 2))

    a, b = vectors
    a_norm, b_norm = norms

    # dot返回的是点积，对二维数组（矩阵）进行计算
    similar = dot(a / a_norm, b / b_norm)
    return similar


def get_similarity(url_one, url_two, gray=True):
    stream_one = get_image_stream(url_one)
    image_array_one = get_image_array(stream_one, (500, 500), gray)

    stream_two = get_image_stream(url_two)
    image_array_two = get_image_array(stream_two, (500, 500), gray)

    sim = get_similarity_by_array(image_array_one, image_array_two)
    return sim

if __name__ == '__main__':
    print('check！')
    image_url_one = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fsafe-img.xhscdn.com%2Fbw%2Fd9dfbe33-1723-4d31-8c84-38b689e01d08%3FimageView2%2F2%2Fw%2F1080%2Fformat%2Fjpg&refer=http%3A%2F%2Fsafe-img.xhscdn.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1707369761&t=7d38e1c02e10085974a88806de9ea5a3'

    image_url_two = 'https://img1.baidu.com/it/u=3389309954,3901885263&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=667'

    sim = get_similarity(image_url_one, image_url_two)
    print('两张图片的相似度：', sim)

