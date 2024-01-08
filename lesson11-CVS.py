import pandas as pd

l_connections = [
    {
        "user_name": "etl_user",
        "password": "12,3",
        "host": "127.0.0.1"
    },
    {
        "user_name": "test_user",
        "password": "456",
        "host": "127.0.0.2"
    }
]
df1 = pd.DataFrame(l_connections)
print(df1)
print(type(df1))

# Write
df1.to_csv(r'files\from_pandas.csv', index=False)

# Read
df2 = pd.read_csv(r'files\from_pandas.csv')
print(df2)
print(type(df2))
