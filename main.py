from transformers import pipeline

if __name__ == '__main__':
    pipe = pipeline("text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
    res = pipe('I love Python')

    print(res)
