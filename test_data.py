import pandas as pd

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Check dataset is not empty
assert len(df) > 0

# Check target column exists
assert "Attrition" in df.columns

print("All tests passed!")
