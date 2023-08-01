# 打开 train.tsv 文件进行读取
import chardet
# "news-commentary-v16"32275 45
# "en-zh-v1"14170585 20000-45


import random

def random_sampling(file_path, sample_count):
    with open(file_path, 'r',encoding="utf-8") as file:
        lines = file.readlines()
        sampled_lines = random.sample(lines, sample_count)
        return sampled_lines

# 假设原始txt文档的路径为file.txt
file1_path = "en-zh-v1.txt"
file2_path = "news-commentary-v16.en-zh.tsv"

sample1_count = 20000-45  # 要抽取的数据数量
sample2_count = 45
sampled_data = random_sampling(file2_path, sample2_count)

# 将抽样结果写入新的txt文档
output_file_path = "./result2.txt"
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.writelines(sampled_data)

sampled_data = random_sampling(file1_path, sample1_count)

# 将抽样结果写入新的txt文档
output_file_path = "./result1.txt"
with open(output_file_path, 'w',encoding='utf-8') as output_file:
    output_file.writelines(sampled_data)
