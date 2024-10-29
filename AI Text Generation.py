#Import the libraries
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
#Use GPT to form random sentences
name = "gpt2"
tokens = GPT2Tokenizer.from_pretrained(name)
model = GPT2LMHeadModel.from_pretrained(name)
model.eval()
#Used to generate text
def text_generate(prompt, max_length=50):
    input_ids = tokens.encode(prompt, return_tensors='pt')
    attention_mask = torch.ones(input_ids.shape, dtype=torch.int)
    output = model.generate(input_ids=input_ids,
        attention_mask=attention_mask,
        max_length=max_length,
        num_return_sequences=1,
        pad_token_id=tokens.eos_token_id,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        top_k=100
    )
    return tokens.decode(output[0], skip_special_tokens=True)
#Ask for the prompt
def main():
    prompt = input("Enter your prompt: ")
    generated_text = text_generate(prompt)
    print(generated_text)
if __name__ == "__main__":
    main()
