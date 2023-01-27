import numpy as np 

def importData():
    with open('7janvier.csv', newline='') as csvfile:
        jourCherche = list(csv.reader(csvfile))

    with open('eCO2mix_RTE_En-cours-TR_2.xls', newline='') as csvfile:
        data = list(csv.reader(csvfile))


    with open('RTE.xls', newline='') as csvfile:
        data2 = list(csv.reader(csvfile))

    data.append(data2)


def defineCorrelation(a1, a2):
    cor = np.corrcoef(a1,a2)
    maxcor = max(cor)

    