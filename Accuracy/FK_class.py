# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：nlp-model -> FK_class
@IDE    ：PyCharm
@Author ：qs
@Date   ：2020/9/12 17:13
@Desc   ：求F值
=================================================='''


class Fk:
    def __init__(self, P=0., R=0., k=1):
        """
        F值
        :param P:  precision
        :param R:  recall
        """
        self.P = P
        self.R = R
        self.k = k
        if (self.k * self.k) * self.P + self.R != 0:
            self.Fk = (1 + k) * self.P * self.R / ((self.k * self.k) * self.P + self.R)
        else:
            self.Fk = 0
