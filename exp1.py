import pandas as pd

df = pd.read_csv(r"C:\Users\Exam1\Desktop\ml datst.csv")



import matplotlib.pyplot as plt

plt.hist(df['temperature_celsius'])
plt.title("Temperature Distribution")
plt.show()

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.hist(df["temperature_celsius"], bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

import seaborn as sns

sns.heatmap(
    df[['temperature_celsius',
        'humidity',
        'pressure_mb',
        'wind_kph',
        'uv_index']].corr(),
    annot=True
)

plt.show()

plt.figure(figsize=(7,5))

plt.scatter(
    df["temperature_celsius"],
    df["humidity"],
    alpha=0.6
)

plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.title("Temperature vs Humidity")
plt.grid(True)

plt.show()

