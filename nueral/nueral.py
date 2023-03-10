import pandas as pd
from keras import Sequential
from keras.layers import InputLayer, Dense
from sklearn.model_selection import train_test_split
import tensorflow

df = pd.read_csv('diabetes.csv')
train_df, test_df = train_test_split(df, test_size=0.20)

train_df = pd.DataFrame(train_df)
train_x = train_df.drop(columns=["Outcome"], axis=1)
train_y = train_df['Outcome']

# build the model
model = Sequential()
model.add(InputLayer(input_shape=train_x.shape[1]))  # 8, 1
model.add(Dense(1, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(train_x, train_y, epochs=20)
