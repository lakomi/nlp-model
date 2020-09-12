# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：nlp-model -> myUtils
@IDE    ：PyCharm
@Author ：qs
@Date   ：2020/9/12 17:32
@Desc   ：
=================================================='''


def getNums(target_list, pred_list, label):
    """
    得到相应类别的三个数。
    :param target_list: 目标结果列表
    :param pred_list: 预测结果列表
    :param label: 类别
    :return: 真正预测对的数量、预测结果是“对”的数量、所有结果是“对”的数量
    """

    right_num, pred_right_num, target_right_num = 0, 0, 0

    # 根据label，遍历求个数。
    for i in range(len(target_list)):
        if target_list[i] == label:
            target_right_num += 1
            if target_list[i] == pred_list[i]:
                right_num += 1
        if pred_list[i] == label:
            pred_right_num += 1
    return right_num, pred_right_num, target_right_num
