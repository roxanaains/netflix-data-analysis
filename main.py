import pandas as pd

# citire csv
df = pd.read_csv("netflix_titles.csv")

# afiseaza primele randuri
print(df.head())

# informatii despre date
print(df.info())

# cate filme sunt
print(df["type"].value_counts())
# top 10 tari
print(df["country"].value_counts().head(10))

print(df["release_year"].value_counts().head(10))
print(df["rating"].value_counts())


import matplotlib.pyplot as plt
df["type"].value_counts().plot(kind="bar")

plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")

plt.show()

df["country"].value_counts().head(10).plot(kind="bar")

plt.title("Top 10 Countries")

plt.show()
recent_movies = df[df["release_year"] > 2020]

print(recent_movies.head())

df["release_year"].value_counts().head(10).plot(kind="bar")

plt.title("Top Release Years")

plt.show()


movies = df[df["type"] == "Movie"]

print(movies.head())

usa_content = df[df["country"] == "United States"]

print(usa_content.head())
recent = df[df["release_year"] > 2018]

print(recent.head())
