# Task02.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("outputs", exist_ok=True)
train = pd.read_csv("C:/Users/Vishal.S/Downloads/intership of google play store/prodigy internship/prodigy_DS_01/train.csv")               
test = pd.read_csv("C:/Users/Vishal.S/Downloads/intership of google play store/prodigy internship/prodigy_DS_01/test.csv")                  
gender_submission = pd.read_csv("C:/Users/Vishal.S/Downloads/intership of google play store/prodigy internship/prodigy_DS_01/gender_submission.csv")  

print("Datasets loaded:")
print("Train shape:", train.shape)
print("Test shape:", test.shape)
print("Gender submission shape:", gender_submission.shape)

train["Age"].fillna(train["Age"].median(), inplace=True)
train["Embarked"].fillna(train["Embarked"].mode()[0], inplace=True)
train["Fare"].fillna(train["Fare"].median(), inplace=True)
train["Cabin"].fillna("Unknown", inplace=True)

plt.figure(figsize=(6,4))
sns.countplot(x="Sex", hue="Survived", data=train, palette="Set2")
plt.title("Survival by Gender")
plt.savefig("outputs/survival_by_gender.png")
plt.close()

plt.figure(figsize=(6,4))
sns.countplot(x="Pclass", hue="Survived", data=train, palette="Set1")
plt.title("Survival by Passenger Class")
plt.savefig("outputs/survival_by_class.png")
plt.close()

plt.figure(figsize=(8,5))
sns.histplot(train["Age"], bins=30, kde=True, color="blue")
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.savefig("outputs/age_distribution.png")
plt.close()

plt.figure(figsize=(8,6))
corr = train[["Survived","Age","SibSp","Parch","Fare","Pclass"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig("outputs/correlation_heatmap.png")
plt.close()

print("EDA plots saved in outputs/ folder.")
