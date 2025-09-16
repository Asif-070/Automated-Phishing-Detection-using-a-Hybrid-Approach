import pandas as pd

# Load dataset
df = pd.read_excel("combined.xlsx", header=None)
df.columns = ["label", "html" ,"url"]

# Take next 10000 (rows 10000–19999) from each class
df_0 = df[df["label"] == 0].iloc[18000:23000]
df_1 = df[df["label"] == 1].iloc[18000:23000]

# Combine
balanced_df = pd.concat([df_0, df_1])

# (Optional) Shuffle
balanced_df = balanced_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save
balanced_df.to_excel("combined_d3.xlsx", index=False)
