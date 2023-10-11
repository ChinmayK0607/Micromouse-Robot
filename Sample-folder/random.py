import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
 author.delete('1.0','end')
 author.insert('1.0',article.authors)

 publication.delete('1.0','end')
 publication.insert('1.0',article.publish_date)

 summary.delete('1.0','end')
 summary.insert('1.0',article.summary)
