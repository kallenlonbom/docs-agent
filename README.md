# Documentation Agent - RAG framework to answer coding questions

Retrieval-augmented generation is a technique that enhances the accuracy and relevancy of a LLM by providing reference information to the model.
This implementation uses a custom web crawler to download the text of a given documentation page and all its subpages (ex. https://developers.google.com/gmail/api/guides), and then feed it to OpenAI's GPT-4o.

## Installation

Prerequisites: Python3, Pip  
Clone repo  
```pip install -r requirements.txt```  

## Usage

To download and save documentation to new folder: ```python docs-agent.py -download <url> <folder name>```  
To run query engine on saved documentation: ```python docs-agent.py -run <folder name>```  

## Warning  

Running the engine on large collections of documentation will take a significant amount of API credits. (ex. 1,287 pages for a total of ~60 MB costs ~$3 to build). Once the engine is running, each individual won't use a significant amount, but every time the program is restarted, the engine must be started again. Automatic saving of index state will be added soon to remedy this.
