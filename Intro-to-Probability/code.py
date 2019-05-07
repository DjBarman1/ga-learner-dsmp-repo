# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=pd.read_csv(path)
p_a=len(df[df['fico']>700]['fico'])/len(df['fico'])
p_b=len(df[df['purpose']== 'debt_consolidation']['purpose'])/len(df['purpose'])
df1=df[df['purpose']== 'debt_consolidation']
p_a_b=(p_b*p_a)/p_a
result=p_a_b == p_a
print(result)






# code ends here


# --------------
# code starts here




#prob_lp=len(df[df['paid.back.loan']=='Yes']['paid.back.loan'])/len(df['paid.back.loan'])
prob_lp=df[df['paid.back.loan']=='Yes'].shape[0]/df.shape[0]
print(prob_lp)
#prob_cs=len(df[df['credit.policy']=='Yes']['credit.policy'])/len(df['credit.policy'])
prob_cs=df[df['credit.policy']=='Yes'].shape[0]/df.shape[0]
print(prob_cs)
new_df=df[df['paid.back.loan'] == 'Yes']
prob_pd_cs=new_df[new_df['credit.policy']=='Yes'].shape[0]/new_df.shape[0]
bayes=prob_pd_cs *prob_lp/prob_cs
print(bayes)



# code ends here


# --------------
# code starts here
df.purpose.value_counts(normalize=True).plot(kind='bar')
df1=df[df['paid.back.loan'] == 'No']
df1.purpose.value_counts(normalize=True).plot(kind='bar')




# code ends here


# --------------
# code starts here
inst_median=df['installment'].median
inst_mean=df['installment'].mean
plt.hist(df['installment'])
plt.hist(df['log.annual.inc'])


# code ends here


