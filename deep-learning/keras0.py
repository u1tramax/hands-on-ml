#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
from tensorflow import keras


# In[2]:


tf.__version__, keras.__version__


# In[3]:


fashion_mnist = keras.datasets.fashion_mnist
(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()


# In[4]:


# X_train_full.shape, X_train_full.dtype


# In[5]:


X_valid, X_train = X_train_full[:5000] / 255.0, X_train_full[5000:] / 255.0
y_valid, y_train = y_train_full[:5000], y_train_full[5000:]


# In[6]:


class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
"Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]


# In[7]:


# class_names[y_train[0]]


# In[8]:


model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),
    keras.layers.Dense(300, activation="relu"),
    keras.layers.Dense(100, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])


# In[9]:


# model.summary()


# In[10]:


# model.layers


# In[11]:


hidden1 = model.layers[1]


# In[12]:


# hidden1.name


# In[13]:


weights, biases = hidden1.get_weights()
# weights, biases


# In[ ]:


model.compile(loss="sparse_categorical_crossentropy",
    optimizer="sgd",
    metrics=["accuracy"]
)


# In[ ]:


history = model.fit(X_train, y_train, epochs=30,
    validation_data=(X_valid, y_valid)
)


# In[ ]:




