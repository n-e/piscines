
import pandas as pd
import matplotlib.pyplot as plt

col_names = ['Date','Etablissement','Capacite','Fréquentation','Restant']

df = pd.read_csv(
    'data.tsv',
    sep='\t',
    header=None,
    na_values=['-'],
    parse_dates=['Date'],
    names=col_names)

df = df.pivot(index='Date',columns='Etablissement',values='Fréquentation')
df = df.filter(regex='Piscine|Centre')
print(df)

df = df.tz_localize('UTC')
df = df.tz_convert('Europe/Paris')


df.plot()
lgd = plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.savefig('graph.png', bbox_extra_artists=(lgd,), bbox_inches='tight')