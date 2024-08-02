import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')

from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
root.geometry("800x600")
root.title("Sentiment Analyzer")

def get_msg():
    text = inputtxt.get("1.0", "end-1c")
    sid = SentimentIntensityAnalyzer()
    score = ((sid.polarity_scores(str(text))))['compound']
    if score > 0:
        showinfo('Analyzed', "Sentence Is Positive")
    elif score == 0:
        showinfo('Analyzed', "Sentence Is Neutral")
    else:
        showinfo('Analyzed', "Sentence Is Negative")

btn = Button(root, height=2, width=20, text='Analyze',
             command=get_msg)
label = Label(text="What Is the Text?")
inputtxt = Text(root, height=32, width=98)


label.pack()
inputtxt.pack()
btn.pack(pady=(10, 10))

mainloop()