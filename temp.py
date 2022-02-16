import matplotlib
#%matplotlib inline
matplotlib.rcParams['figure.dpi'] = 200
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import seaborn as seconds_in_a_day
import pandas as pd
import json

datasets = ['Dataset/ehealthforumQAs.json',
            'Dataset/icliniqQAs.json',
            'Dataset/questionDoctorQAs.json',
            'Dataset/webmdQAs.json']

df = pd.DataFrame()

questions, answers = [], []

for dataset in datasets:
  data = json.load(open(dataset, 'r'))
  for i in data['pairs']:
    questions.append(i['question'])
    answers.append(i['answer'])

df['questions'] = questions
df['answers'] = answers

df.head()

df.to_pickle('temp.pkl')

df['q_length'] = df['questions'].str.len().astype(int)
df['a_length'] = df['answers'].str.len().astype(int)

df.head()

special_token = ' <|endoftext|> '

print(df.shape)

df['train_param'] = '\nQuestion: ' + df.questions + '\nAnswer: ' + df.answers + special_token
df.iloc[100]
print(df.iloc[100].train_param)
df.to_pickle('df_preprocessed.pkl')

dataset_train = df[:29000].train_param.values
dataset_val = df[29000:].train_param.values

with open('Dataset/dataset_train.txt', 'w', encoding = 'UTF-8') as f:
  f.write('\n'.join(dataset_train))

with open('Dataset/dataset_val.txt', 'w', encoding = 'UTF-8') as f:
  f.write('\n'.join(dataset_val))
