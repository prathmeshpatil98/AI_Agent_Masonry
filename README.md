
---

# Web Research Agent Documentation

## Overview

**Masonry Web Research Agent** is an AI-powered tool designed to automatically search the web, extract relevant information, analyze it and generate a detailed research report based on user queries. The goal of the agent is to provide a comprehensive summary of the topic requested by the user, including data extraction from news articles, web pages and analysis of relevant content.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Setting Up the Environment](#setting-up-the-environment)
4. [Running the Application](#running-the-application)
5. [Application Flow and Structure](#application-flow-and-structure)
6. [How the Web Research Agent Works](#how-the-web-research-agent-works)
7. [Handling Errors](#handling-errors)
8. [Contributing](#contributing)
9. [License](#license)

---

## Prerequisites

Before setting up the agent, ensure you have the following:

- **Python 3.10+**: The project is developed using Python 3.10 or later. Ensure you have it installed.
- **pip**: Python's package installer. If you don't have it, you can follow the [pip installation guide here](https://pip.pypa.io/en/stable/installation/).
- **API Keys**: You will need the following API keys to run the application:
  - Google API Key (for connecting to the Gemini AI model)
  - News API Key (to fetch the latest news articles related to your research query)
- **Internet Access**: The agent needs internet access to fetch data from various web sources.

---

## Installation

### 1. Clone the Repository

To start using the Web Research Agent, clone the repository to your local machine.

```bash
git clone https://github.com/prathmeshpatil98/AI_Agent_Masonry.git
cd AI_Agent_Masonry
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

Create and activate a virtual environment to keep the dependencies isolated:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

This will install all necessary dependencies, including `requests`, `beautifulsoup4`, `streamlit`, `google-generativeai` and others.

---

## Setting Up the Environment

### 1. API Keys Configuration

The agent requires two API keys to function properly:

- **Google API Key**: For connecting to the Gemini AI model.
- **News API Key**: For fetching the latest news articles.

Create a `.env` file in the root directory of the project and add the following keys:

```bash
GOOGLE_API_KEY=your_google_api_key_here
NEWS_API_KEY=your_news_api_key_here
```

Replace `your_google_api_key_here` and `your_news_api_key_here` with your actual keys.

### 2. Install `.env` Package

If you don’t have the `python-dotenv` package installed (which loads the `.env` file), you can install it using:

```bash
pip install python-dotenv
```

This will automatically load the environment variables from the `.env` file when the application runs.

---

## Running the Application

Once you’ve completed the setup, you can run the Web Research Agent. Follow these steps:

### 1. Start the Streamlit Application

Run the following command to start the Streamlit app:

```bash
streamlit run app.py
```

The application will launch in your default web browser, where you can enter your research query.

### 2. Enter Your Research Query

In the input box on the Streamlit interface, type your research topic or question. The agent will automatically begin searching the web, extracting relevant data and analyzing it.

### 3. View the Results

Once the research process is complete, the agent will display:

- **Research Summary**: A concise summary of the findings.
- **Web Sources**: A list of relevant web sources.
- **Latest News**: Recent news articles related to the topic.
- **Comprehensive Report**: A detailed, AI-generated summary of the research findings.

---

## Application Flow and Structure

The Web Research Agent follows a structured flow to gather, analyze, and report information.

### Flow Diagram:

```
+-------------------------+
|   User Input (Query)     |
+-------------------------+
            |
            v
+-------------------------+
|  Step 1: Search Web     |  ->  Google Search API
+-------------------------+
            |
            v
+-------------------------+
|  Step 2: Scrape Content |
|  (From Found Links)     |
+-------------------------+
            |
            v
+-------------------------+
|  Step 3: Analyze Content|
|  (Extract Key Findings) |
+-------------------------+
            |
            v
+-------------------------+
|  Step 4: Fetch News     |  ->  News API
+-------------------------+
            |
            v
+-------------------------+
|  Step 5: Compile Report |
+-------------------------+
            |
            v
+-------------------------+
|  Final Research Report  |
+-------------------------+
```

---

## How the Web Research Agent Works

### 1. Web Search

When a user submits a query, the agent first performs a web search using the **Google Search API**. It retrieves the top search results related to the query.

### 2. Content Scraping

The agent scrapes content from the URLs obtained through the web search. It extracts the main text content using **BeautifulSoup**, ensuring it captures only the relevant information.

### 3. Content Analysis

Once the content is scraped, it is analyzed by checking if specific keywords are present. The relevance score is calculated, and the agent determines if the content is relevant to the user's query.

### 4. News Aggregation

The agent uses **News API** to fetch the latest news articles related to the query. These articles are added to the report, providing real-time information on the topic.

### 5. Report Compilation

Using the **Gemini AI model**, the agent generates a comprehensive research report that includes:
- A **summary** of the key findings.
- **Data, timelines**, or statistics if relevant.
- **Citations** for sources like web pages or news articles.

---

## Handling Errors

While running the Web Research Agent, there are several potential issues that may occur:

### 1. **API Failures**
If the API (News API or Gemini AI) fails, the agent will notify the user with a friendly error message and continue with the available data. 

### 2. **Unreachable Websites**
If a website is unreachable during scraping, the agent will skip that website and proceed with others.

### 3. **Conflicting Information**
If the sources provide conflicting information, the agent will present the different viewpoints and summarize them, offering a balanced report.

### 4. **No Relevant Data**
If no relevant data is found, the agent will display a message indicating that no useful content was available for the given query.

---

## Contributing

We welcome contributions to enhance the functionality of the Web Research Agent. If you would like to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to your branch (`git push origin feature/your-feature`).
6. Open a Pull Request.

---

## License

MIT License

Copyright (c) 2025 Prathmesh

Permission is hereby granted, free of charge, to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, subject to the following conditions:

The copyright notice and this permission notice must be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY ARISING FROM THE SOFTWARE.

---

## Contact

For any questions or support, feel free to reach out to us at:  
**Email**: prthmeshpatil98@gmail.com

---

## Conclusion

This Web Research Agent is designed to streamline the process of gathering, analyzing and compiling research from the web. With minimal input from the user, it provides a comprehensive and well-structured research report, helping users save time and effort in their research tasks.

---

### End of Documentation
