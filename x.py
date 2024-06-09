import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Generate synthetic data
# Assume we have 1000 samples, each with 10 genetic markers (features)
import numpy as np

np.random.seed(42)
num_samples = 1000
num_features = 10

# Randomly generate genetic marker data
X = np.random.rand(num_samples, num_features)

# Randomly generate binary trait (0 or 1)
y = np.random.randint(0, 2, num_samples)

# Convert to DataFrame for convenience
data = pd.DataFrame(X, columns=[f'marker_{i}' for i in range(num_features)])
data['trait'] = y

# Display the first few rows of the dataset
print(data.head())
Step 3: Train the model
python
Copy code
# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data.drop(columns=['trait']), data['trait'], test_size=0.2, random_state=42)

# Initialize and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
Step 4: Predict the likelihood of a trait
python
Copy code
# Function to predict the likelihood of the trait
def predict_trait(genetic_markers):
    """
    Predict the likelihood of having the trait based on genetic markers.

    Parameters:
    genetic_markers (array-like): Array of genetic markers.

    Returns:
    float: Probability of having the trait.
    """
    prob = model.predict_proba([genetic_markers])[0][1]
    return prob

# Example usage
new_sample = np.random.rand(num_features)
likelihood = predict_trait(new_sample)
print(f'Likelihood of having the trait: {likelihood:.2f}')
Full Script
Combining all the steps, here's the complete script:

python
Copy code
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

# Generate synthetic data
np.random.seed(42)
num_samples = 1000
num_features = 10

X = np.random.rand(num_samples, num_features)
y = np.random.randint(0, 2, num_samples)

data = pd.DataFrame(X, columns=[f'marker_{i}' for i in range(num_features)])
data['trait'] = y

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data.drop(columns=['trait']), data['trait'], test_size=0.2, random_state=42)

# Initialize and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Function to predict the likelihood of the trait
def predict_trait(genetic_markers):
    prob = model.predict_proba([genetic_markers])[0][1]
    return prob

# Example usage
new_sample = np.random.rand(num_features)
likelihood = predict_trait(new_sample)
print(f'Likelihood of having the trait: {likelihood:.2f}')