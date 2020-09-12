# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：nlp-model -> main
@IDE    ：PyCharm
@Author ：qs
@Date   ：2020/9/12 16:34
@Desc   ：
=================================================='''
from Accuracy import Precision_class, Recall_class, FK_class, myUtils

if __name__ == "__main__":
    # evalList中记录所要求的P,R,F值。列分别代表P,R,F值，行代表不同类别的三个值
    evalList = [[0, 0, 0], [0, 0, 0]]
    target = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    predict = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0]

    nums = [list(myUtils.getNums(target, predict, 0)), list(myUtils.getNums(target, predict, 1))]
    k = 1
    for i in range(len(nums)):
        evalList[i][0] = Precision_class.Precision(nums[i][0], nums[i][1]).P
        evalList[i][1] = Recall_class.Recall(nums[i][0], nums[i][2]).R
        evalList[i][2] = FK_class.Fk(evalList[i][0], evalList[i][1], k).Fk
    print(evalList)
