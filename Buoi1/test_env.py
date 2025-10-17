import numpy as np
import pandas as pd
import tensorflow as tf
import sklearn

print(f"NumPy version: {np.__version__}")

print(f"Pandas version: {pd.__version__}")
print(f"TensorFlow version: {tf.__version__}")
print(f"scikit-learn version: {sklearn.__version__}")

print("GPU Available: ", tf.config.list_physical_devices('GPU'))