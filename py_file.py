import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def Corr_heatmap(data,title):
    '''
    This function will create a heatmap of correlation among features in data
    data: The dataframe that contains multiple features
    return:
    Heatmap of Correlation
    '''
    corr = data.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    plt.subplots(figsize=(11, 9))
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, vmin=-1, center=0,
            annot=True,square=True, linewidths=10, cbar_kws={"shrink": .5})
    plt.xticks(rotation=30, ha="right")
    plt.title(title)
    plt.show()

def pie_chart(data,label,title):
    '''
    This function create a pie chart for target data
    data: Target data, should be in numberical or percentage form
    and sum to 1
    Label: A series of strings that contains the names for each portion
    title(string): The title of the related pie chart
    return:
    pie chart
    '''
    colors = [ 'yellowgreen','gold', 'lightskyblue']
    plt.subplots(figsize=(5,5))
    plt.pie(data, labels=label, colors=colors,autopct='%1.2f%%',shadow=True)
    plt.legend(loc='upper right',bbox_to_anchor=(1, 0, 0.5, 1))
    plt.ylabel(None)
    plt.axis('equal')
    plt.title(title)
    plt.show()

if __name__ =="__main__":
    Corr_heatmap()
    pie_chart()