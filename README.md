# ToSumUp - Text Summarization Tool

## Overview

**ToSumUp** is a text summarization tool built using **Gradio**, **Flask**, and **Hugging Face Transformers**. This application takes a block of text as input and generates a concise summary using a pre-trained `t5-small` model from Hugging Face.

## Features

- **Gradio Interface**: A user-friendly web interface to interact with the summarization model.
- **Flask Integration**: Allows hosting the summarization tool as a web application.
- **Pre-trained Model**: Utilizes the `t5-small` model for efficient and accurate text summarization.
- **Customization**: Designed to handle both programmatic API calls and user interaction via the Gradio interface.

## Requirements

### Python Libraries:
- **Flask**: For building the web application.
- **Gradio**: For creating an interactive user interface.
- **Transformers**: For leveraging pre-trained NLP models.

### Install Dependencies:
```bash
pip install flask gradio transformers

## Usage

### 1. Run the Application:
```bash
python app.py
