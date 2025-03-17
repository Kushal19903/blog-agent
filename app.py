import streamlit as st
import logging
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import initialize_agent, Tool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_ollama import OllamaLLM

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Streamlit app title and description
st.title("Blog Generation System")
st.write("Enter a blog topic, and the system will generate a well-structured blog for you!")

# Initialize Ollama LLM


def initialize_llm(model_name="gemma:2b"):
    try:
        llm = Ollama(model=model_name)
        logger.info(f"Initialized Ollama model: {model_name}")
        return llm
    except Exception as e:
        logger.error(f"Failed to initialize Ollama model: {e}")
        st.error("Failed to initialize the language model. Please check the logs.")
        return None

# Initialize tools


def initialize_tools():
    try:
        search = DuckDuckGoSearchRun()
        wikipedia_api_wrapper = WikipediaAPIWrapper()
        wikipedia = WikipediaQueryRun(api_wrapper=wikipedia_api_wrapper)
        tools = [
            Tool(
                name="Search",
                func=search.run,
                description="Useful for finding current information on the web."
            ),
            Tool(
                name="Wikipedia",
                func=wikipedia.run,
                description="Useful for getting factual information from Wikipedia."
            )
        ]
        logger.info("Initialized tools: DuckDuckGo Search and Wikipedia.")
        return tools
    except Exception as e:
        logger.error(f"Failed to initialize tools: {e}")
        st.error("Failed to initialize tools. Please check the logs.")
        return []

# Create the agent


def create_agent(llm, tools):
    try:
        agent = initialize_agent(
            tools, llm, agent="zero-shot-react-description", verbose=True)
        logger.info("Created LangChain agent.")
        return agent
    except Exception as e:
        logger.error(f"Failed to create agent: {e}")
        st.error("Failed to create the agent. Please check the logs.")
        return None

# Define the blog generation function


def generate_blog(topic, llm):
    try:
        prompt_template = PromptTemplate(
            input_variables=["topic"],
            template="""
            You are a professional blog writer. Write a well-structured and engaging blog on the topic: {topic}.
            The blog should have the following sections:
            1. Heading: Clearly define the topic of the blog.
            2. Introduction: Provide an engaging introduction to the topic, highlighting its importance.
            3. Content: Present detailed and informative content, supported by research and relevant sources. Include at least three key points.
            4. Summary: Summarize the main points covered in the blog and provide a concluding thought.
            Use simple and clear language, and ensure the content is accurate and relevant.
            """
        )
        blog_chain = LLMChain(llm=llm, prompt=prompt_template)
        blog = blog_chain.run(topic)
        logger.info(f"Generated blog for topic: {topic}")
        return blog
    except Exception as e:
        logger.error(f"Failed to generate blog: {e}")
        st.error("Failed to generate the blog. Please check the logs.")
        return None


# Streamlit input for the blog topic
topic = st.text_input("Enter the blog topic:")

# Generate and display the blog
if st.button("Generate Blog"):
    if topic:
        with st.spinner("Generating blog..."):
            # Initialize components
            llm = initialize_llm()
            tools = initialize_tools()
            agent = create_agent(llm, tools)

            if llm and tools and agent:
                blog = generate_blog(topic, llm)
                if blog:
                    st.success("Blog generated successfully!")
                    st.write("### Generated Blog:")
                    st.write(blog)
    else:
        st.warning("Please enter a blog topic.")

# Add a download button for the generated blog
if "blog" in locals():
    st.download_button(
        label="Download Blog",
        data=blog,
        file_name="generated_blog.txt",
        mime="text/plain"
    )
