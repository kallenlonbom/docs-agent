from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.openai import OpenAI
from llama_index.core.node_parser import SimpleNodeParser
import os
import sys
from crawler import crawl

os.environ["OPENAI_API_KEY"] = "YOUR-API-KEY"

# to download and save docs - python docs-agent.py -download <url> <name of folder to create and save docs to>
# to run query engine on docs - python docs-agent.py -run <folder containing docs>
if sys.argv[1] == '-download':
    folder = sys.argv[3]
    crawl(sys.argv[2], folder)
elif sys.argv[1] == '-run':
    folder = sys.argv[2]

    # read docs
    docs = SimpleDirectoryReader(input_dir=folder).load_data()
    print(f"\nLoaded {len(docs)} docs\nBuilding query engine")

    # define LLM
    llm = OpenAI(model="gpt-4o")
    Settings.llm = llm

    # build index and query engine
    node_parser = SimpleNodeParser.from_defaults(chunk_size=260,chunk_overlap=2)
    nodes = node_parser.get_nodes_from_documents(docs)
    index = VectorStoreIndex(nodes)
    query_engine = index.as_query_engine()

    # user input loop
    while True:
        print('\nEnter question, or "quit" to quit')
        prompt = input()
        if prompt == 'quit':
            break
        else:
            response = query_engine.query(
                prompt + " Be specific, with exact instructions and syntax."
            )
            response_text = str(response)
            print(response_text)
else:
    print('Invalid input, correct format is\npython docs-agent.py -download <url> <name of folder to create and save docs to>\nor\npython docs-agent.py -run <folder containing docs>')