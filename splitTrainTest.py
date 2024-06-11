from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Função para pré-processamento
def preprocess_data(data):
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return train_test_split(X_scaled, y, test_size=0.2, random_state=42)

