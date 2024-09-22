import os
from enoppy.paper_based.pdo_2022 import *
from copy import deepcopy
import numpy as np
import warnings

warnings.filterwarnings("ignore")

PopSize = 100
DimSize = 10
LB = [-100] * DimSize
UB = [100] * DimSize

TrialRuns = 30
MaxFEs = 500 * DimSize
curFEs = 0

MaxIter = int(MaxFEs / PopSize)
curIter = 0

Pop = np.zeros((PopSize, DimSize))
FitPop = np.zeros(PopSize)

FuncNum = 0

BestFit = float("inf")
BestPop = None


# initialize the Pop randomly
def Initialization(func):
    global Pop, FitPop, curFEs, DimSize, BestPop, BestFit
    Pop = np.zeros((PopSize, DimSize))
    for i in range(PopSize):
        for j in range(DimSize):
            Pop[i][j] = LB[j] + (UB[j] - LB[j]) * np.random.rand()
        FitPop[i] = func(Pop[i])
    best_idx = np.argmin(FitPop)
    BestPop = deepcopy(Pop[best_idx])
    BestFit = FitPop[best_idx]


def CDEKI(func):
    global Pop, FitPop, curIter, MaxIter, LB, UB, PopSize, DimSize, curFEs, BestPop, BestFit
    Off = np.zeros((PopSize, DimSize))
    FitOff = np.zeros(PopSize)
    for i in range(PopSize):
        IDX = np.random.randint(0, PopSize)
        while IDX == i:
            IDX = np.random.randint(0, PopSize)
        candi = list(range(0, PopSize))
        candi.remove(i)
        candi.remove(IDX)
        r1, r2 = np.random.choice(candi, 2, replace=False)

        F1 = np.random.normal(0.5, 0.3)
        F2 = np.random.normal(0.5, 0.3)
        if FitPop[IDX] < FitPop[i]:  # DE/winner-to-best/1
            Off[i] = Pop[i] + F1 * (BestPop - Pop[i]) + F2 * (Pop[r1] - Pop[r2])
        else:
            Off[i] = Pop[IDX] + F1 * (BestPop - Pop[IDX]) + F2 * (Pop[r1] - Pop[r2])

        jrand = np.random.randint(0, DimSize)  # bin crossover
        for j in range(DimSize):
            Cr = np.random.normal(0.5, 0.3)
            if np.random.rand() < Cr or j == jrand:
                pass
            else:
                Off[i][j] = Pop[i][j]

        for j in range(DimSize):
            if Off[i][j] < LB[j] or Off[i][j] > UB[j]:
                Off[i][j] = np.random.uniform(LB[j], UB[j])

        FitOff[i] = func(Off[i])
        if FitOff[i] < FitPop[i]:
            Pop[i] = deepcopy(Off[i])
            FitPop[i] = FitOff[i]
            if FitOff[i] < BestFit:
                BestFit = FitOff[i]
                BestPop = deepcopy(Off[i])


def main():
    global FuncNum, DimSize, Pop, MaxFEs, curIter, MaxIter, LB, UB, BestFit
    Probs = [WBP(), PVP(), CSP(), SRD(), TBTD(), GTD(), CBD(), IBD(), TCD(), PLD(), CBHD(), RCB()]
    Names = ["WBP", "PVP", "CSP", "SRD", "TBTD", "GTD", "CBD", "IBD", "TCD", "PLD", "CBHD", "RCB"]
    for i in range(len(Probs)):
        DimSize = Probs[i].n_dims
        Pop = np.zeros((PopSize, DimSize))
        MaxFEs = 10000
        MaxIter = int(MaxFEs / PopSize)
        LB = Probs[i].lb
        UB = Probs[i].ub
        FuncNum = Names[i]
        All_Trial_Best = []
        for time in range(TrialRuns):
            Best_list = []
            curIter = 0
            np.random.seed(2024 + 7 * time)
            Initialization(Probs[i].evaluate)
            Best_list.append(BestFit)
            while curIter <= MaxIter:
                CDEKI(Probs[i].evaluate)
                curIter += 1
                Best_list.append(BestFit)
            All_Trial_Best.append(Best_list)
        np.savetxt("./CDE_Data/Engineer/" + str(FuncNum) + ".csv", All_Trial_Best, delimiter=",")


if __name__ == "__main__":
    if os.path.exists('./CDE_Data/Engineer') == False:
        os.makedirs('./CDE_Data/Engineer')
    main()
