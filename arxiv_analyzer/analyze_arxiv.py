import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df = pandas.read_json("arxiv_papers.json")
df = df[(df['originally_published_time'] > '2015-01-01') & (df['originally_published_time'] < '2017-05-06')]
df['published_year_time'] = df['originally_published_time'].dt.strftime('%Y%m').astype('int')

g = sns.countplot(x="published_year_time", data=df,color="salmon", saturation=.5)
g.tick_params(labelsize=9)
g.set(xlabel='Monat der Publikation', ylabel='Anzahl Dokumente')
g.set_title('Publikationen auf arXiv.org zum Theam "Text Summarization", (n={})'.format(len(df)))

for item in g.get_xticklabels():
    item.set_rotation(45)

#plt.show()
plt.savefig("chart.png",dpi=200,bbox_inches='tight')
#df[['published_year_time','tags', 'link', 'title']].to_csv("papers_in_chart.csv")