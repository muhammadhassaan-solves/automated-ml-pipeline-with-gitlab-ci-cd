import os
import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Make sure 'model' directory exists
os.makedirs('model', exist_ok=True)

# Save the trained model inside 'model' folder
with open('model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved to model/model.pkl")
