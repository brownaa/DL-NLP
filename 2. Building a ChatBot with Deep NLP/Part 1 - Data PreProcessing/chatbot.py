# Building a Chatbot with Deep NLP

# Importing the libraries
import numpy as np
import tensorflow as tf
import re
import time

###### Part 1 - Data Preprocessing #######

file_lines = '2. Building a ChatBot with Deep NLP/Part 1 - Data PreProcessing/cornell movie-dialogs corpus/movie_lines.txt'
file_conversations = '2. Building a ChatBot with Deep NLP/Part 1 - Data PreProcessing/cornell movie-dialogs corpus/movie_conversations.txt'
lines = open(file_lines ,encoding = 'utf-8', errors = 'ignore').read().split('\n')
conversations = open(file_conversations, encoding = 'utf-8', errors = 'ignore').read().split('\n')

