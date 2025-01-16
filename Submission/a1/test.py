import pickle


with open('attrition_available_11.pkl', 'rb') as f:
    data = pickle.load(f)

print (data)