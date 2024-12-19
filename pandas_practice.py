# import pandas as pd

# df1 = pd.DataFrame({'id': [1, 2, 3, 4], 'salary': [1000, 2000, 3000, 4000]})
# df2 = pd.DataFrame({'id': [1, 5, 3, 4], 'salary': [1000, 5000, 3000, 10000]})

# print(df1['id'].isin(df2['id']))

# deleted_row_in_df2 =df1[~df1['id'].isin(df2['id'])]
# print(deleted_row)


# deleted_row_in_df1= df2[~df2['id'].isin(df1['id'])]
# print(deleted_row_in_df1)


# Find rows in df2 where id exists in df1 but salary is different (updated)
# updated_rows = df2[df2['id'].isin(df1['id']) & ~df2['id'].isin(df1[df1['salary'] == df2['salary']] ['id'])]

# print(updated_rows)
# print(df1['salary'] == df2['salary'])
# print(df1[df1['salary'] == df2['salary']] ['id'])
# print(df2['id'].isin(df1[df1['salary'] == df2['salary']] ['id']))
# print(~df2['id'].isin(df1[df1['salary'] == df2['salary']] ['id']))
# print(df2['id'].isin(df1['id']))
# print(df2['id'].isin(df1['id'][df1['salary'] == df2['salary']] ))



