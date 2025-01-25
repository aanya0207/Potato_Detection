import tensorflow as tf

MODEL_PATH = "C:/Users/aanya/xyz/saved_models/Potato Detection/1.keras"
model = tf.keras.models.load_model(MODEL_PATH)
print("Model loaded successfully!")
