import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable


def judge_classifier_282(data):
    print('Results of ' + data)
    x = PrettyTable()
    x.field_names = ['conf_thresh', 'data', 'DC', 'UTC', 'mAP', 'TP', 'FP', 'FN', 'IoU', 'precision', 'recall', 'F1']

    conf_thresh = [0.25, 0.1, 0.08, 0.07, 0.04]
    DC = 24030
    UTC = 8819
    mAP = 80.97
    TP = [5939, 7035, 7181, 7260, 7519]
    FP = [774, 1976, 2356, 2638, 3945]
    FN = [2880, 1784, 1638, 1559, 1300]
    IoU = [65.77, 57.52, 55.45, 53.98, 48.13]

    for i in range(len(conf_thresh)):
        TN = DC - (TP[i] + FP[i] + FN[i])
        TPR = TP[i] / (TP[i] + FN[i])
        FPR = FP[i] / (FP[i] + TN)
        precision = round(TP[i] / (TP[i] + FP[i]), 2)
        recall = round(TP[i] / (TP[i] + FN[i]), 2)
        F1 = round(2 * precision * recall / (precision + recall), 2)
        # FP[i] = round(FP[i]/DC, 2)
        # FN[i] = round(FN[i]/UTC, 2)
        judge = [conf_thresh[i], data, DC, UTC, mAP, TP[i], FP[i], FN[i], IoU[i], precision, recall, F1]
        x.add_row(judge)

    print(x)


def judge_classifier_43(data):
    print('Results of ' + data)
    x = PrettyTable()
    x.field_names = ['conf_thresh', 'data', 'DC', 'UTC', 'mAP', 'TP', 'FP', 'FN', 'IoU', 'precision', 'recall', 'F1']

    conf_thresh = [0.25, 0.1, 0.08, 0.07, 0.06, 0.05, 0.04]
    DC = 13014
    UTC = 8819
    mAP = 78.35
    TP = [3951, 5911, 6202,6336, 6488, 6667, 6840]
    FP = [338, 799, 941, 1027, 1158, 1300, 1518]
    FN = [4868, 2908, 2617, 2483, 2331, 2152, 1979]
    IoU = [70.02, 66.71, 65.63, 64.97, 63.98, 63.00, 61.53]

    for i in range(len(conf_thresh)):
        TN = DC - (TP[i] + FP[i] + FN[i])
        TPR = TP[i] / (TP[i] + FN[i])
        FPR = FP[i] / (FP[i] + TN)
        precision = round(TP[i] / (TP[i] + FP[i]), 2)
        recall = round(TP[i] / (TP[i] + FN[i]), 2)
        F1 = round(2 * precision * recall / (precision + recall), 2)
        # FP[i] = round(FP[i] / DC, 2)
        # FN[i] = round(FN[i] / UTC, 2)
        judge = [conf_thresh[i], data, DC, UTC, mAP, TP[i], FP[i], FN[i], IoU[i], precision, recall, F1]
        x.add_row(judge)

    print(x)


judge_classifier_282('train282')
judge_classifier_43('train43')
