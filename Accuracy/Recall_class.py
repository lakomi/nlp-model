# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：nlp-model -> Recall_class
@IDE    ：PyCharm
@Author ：qs
@Date   ：2020/9/12 16:34
@Desc   ：
=================================================='''


class Recall:
    def __init__(self, right_num=0., tar_right_num=0.):
        """
        查全率
        :param right_num: 真正预测对的数量
        :param target_right_num:目标结果是“对”的数量
        """
        self.right_num = right_num
        self.tar_right_num = tar_right_num

        if self.tar_right_num != 0:
            self.R = self.right_num / self.tar_right_num
        else:
            self.R = 0
