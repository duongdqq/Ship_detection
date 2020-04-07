import pandas as pd

filename = 'statistic_data.txt'

df = pd.read_csv(filename, header=None, error_bad_lines=False, encoding='utf8')

df.columns = ['all']

coordination = df['all'].str.split(' ', n=5, expand=True)

df['id_class'] = coordination[0]
df['x_center'] = coordination[1]
df['y_center'] = coordination[2]
df['width'] = coordination[3]
df['height'] = coordination[4]

df = df.drop(columns=['all'])

df.to_csv('converted_csv.csv', index=False)