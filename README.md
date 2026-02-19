# LangChain Structured Output 🚀

This repository demonstrates how to extract structured information from unstructured text using **LangChain** and Pydantic. It ensures that the LLM response follows a specific schema, making it easier to integrate with applications.

## ✨ Features

* **Structured Data Extraction**: Convert raw text into JSON-like objects.
* **Pydantic Validation**: Uses Pydantic models for strict type checking.
* **Environment Configuration**: Securely manages API keys using `.env`.

## 🛠️ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Vedant4102004/Langchain-Structured-Output.git
cd Langchain-Structured-Output

```


2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Set up Environment Variables:**
Create a `.env` file in the root directory and add your API keys:
```env
OPENAI_API_KEY=your_openai_api_key
HUGGINGFACE_TOKEN=your_huggingface_token

```



## 🚀 Usage

Run the main script to see structured output in action:

```bash
python main.py

```

## 📂 Project Structure

* `main.py`: Main logic for LangChain structured output.
* `.env`: Environment variables (ignored by Git).
* `.gitignore`: Files to be excluded from version control.
* `requirements.txt`: List of Python dependencies.

---

