import pandas as pd

# Carregar os dados do MIT-BIH
mitbih_train = pd.read_csv('mitbih_train.csv', header=None)
mitbih_test = pd.read_csv('mitbih_test.csv', header=None)

# Combinar os dados de treino e teste
mitbih_data = pd.concat([mitbih_train, mitbih_test], axis=0)

# Exibir as primeiras linhas da base de dados
print(mitbih_data.head())

# Verificar a distribuição das classes
print(mitbih_data.iloc[:, -1].value_counts())

