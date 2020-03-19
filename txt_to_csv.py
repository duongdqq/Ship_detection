import pandas as pd

read_file = pd.read_csv(r'/media/veec20/Data/duongdq/darknet/combine_txt.txt')
read_file.to_csv('/media/veec20/Data/duongdq/darknet/change_txt_csv.csv', index=None)