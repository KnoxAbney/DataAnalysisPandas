from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')

df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']

sns.set_style('whitegrid')
sns.set_context('poster', font_scale = 0.6)

fig, ax = plt.subplots(figsize = (15,7))

ax = sns.barplot(data = df, x = 'Year', y = 'Total Goals')
ax.set_title('Average World Cup Goals per Game by Year')

plt.show()


df_goals = pd.read_csv('goals.csv')

sns.set_context('notebook', font_scale = 1.25)

fig, ax2 = plt.subplots(figsize = (15,7))
ax2 = sns.boxplot(data = df_goals, x = 'year', y = 'goals', palette = 'Spectral')
ax2.set_title('World Cup Goals per Game by Year')

plt.show()


dfg = df[['Year', 'Total Goals']]

sns.set_context('talk', font_scale = .8)
fig, ax3 = plt.subplots(figsize = (15,7))
ax3.set_title('World Cup Goals By Year')

sns.violinplot(data = dfg, x = 'Year', y = 'Total Goals', palette = 'pastel')
plt.show()
