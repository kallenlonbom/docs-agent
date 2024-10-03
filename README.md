# Documentation Agent - RAG framework to answer coding questions

Retrieval-augmented generation is a technique that enhances the accuracy and relevancy of a LLM by providing refernece information to the model.
This implementation uses a custom web crawler to download the text of a given documentation page and all its subpages (ex. https://developers.google.com/gmail/api/guides), and then feed it to OpenAI's gpt-4.

## Installation

Prerequisites: Python3, Pip  
Clone repo  
```pip install -r requirements.txt```  

## Usage

To download docs and run query engine - python docs-agent.py -download <url> <folder to save docs to>  
To run query engine on already downloaded docs - python docs-agent.py <folder containing docs>  
