import pickle

# Função para salvar modelos e resultados
def save_results(model, results, filename_model, filename_results):
    with open(filename_model, 'wb') as model_file:
        pickle.dump(model, model_file)
    with open(filename_results, 'wb') as results_file:
        pickle.dump(results, results_file)

def load_results(filename_model, filename_results):
    with open(filename_model, 'rb') as model_file:
        model = pickle.load(model_file)
    with open(filename_results, 'rb') as results_file:
        results = pickle.load(results_file)
    return model, results