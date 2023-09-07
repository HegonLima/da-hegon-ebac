# para gerar um grafico vou usar o seaborn e pra salavar o pyplot
import seaborn as sns
import matplotlib.pyplot as plt


#  para gerar grafico de barras uso o barplot com uma paleta pastel, pra mim uma game de cores bem suave de se apresentar
with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda", errorbar=None, palette="pastel")
  grafico.set(title='valor da gasolina por dia', xlabel='Dias', ylabel='Valor da gasolina');
  plt.savefig('gasolina.png')