# Import the OutputParser class
from langchain.agents.conversational.output_parser import OutputParser

# Define a subclass of OutputParser that parses the output into a list of answers
class ListOutputParser(OutputParser):
    def parse(self, output: str) -> list:
        # Split the output by newlines and remove empty lines
        lines = [line.strip() for line in output.split("\n") if line.strip()]
        # Return the list of answers
        return lines

    def get_format_instructions(self) -> str:
        # Return a custom format instruction that tells the language model to return one answer per line
        return "Please return one answer per line.\n"

# Create an instance of the ListOutputParser
output_parser = ListOutputParser()

# Create a ConversationalRetrieval chain and pass the output parser as an option
chain = ConversationalRetrievalQAChain.fromLLM(
    model,
    vectorstore.asRetriever(15),
    {
        "qaTemplate": QA_PROMPT,
        "questionGeneratorTemplate": CONDENSE_PROMPT,
        "verbose": True,
        "outputParser": output_parser, # Pass the output parser instance
    },
)

# Call the chain and use the output parser to parse the response
question = "What are some benefits of meditation?"
response = chain.call({"question": question})
answers = output_parser.parse(response)
print(answers)
