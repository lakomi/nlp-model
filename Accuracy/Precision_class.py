# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：nlp-model -> Precission_class
@IDE    ：PyCharm
@Author ：qs
@Date   ：2020/9/12 16:34
@Desc   ：
=================================================='''


class Precision:
    def __init__(self, right_num=0., pred_right_num=0.):
        """
        查准率
        :param pred_right_num: 真正预测准确的数量
        :param pred_num: 预测结果是“对”的数量
        """
        self.right_num = right_num
        self.pred_right_num = pred_right_num

        if self.pred_right_num != 0:
            self.P = self.right_num / self.pred_right_num
        else:
            self.P = 0
