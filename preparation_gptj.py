import json

filenames = ['Dataset/ehealthforumQAs.json',
            'Dataset/icliniqQAs.json',
            'Dataset/questionDoctorQAs.json', 
            'Dataset/webmdQAs.json']
for filename in filenames:
    with open(filename, 'r') as f:
        with open('Dataset/processed_dataset.txt', 'w', encoding = "UTF-8") as g:
            data = json.load(f)
            for i in data['pairs']:
                g.write(f"User: {i['question']}\n")
                g.write(f"MedBot: {i['answer']}\n")
