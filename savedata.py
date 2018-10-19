# savedata.py

import pickle



def save_obj():
    with open('save.pkl', 'wb+') as f:
        pickle.dump(charData, f, pickle.HIGHEST_PROTOCOL)

def load_obj():
    with open('save.pkl', 'rb') as f:
        return pickle.load(f)

charData = load_obj()

print(charData)

