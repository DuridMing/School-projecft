import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import RandomFourierFeatures

def create_model():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(416 , 3)),
        # keras.Input(shape=(173056*3,) , batch_size=1),
        RandomFourierFeatures(
            output_dim=32,
            scale=10,
            kernel_initializer="Gaussian"
        ),
        # layers.Dense(units=10),
        # layers.Dense(392 , activation="relu"),
        
        layers.Dense(units=2),
    ])

    model.compile(
        optimizer=keras.optimizers.Adam(lr=0.01),
        # steps_per_epoch=1024,
        loss=keras.losses.hinge,
        metrics=[keras.metrics.CategoricalAccuracy(name="accuarcy")],
    )

    return model


def get_dataset(file_path, **kwargs):
    dataset = tf.data.experimental.make_csv_dataset(
        file_path,
        batch_size=1, # Artificially small to make examples easier to show.
        num_epochs=1,
        ignore_errors=True, 
        **kwargs)
    return dataset


'''
for MINIST
# Load MNIST
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# print("x = " , x_train , "y = ",  y_train)

# Preprocess the data by flattening & scaling it
x_train = x_train.reshape(-1, 784).astype("float32") / 255
x_test = x_test.reshape(-1, 784).astype("float32") / 255

# Categorical (one hot) encoding of the labels
y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)
'''

# CSV_COLUMNS = ['path','x','y','h','w','class']

# temp_dataset = SVM.get_dataset(
#     "test_xx_annotations_download_car_bus.csv",  column_names=CSV_COLUMNS , label_name="class")

# for batch, label in temp_dataset.take(1):
#     for key, value in batch.items():
#         print("{:20s}: {}".format(key, value.numpy()))
# print(temp_dataset['path'])

# print(dataset)
