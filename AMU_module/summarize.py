import textwrap
from transformers import BartTokenizer, BartForConditionalGeneration

def bart_completion(prompt, model, tokenizer, max_length=1000):
    prompt = 'Summarize the following sentence: ' + prompt
    input_ids = tokenizer(prompt, return_tensors="pt", max_length=max_length, truncation=False)["input_ids"]
    output = model.generate(input_ids, max_length=300, temperature=0.6, num_beams=4, length_penalty=2.0, do_sample=True)
    return tokenizer.decode(output[0], skip_special_tokens=True)

def summarize(text):
    # In theory, this function should be recursive. However, the performance of BART model was not satisfactory when we recursivley summarize the text.
    # In the future, we need to change this code into recursive one once we have a statisfactory summarization model.
    chunks = textwrap.wrap(text, 1000)
    result = list()
    count = 0
    tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
    model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
    print('Chunks: ' + str(len(chunks)))
    for chunk in chunks:
        count = count + 1
        print(str(count))
        summary = bart_completion(chunk, model, tokenizer)
        result.append(summary)
    return " ".join(result) 