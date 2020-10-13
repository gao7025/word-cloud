# -*- coding: utf-8 -*-

from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt


class drawWordcloud():
    def __init__(self):
        pass
    def draw_wordcloud(self,comment_text):
        cut_text = " ".join(jieba.cut(comment_text)) # 结巴分词，生成字符串
        cloud = WordCloud(
            font_path=r'C:\Windows\Fonts\simhei.ttf', #设置字体，本次使用Windows自带的黑体字
            background_color='white',# 设置背景色
            # mask=color_mask, # 词云形状
            max_words=500, # 允许最大词汇
            max_font_size=100, # 最大号字体
            min_font_size=5, # 最小号字体
            # random_state=20, # 设置有多少种随机生成状态，即有多少种配色方案
            width=800,  # 生成图片的大小
            height=600,
        )
        word_cloud = cloud.generate(cut_text)
        word_cloud.to_file("my_cloud.jpg")
        # 显示图片
        plt.imshow(word_cloud)
        plt.axis('off')
        plt.show()

    def domain(self):
        comment_text = open(r'E:\programGao\wordcloud_test\gov_report.txt','r',encoding='utf-8').read()
        self.draw_wordcloud(comment_text)


if __name__ == '__main__':
    drawWordcloud().domain()