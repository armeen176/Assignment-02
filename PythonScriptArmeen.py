import pandas as pd

# Import CSV data
data = pd.read_csv(r"C:\Users\Fine Traders\Downloads\study_performance_armeen.csv")

# Preview dataset
print("\nPreview (First 10 rows):\n", data.head(10))
print("\nData Types by Column:\n", data.dtypes)

# Identify categorical features
categorical_features = data.select_dtypes(include=["object"]).columns
for feature in categorical_features:
    print(f"Count of unique values in '{feature}':", data[feature].nunique())

# Remove missing entries and format column names
data = data.dropna()
data.columns = [name.strip().lower().replace(" ", "_") for name in data.columns]

# Analyze score columns
score_fields = ["reading_score", "writing_score", "cgpa"]
for field in score_fields:
    mean_val = data[field].mean()
    min_val = data[field].min()
    max_val = data[field].max()
    std_dev = data[field].std()
    print(f"\nStatistics for {field}: Mean={mean_val:.2f}, Min={min_val}, Max={max_val}, StdDev={std_dev:.2f}")

# Filter students with high performance
high_achievers = data[
    (data["reading_score"] > 90) & 
    (data["writing_score"] > 90) & 
    (data["cgpa"] > 90)
]
print("\nHigh-performing students (scores > 90):\n", high_achievers)

# Sort dataset based on writing scores
ranked_by_writing = data.sort_values(by="writing_score", ascending=False)
print("\nTop students by writing score:\n", ranked_by_writing.head())

# Note: Grouping operations skipped as 'gender' and 'test_preparation_course' fields are absent

# Add derived column for average score
data["overall_score"] = data[score_fields].mean(axis=1)

# Define performance grading function
def assign_level(score):
    if score >= 90:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 50:
        return "Average"
    else:
        return "Poor"

# Apply grading function to dataset
data["grade_category"] = data["overall_score"].apply(assign_level)
print("\nUpdated DataFrame with performance grading:\n", data.head())
