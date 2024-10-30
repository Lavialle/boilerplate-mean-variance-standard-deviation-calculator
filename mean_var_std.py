import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    tab = np.array(list)
    tab = np.reshape(tab, (3,3))
    calculations = {}
    calculations['mean'] = [np.mean(tab, axis = 0).tolist(), np.mean(tab, axis = 1).tolist(), np.mean(tab).tolist()]
    calculations['variance'] = [np.var(tab, axis = 0).tolist(), np.var(tab, axis = 1).tolist(), np.var(tab).tolist()]
    calculations['standard deviation'] = [np.std(tab, axis = 0).tolist(), np.std(tab, axis = 1).tolist(), np.std(tab).tolist()]
    calculations['max'] = [np.max(tab, axis = 0).tolist(), np.max(tab, axis = 1).tolist(), np.max(tab).tolist()]
    calculations['min'] = [np.min(tab, axis = 0).tolist(), np.min(tab, axis = 1).tolist(), np.min(tab).tolist()]
    calculations['sum'] = [np.sum(tab, axis = 0).tolist(), np.sum(tab, axis = 1).tolist(), np.sum(tab).tolist()]
    return calculations