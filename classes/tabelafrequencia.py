import numpy as np
import pandas as pd

class TabelaFrequencia:

    def regraDeSturges(self, n):
        return int(np.ceil(1 + 3.3322 * np.log10(n)))

    def amplitudeTotal(self, coluna): 
        return coluna.max() - coluna.min()
    
    def amplitudeDeClasse(self, amplitudetotal, qtdclasses):
        return max(1, int(np.round(amplitudetotal / qtdclasses)))
    
    def gerarBinsLabels(self, lista, qtdClasse):
        amplitude_total = self.amplitudeTotal(lista)
        amplitude_classe = self.amplitudeDeClasse(amplitude_total, qtdClasse)

        valor = lista.min()
        bins = [valor]
        labels = []

        for i in range(qtdClasse):
            inicio = valor
            valor += amplitude_classe
            bins.append(valor)
            labels.append(f'{inicio}-{valor}')

        # bin[-1] = lista.max()

        return bins, labels
    
    def dadosAgrupadosPorClasse(self, data, colunaNome):
        lista = data[colunaNome].copy().sort_values()
        regrasturges = self.regraDeSturges(lista.count())
        bins, labels = self.gerarBinsLabels(lista, regrasturges)
        newdata = data.copy()
        newdata['Agrupado'] = pd.cut(data[colunaNome], bins= bins, labels= labels)
        return newdata