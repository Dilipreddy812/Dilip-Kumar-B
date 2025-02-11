import pandas as pd
from pyweb import pydom
from pyscript import display
from js import Blob, URL, document

def convertCsvToJson(event):
    # Get the uploaded file
    file_input = document.getElementById('csvFileInput')
    if not file_input.files.length:
        alert('Please upload a CSV file.')
        return

    file = file_input.files[0]
    reader = FileReader.new()
    reader.onload = lambda e: process_csv(e.target.result)
    reader.readAsText(file)

def process_csv(csv_data):
    try:
        # Convert CSV to JSON using pandas
        df = pd.read_csv(io.StringIO(csv_data))
        json_data = df.to_json(orient='records', indent=4)

        # Display JSON in the textarea
        json_output = document.getElementById('jsonOutput')
        json_output.value = json_data

        # Create a downloadable link
        blob = Blob.new([json_data], {type: 'application/json'})
        download_link = document.getElementById('downloadLink')
        download_link.href = URL.createObjectURL(blob)
        download_link.style.display = 'inline-block'
        download_link.textContent = 'Download JSON'
    except Exception as e:
        alert(f'Error processing CSV: {str(e)}')

# Attach the conversion function to the button click event
pydom["button#btn-convert"].on("click", convertCsvToJson)
