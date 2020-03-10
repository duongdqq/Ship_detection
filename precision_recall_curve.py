from prettytable import PrettyTable
import matplotlib.pyplot as plt

data = 'train43'
print('Results of ' + data)
x = PrettyTable()
x.field_names = ['conf_thresh', 'data', 'DC', 'UTC', 'mAP', 'TP', 'FP', 'FN', 'IoU', 'precision', 'recall', 'F1']
conf_thresh = [0.25, 0.1, 0.08, 0.07, 0.06, 0.05, 0.04]
DC = 13014
UTC = 8819
mAP = 78.35
TP = [3951, 5911, 6202, 6336, 6488, 6667, 6840]
FP = [338, 799, 941, 1027, 1158, 1300, 1518]
FN = [4868, 2908, 2617, 2483, 2331, 2152, 1979]
IoU = [70.02, 66.71, 65.63, 64.97, 63.98, 63.00, 61.53]
precision = []
recall = []
F1 = []

for i in range(len(conf_thresh)):
    TN = DC - (TP[i] + FP[i] + FN[i])
    TPR = TP[i] / (TP[i] + FN[i])
    FPR = FP[i] / (FP[i] + TN)
    precision.append(round(TP[i] / (TP[i] + FP[i]), 2))
    recall.append(round(TP[i] / (TP[i] + FN[i]), 2))
    F1.append(round(2 * precision[i] * recall[i] / (precision[i] + recall[i]), 2))
    judge = [conf_thresh[i], data, DC, UTC, mAP, TP[i], FP[i], FN[i], IoU[i], precision[i], recall[i], F1[i]]
    x.add_row(judge)


def average_precision():
    AP = 0
    for i in range(len(conf_thresh)-1, 0, -1):
        AP += (recall[i] - recall[i-1]) * precision[i]
    return AP


print(x)
print(average_precision())

