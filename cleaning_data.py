df = pd.read_csv('dirty_data.csv')

df = df.dropna(subset=['Name'])

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

df['Age'] = df['Age'].apply(lambda x: x if x >= 0 else df['Age'].mean())
df['Salary'] = df['Salary'].apply(lambda x: x if x >= 0 else df['Salary'].mean())

df = df[df['Salary'] < 100000]

print("\nОчищенные данные:")
print(df)
