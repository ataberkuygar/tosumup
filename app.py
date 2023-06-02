import gradio as gr
from flask import Flask, request, render_template
from transformers import pipeline, set_seed

app = Flask(__name__)
def summarize(text):
    # Use the summarizer pipeline to generate a summary
    summary = pipe(text)
    
    # Extract the clean summary text from the output
    summary_text = summary[0]['summary_text'].strip()
    
    return summary_text

def pipe(text):
    summary = pipeline('summarization', model = 't5-small' )
    return summary
inputs = gr.inputs.Textbox(label="Input Text")
outputs = gr.outputs.Textbox(label="Output Text")

gradio_app = gr.Interface(summarize, inputs, outputs, title="ToSumUp", 
                          description="Enter some text to summarize it.")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        input_text = request.form["input_text"]
        output_text = summarize(input_text)
        return render_template("index.html", input_text=input_text, output_text=output_text)
    return render_template("index.html")

if __name__ == "__main__":
    gradio_app.launch(share=True)