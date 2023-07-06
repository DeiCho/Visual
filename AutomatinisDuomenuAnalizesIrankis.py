import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_data(file_path):
    data = pd.read_csv(file_path, encoding='utf-8')
    return data

def clean_data(data):
    # cleaned_data = data.drop_duplicates() #pasilna dublikatus
    # cleaned_data['amzius'] = cleaned_data['amzius'].astype(int)
    # cleaned_data['vardas'] = cleaned_data['vardas'].str.strip() #pasalina simblius
    # cleaned_data['pavarde'] = cleaned_data['pavarde'].str.replace(' ', '') #pakeicia tarpa i netarpa
    
    cleaned_data = data.dropna() #istrina tam tikras eilutes 

    return cleaned_data

def perform_calculation(data):
    calculations = {} #nustato dataFrame
    calculations['vidutinis amzius'] = data['amzius'].mean()
    calculations['age range'] = np.ptp(data['amzius']) # ptp iesko range (grazina skirtuma nuo didziausio iki maziausio)
    return calculations

def visualize_data(data):
    age_counts = data['amzius'].value_counts().sort_index()
    plt.figure(figsize=(10, 6)) 
    plt.bar(age_counts.index, age_counts.values)
    plt.xlabel('amzius')
    plt.ylabel('Amziaus daznumas')
    plt.title('Pasiskirstymas pagal amziu')
    plt.show()

def main():
    file_path = 'duomenys.csv'
    data = load_data(file_path)
    cleaned_data = clean_data(data)
    calculations = perform_calculation(cleaned_data)
    print('Skaiciavimai: ')
    for key, value in calculations.items():
        print(f'{key}: {value}')
    
    visualize_data(cleaned_data)

if __name__ == '__main__':
    main()