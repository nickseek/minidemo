import configparser
from transformers import AutoModel, AutoTokenizer, GPT2Tokenizer,GPT2LMHeadModel
import os

# Config = configparser.ConfigParser()
# Config.read('config.ini')
# model_path = Config.get('model','model_path')
# tokenizer_path = Config.get('model','tokenizer_path')
model_data_folder = os.path.join('data','modelFiles')
model_path = os.path.join(model_data_folder,'model')
tokenizer_path = os.path.join(model_data_folder,'tokenizer')
model_name = 'gpt2'

class Generator:
    def __init__(self) -> None:
        self.model = get_model()
        self.tokenizer = get_tokenizer()

    def generate_text(self,prompt):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=15, num_return_sequences=1)
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return(generated_text)

def get_model():
    if not os.path.exists(model_path):    
        model = AutoModel.from_pretrained(model_name)
        model.save_pretrained(model_path)
    else:
        model = GPT2LMHeadModel.from_pretrained(model_path)
    return model

def get_tokenizer():
    if not os.path.exists(tokenizer_path):
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.save_pretrained(tokenizer_path)
    else:
        tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_path)
    return tokenizer


if __name__ == "__main__":
    prompt = 'Helpful model'
    gen = Generator()
    response = gen.generate_text(prompt)
    print(f"prompt: {prompt}")
    print(f"response: {response}")

