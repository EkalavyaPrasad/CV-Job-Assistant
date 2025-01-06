# AI Job Assistant

AI Job Assistant is a Streamlit-based application that uses large language models to help users tailor their CVs and optimize them for specific job descriptions. It provides features like identifying skill gaps, analyzing CVs, and generating ATS-optimized recommendations.

---

## Features

- **Job Industry Identification**: Extracts top three relevant industries based on the CV content.
- **Job Description Analysis**: Summarizes job descriptions and provides insights.
- **CV Review**: Tailors CV content to align with the job description.
- **Skill Gap Analysis**: Identifies missing or underemphasized skills in the CV.
- **CV Update**: Automatically updates the CV in markdown format for clarity and relevance.

---

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd AI-Job-Assistant
   ```

2. Set up a virtual environment (recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate  # For Linux/macOS
   env\Scripts\activate     # For Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure you have the **Ollama** language models and API running locally:
   - Install Ollama following [the official guide](https://ollama.ai/docs).
   - Start the API server using:
     ```bash
     ollama start
     ```

---

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the application in your browser. The URL will typically be:
   ```
   http://localhost:8501
   ```

3. Follow these steps to use the application:
   - **Step 1**: Paste your CV in the provided text area or use the sample CV.
   - **Step 2**: Paste the job description for which you want to tailor your CV.
   - **Step 3**: Click the "Initialise Model" button to generate insights, identify skill gaps, and update your CV.

---

## Project Structure

- **`app.py`**: Main application file.
- **`requirements.txt`**: Lists all the dependencies required to run the project.
- **`README.md`**: Documentation file.
- **Additional Files**: The application fetches and uses the Ollama models specified.

---

## Requirements

Ensure you have the following installed:
- Python 3.8 or higher
- Streamlit
- Ollama API (running locally)
- Supported Ollama Models (`llama3.2:latest`, `phi3:latest`)

---

## How It Works

1. The application uses the `langchain_ollama` integration to interact with LLMs.
2. Users input their CVs and job descriptions.
3. The AI analyzes the inputs to:
   - Identify relevant industries.
   - Generate ATS-friendly recommendations.
   - Highlight skill gaps and suggest CV improvements.
4. The updated CV is presented in a markdown format.

---

## Contributing

Feel free to fork the repository, make changes, and submit pull requests. Contributions are welcome!

---

Happy Job Hunting! 🚀
