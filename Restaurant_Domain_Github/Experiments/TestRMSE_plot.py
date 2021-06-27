import matplotlib.pyplot as plt
import pandas



alpha = 0.01
beta = 0.001
lamda1 = 0.0001
lamda2 = 0.005
K1 = 50

MF_Evaluation = [i.strip().split(",") for i in open("MF/Results/MF_Evaluation_"+str(K1)+"_alpha"+str(alpha)+"_beta"+str(beta)+"_first90train.csv", 'r').readlines()]
MF_Evaluation_df = pandas.DataFrame(MF_Evaluation, columns = ['M','K', 'Train RMSE', 'Test RMSE', 'Train MAE', 'Test MAE', 'MEP', 'MER', 'MAP', 'MAR', 'AUC', 'nDCG', 'F1-score', 'EF1-score'], dtype = int)

EMF_Evaluation = [i.strip().split(",") for i in open("EMF/Results/EMF_Evaluation_"+str(K1)+"_alpha"+str(alpha)+"_beta"+str(beta)+"_first90train.csv", 'r').readlines()]
EMF_Evaluation_df = pandas.DataFrame(EMF_Evaluation, columns = ['M','K', 'Train RMSE', 'Test RMSE', 'Train MAE', 'Test MAE', 'MEP', 'MER', 'MAP', 'MAR', 'AUC', 'nDCG', 'F1-score', 'EF1-score'], dtype = int)

FBEMF_Evaluation = [i.strip().split(",") for i in open("FBEMF/Results/FBEMF_Evaluation_"+str(K1)+"_alpha"+str(alpha)+"_beta"+str(beta)+"_first90train.csv", 'r').readlines()]
FBEMF_Evaluation_df = pandas.DataFrame(FBEMF_Evaluation, columns = ['M','K', 'Train RMSE', 'Test RMSE', 'Train MAE', 'Test MAE', 'MEP', 'MER', 'MAP', 'MAR', 'AUC', 'nDCG', 'F1-score', 'EF1-score'], dtype = int)
a = []
b = []
c = []
k = []


for i in range(1,len(MF_Evaluation_df['Test RMSE'])):
    a.append(float(MF_Evaluation_df['Test RMSE'][i]))

for i in range(1,len(MF_Evaluation_df['K'])):
    k.append(float(MF_Evaluation_df['K'][i]))

for i in range(1,len(EMF_Evaluation_df['Test RMSE'])):
    b.append(float(EMF_Evaluation_df['Test RMSE'][i]))

for i in range(1,len(FBEMF_Evaluation_df['Test RMSE'])):
    c.append(float(FBEMF_Evaluation_df['Test RMSE'][i]))

plt.figure()
lw = 1
plt.plot(k,a, 's-' , color='darkorange', lw=lw, label='MF')
plt.plot(k,b, '^-' , color='red', lw=lw, label='EMF')
plt.plot(k,c, 'D-' , color='lightgreen', lw=lw, label='FBEMF')
plt.xlabel('Factors (K)')
plt.ylabel('RMSE')
#plt.title('Test RMSE'+' alpha'+str(alpha)+' beta'+str(beta))
plt.title('Test RMSE')
plt.legend(bbox_to_anchor=(0.87, 1), loc=2, borderaxespad=0)
plt.legend(loc="upper left")
plt.savefig('Figures/Test RMSE.jpg')
plt.show()