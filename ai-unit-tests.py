import google.generativeai as genai

# Configure Google API access
genai.configure(api_key="REPLACE_THIS_WITH_YOUR_FREE_GOOGLE_API_KEY")

# Select the Large Language Model (LLM)
model = genai.GenerativeModel("gemini-pro")

# Set low randomness of output (low model creativity)
generation_config = genai.GenerationConfig(temperature=0.0)

# Create a prompt template
prompt_template = """
Can you please create test cases in code for this Python code?

{question}

Explain in detail what these test cases are designed to achieve.
"""

# Create a question for the prompt
question = """
class Calculator:
    def add(self, left, right):
        return left + right

    def subtract(self, left, right):
        return left - right

    def multiply(self, left, right):
        return left * right

    def divide(self, left, right):
        return left / right
"""

# Ask the Large Language Model (LLM)
completion = model.generate_content(
  contents = prompt_template.format(question=question),
  generation_config=generation_config)

# Print the response from the Large Language Model (LLM)
print(completion.text)
