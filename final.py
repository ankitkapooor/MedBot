from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('Models/epochs_1/')
model = AutoModelForCausalLM.from_pretrained('Models/epochs_1/')

with open('Dataset/dataset_val.txt', 'r', encoding = "UTF-8") as f:
    data = f.read()

special_token = '<|endoftext|>'

data = data.split(special_token)

#print(data[0])
prompt_text = data[100].split('Answer:')[0] + 'Answer: '
#print(prompt_text)

prompt_text = 'Question: Hi think I am addicted to smoking, how do i quit?\nAnswer:'
encoded_prompt = tokenizer.encode(prompt_text,
                                  add_special_tokens = False,
                                  return_tensors = 'pt')

output_sequences = model.generate(
    input_ids = encoded_prompt,
    max_length = 700,
    temperature = 0.9,
    top_k = 20,
    top_p = 0.9,
    repetition_penalty = 1,
    do_sample = True,
    num_return_sequences = 4
)

for i, output_sequence in enumerate(output_sequences):
    result = tokenizer.decode(output_sequence)
    result = result[:result.index(special_token)]
    print('---')
    print(f'Generated output #{i+1}')
    print('---')
    print(result)
