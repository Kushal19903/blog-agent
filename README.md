# Blog Generation System

## Overview

This project is a Blog Generation System that utilizes Streamlit and Ollama to generate blog content based on user input. It leverages the `gemma:2b` model and external resources like Wikipedia and DuckDuckGo search to enhance content generation.


## **Features**
- **Blog Generation**: Generates a blog with the following sections:
  - Heading
  - Introduction
  - Content
  - Summary
- **Research Tools**: Uses DuckDuckGo Search and Wikipedia to gather information.
- **Streamlit Interface**: Provides a simple web interface for users to input a topic and view the generated blog.
- **Download Option**: Allows users to download the generated blog as a `.txt` file.

---

## **Requirements**
To run this project, you need the following:

1. **Python 3.8 or later**
2. **Ollama**: A lightweight framework for running large language models locally.
3. **Streamlit**: For the web interface.
4. **LangChain**: For integrating the language model and tools.
5. **Additional Libraries**: `duckduckgo-search`, `wikipedia-api`, etc.

---

## Installation and Setup

### Step 1: Install Ollama

Download and install Ollama from the official website: [Ollama](https://ollama.com/).

### Step 2: Pull the Gemma Model

Run the following command to download the `gemma:2b` model:

```bash
ollama pull gemma:2b
```

### Step 3: Install Required Libraries

Install the necessary Python dependencies using pip:

```bash
pip install streamlit langchain langchain-community duckduckgo-search wikipedia-api
```

## Running the Project

### Start the Ollama Server

Ensure the Ollama server is running in the background before launching the application:

```bash
ollama serve
```

### Run the Streamlit App

Navigate to the project directory and run the Streamlit app using:

```bash
streamlit run blog_generator_app.py
```

### Use the App

1. Open the URL displayed in the terminal (usually [http://localhost:8501](http://localhost:8501)).
2. Enter a blog topic in the input field and click **Generate Blog**.
3. View the generated blog and download it using the **Download Blog** button.

## Project Structure

```
blog-generation-system/
├── blog_generator_app.py       # Main Streamlit app code
├── README.md                   # Project documentation
└── requirements.txt            # List of dependencies
```

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributing

Feel free to contribute by submitting pull requests or reporting issues.

