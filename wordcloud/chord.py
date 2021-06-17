from cal import drug_names
import matplotlib.pyplot as plt

from wordcloud import WordCloud

drug_names = ' '.join(drug_names)
wordcloud = WordCloud(width=480, height=480, margin=0).generate(drug_names)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.savefig('wordcloud.png')
