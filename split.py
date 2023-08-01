import pandas as pd
from sklearn.model_selection import train_test_split

# 读取CSV文件
data = pd.read_csv('data.csv',encoding='utf-8')

# 获取特征列
features = data[['src', 'mt','score']]


# 划分训练集和验证集
train_data, valid_data = train_test_split(features, test_size=0.1, random_state=42)

# 将训练集保存到文件

train_data.to_csv('train_data.csv', index=False, encoding='utf-8')

# 将验证集保存到文件

valid_data.to_csv('valid_data.csv', index=False, encoding='utf-8')