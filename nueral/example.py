from keras.layers import InputLayer
from keras.layers import Dense
from keras.models import Sequential
from keras.losses import MSE
from keras.optimizers import SGD


model = Sequential()
model.add(InputLayer(input_shape=(2,)))  # input
model.add(Dense(5, activation='relu'))  # [2,1] * [1,5] + [1,5] = [5,1]
model.add(Dense(3, activation='relu'))  # [5,1] * [3,5] + [3] = [3,1]
model.add(Dense(2, activation='relu'))  # [1,3] * [3,2] + [1,2] = [1,2]
model.add(Dense(2, activation='sigmoid'))  # 0.74
opt = SGD(learning_rate=0.000001)

model.compile(loss=MSE, optimizer=opt)
