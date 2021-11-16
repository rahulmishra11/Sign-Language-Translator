import tensorflow as tf
import pandas as pd
import numpy as np
import tensorflow.keras as keras
import matplotlib.pyplot as plt

train = pd.read_csv("./sign_mnist_train/sign_mnist_train.csv")
test = pd.read_csv("./sign_mnist_test/sign_mnist_test.csv")

# put labels into y_train variable
Y_train = train["label"]
# Drop 'label' column
X_train = train.drop(labels = ["label"],axis = 1) 

# put labels into y_test variable
Y_test = test["label"]
# Drop 'label' column
X_test = test.drop(labels = ["label"],axis = 1)



# Normalize the data
X_train = X_train / 255.0
X_test = X_test / 255.0
print("x_train shape: ",X_train.shape)
print("x_test shape: ",X_test.shape)

#Reshape
X_train = X_train.values.reshape(-1,28,28,1)
X_test = X_test.values.reshape(-1,28,28,1)
print("x_train shape: ",X_train.shape)
print("x_test shape: ",X_test.shape)



plt.imshow(X_train[2],cmap='gray')
plt.title(train.iloc[10,0])
plt.axis("off")
plt.show()



model = keras.models.Sequential([
    keras.layers.Conv2D(filters=64, kernel_size=7, input_shape=[28, 28, 1]),
    keras.layers.MaxPooling2D(pool_size=2),
    keras.layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding="SAME"),
    keras.layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding="SAME"),
    keras.layers.MaxPooling2D(pool_size=2),
    keras.layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding="SAME"),
    keras.layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding="SAME"),
    keras.layers.MaxPooling2D(pool_size=2),
    keras.layers.Flatten(),
    keras.layers.Dense(units=128, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(units=64, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(units=25, activation='softmax'),
])

model.summary()

model.compile(
    loss="sparse_categorical_crossentropy",
    optimizer = 'nadam',
    metrics=['accuracy']
)

history = model.fit(X_train,Y_train,
                   epochs=10,)

pd.DataFrame(history.history).plot()

model.save("sign_mnist_train.h5")
print(model.evaluate(X_test,Y_test))