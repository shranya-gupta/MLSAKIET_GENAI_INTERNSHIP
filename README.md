BASIC TEXT GENERATOR
-----------------------
Description: Use a simple generative AI model to generate text based on a prompt
Skills: Basic Python, text generation, API usage

Overview

This project utilizes the OpenAI language model to generate text according to prompts specified by users. It uses GPT-2, developed by OpenAI, as a powerful transformer-based model. This project first asks the user to enter a prompt then the user gets generated text as an output.

Prerequisites

You must have prior knowledge about the following:
•	Basic Python
•	Transformers and their implementation.
•	Use of torch in python
•	Basic Generative AI knowledge

Requirements

Before running the project, ensure you have the following installed:
•	Transformers library by Hugging Face
•	Python 3.6 or higher
•	PyTorch

Code Explanation

•	Imports: The python script imports libraries, including transformers for the GPT-2 model and torch for tensor operations.
•	Model Initialization: Initialization of  GPT-2 tokenizer and model occurs using    from_pretrained() method
•	Text Generation Function: The text_generate() function is used to generate text based on the prompt specified by the user takes a prompt and generates text using specified parameters. 
•	Main Function: The main() function is a user interface which asks the user to enter a propmpt and then display generated text.

Example

Enter your prompt:
"Once upon a time"
"Once upon a time, in a land far away, there lived a young princess who loved to explore the forest."

--------------------------------------------------------------------------------------------------------------------------------------------------------------------


SENTIMENT ANALYSIS TOOL
------------------------
Description: Use AI Builder to develop a tool that analyzes text sentiment
Skills: Sentiment analysis, AI Builder, text processing

Overview

This project helps create a sentiment analysis workflow using Power Automate. This project first takes a sentence or a paragraph from a user as an input . The workflow takes this input to AI Builder for sentiment analysis.Based on the input, it determines the sentiment of the user i.e Positive,Negative and Neutral. It then stores the probability of each sentiment dynamically in a pre-existing excel file.

Prerequisites

Before you begin, ensure you have:
•	AI Builder
•	Microsoft Power Automate account
•	An Excel Online account (can be either OneDrive or Business)
•	Understanding of how to use AI Builder with Power Automate

Workflow Description

1.	Text Input: User enters text to be analysed.
2.	Sentiment Analysis: The workflow sends the text to the AI Builder sentiment analysis which returns the probabilities of the sentiments.
3.	Store Results: The results including the original text, the detected sentiment, and the probabilities for positive, negative, and neutral sentiments are stored in a specified Excel file.






