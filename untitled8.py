# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j_H4CJugsNjltDN6FdOYH8KbKL_j0HW5
"""

from google.colab import files
upload=files.upload()

import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

df = pd.read_csv('Iris.csv')
df

#menghapus column yang tidak diperlukan
df = df.drop(columns='Id')

#Selanjutnya kita perlu melakukan one hot encoding karena label kita merupakan data kategorikal. Fungsi get_dummies() memudahkan kita untuk melakukan hal ini.
category = pd.get_dummies(df.Species)
category

#menggabungkan kolom hasil one hot encoding 
#membuang kolom spesies karena kolom tersebut sudah tidak terpakai

new_df = pd.concat([df, category], axis=1)
new_df = new_df.drop(columns= 'Species')
new_df

#konversi datafrmae menjadi numpy array dengan fungsi values data frame
dataset = new_df.values
dataset

#memisahkan atribut dan label
#plih 4 klom pertama untuk dijadikan sebagai atribut
x = dataset [:,0:4]
#pilih 3 kolom terakhir sebagai label 
y = dataset[:,4:7]

#normalisasi data agar dapat dipelajari dnegan baik oleh model
min_max_scaler = preprocessing.MinMaxScaler()
x_scale = min_max_scaler.fit_transform(x)
x_scale

#pembagian data menjadi data latih dan data uji, dengan ukuran data testing yang di gunakan 30%
X_train,X_test,Y_train, Y_test = train_test_split(x_scale, y, test_size= 0.3)

#membuar arsitektur model menggunakan 3 layer
model = Sequential([
                     Dense(64, activation='relu', input_shape=(4,)),    
                    Dense(64, activation='relu'),    
                    Dense(3, activation='softmax'),          
])

#menentukan optimize dan loss function dari model,
#untuk klasifikasi multi kelas bisa menggunakan loss 'categorical_crossentropy'
model.compile(optimizer='Adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

#fungsi fit() kita tampung kedalam objek hist(history)
hist = model.fit(X_train, Y_train, epochs=100)

#menguji akurasi presiksi model pada data uji
model.evaluate(X_test, Y_test)