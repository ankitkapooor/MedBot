from transformers import AutoModelForCausalLM, AutoTokenizer
import random

tokenizer = AutoTokenizer.from_pretrained('Models/epochs_1/')
model = AutoModelForCausalLM.from_pretrained('Models/epochs_1/')
special_token = '<|endoftext|>'

#replies = []

class Generator:
    def __init__(self):
        self.tokenizer = tokenizer
        self.model = model

    def get_reply(user_input):
        prompt_text = f'Question: {user_input}\nAnswer:'
        encoded_prompt = tokenizer.encode(prompt_text,
                                  add_special_tokens = False,
                                  return_tensors = 'pt')

        output_sequences = model.generate(
            input_ids = encoded_prompt,
            max_length = 500,
            temperature = 0.9,
            top_k = 20,
            top_p = 0.9,
            repetition_penalty = 1,
            do_sample = True,
            num_return_sequences = 4
        )

        result = tokenizer.decode(random.choice(output_sequences))
        result = result[result.index("Answer: "):result.index(special_token)]
        return(result[8:])

        '''
        for i, output_sequence in enumerate(output_sequences):
            result = tokenizer.decode(output_sequence)
            result = result[result.index("Answer: "):result.index(special_token)]
            #print('---')
            #print(f'Generated output #{i+1}')
            #print('---')
            #print(result[8:])
            replies.append('---\n' + f'Generated output #{i+1}\n' + '---\n' + result[8:] + '\n')
        return ''.join(reply for reply in replies)
        '''
