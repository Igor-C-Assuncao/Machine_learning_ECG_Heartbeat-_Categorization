from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns

# Função para rodar o modelo várias vezes e calcular métricas
def run_model(model, X_train, X_test, y_train, y_test, n_runs=15):
    precision_scores = []
    recall_scores = []
    f1_scores = []

    for _ in range(n_runs):
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        precision_scores.append(precision_score(y_test, y_pred, average='macro'))
        recall_scores.append(recall_score(y_test, y_pred, average='macro'))
        f1_scores.append(f1_score(y_test, y_pred, average='macro'))

    return precision_scores, recall_scores, f1_scores