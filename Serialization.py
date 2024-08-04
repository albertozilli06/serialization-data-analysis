import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Simulate Serialization Data
np.random.seed(42)  # For reproducibility

# Simulating data
num_records = 1000
serial_numbers = np.arange(1, num_records + 1)
timestamps = pd.date_range(start='2023-01-01', periods=num_records, freq='H')
locations = np.random.choice(['Factory A', 'Factory B', 'Factory C'], size=num_records)
status = np.random.choice(['produced', 'shipped', 'returned'], size=num_records, p=[0.7, 0.25, 0.05])

# Create a DataFrame
data = pd.DataFrame({
    'serial_number': serial_numbers,
    'timestamp': timestamps,
    'location': locations,
    'status': status
})

# Step 2: Data Analysis
# Calculate the number of products produced, shipped, and returned
status_counts = data['status'].value_counts()
print(status_counts)

# Calculate production over time
production_over_time = data[data['status'] == 'produced'].groupby(data['timestamp'].dt.date).size()

# Step 3: Data Visualization
# Status Counts
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='status', order=status_counts.index)
plt.title('Product Status Distribution')
plt.xlabel('Status')
plt.ylabel('Count')
plt.show()

# Production Over Time
plt.figure(figsize=(12, 6))
production_over_time.plot(kind='line', marker='o')
plt.title('Production Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Products Produced')
plt.grid(True)
plt.show()

# Production by Location
plt.figure(figsize=(10, 6))
sns.countplot(data=data[data['status'] == 'produced'], x='location')
plt.title('Production by Location')
plt.xlabel('Location')
plt.ylabel('Number of Products Produced')
plt.show()

# Analysis of returned products over time
returned_over_time = data[data['status'] == 'returned'].groupby(data['timestamp'].dt.date).size()
plt.figure(figsize=(12, 6))
returned_over_time.plot(kind='bar')
plt.title('Returned Products Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Returned Products')
plt.grid(True)
plt.show()
