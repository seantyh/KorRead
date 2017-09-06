from keras.models import Sequential, Model
from keras.layers import Input, Dense, Flatten, 
from keras.layers import Embedding
from keras.layers import MaxPooling1D, Conv1D

def setup_model(embed_mat):
    # define input layers
    input_text = Input(shape=(None, ), name="input_text")

    # embedding layers for text
    vocab_size = embed_mat.shape[0]
    embed_dim = embed_mat.shape[1]
    embed = Embedding(vocab_size, embed_dim,
                weights=[embed_mat], 
                trainable=False)(input_text)
    

    x = Conv1D(72, 5, activation="relu")(embed)
    x = MaxPooling1D(5)(x)
    x = Conv1D(72, 5, activation="relu")(embed)
    x = MaxPooling1D(5)(x)
    x = Conv1D(72, 5, activation="relu")(embed)
    x = MaxPooling1D(20)(x)
    x = Flatten()(x)
    x = Dense(128, activation='relu')(x)
    pred = Dense(6, activation="softmax")(x)

    model  = Model(input_text, preds)
    model.compile(optimizer = 'rmsprop', 
                loss="categorical_crossentropy", 
                metrics = ["accuracy"])
    
    return model
