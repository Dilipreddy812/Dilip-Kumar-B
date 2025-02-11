import pandas as pd
from pyweb import pydom
from pyscript import display
from js import Blob, URL, document, FileReader, alert

def convertCsvToJson(event):
    # Get the uploaded file
    file_input = document.getElementById('csvFileInput')
    
    # Check if a file was uploaded
    if file_input.files.length == 0:
        alert('Please upload a CSV file.')
        return

    # Access the first file in the FileList
    file = file_input.files.item(0)  # Use .item() to access the file
    if not file:
        alert('Failed to read the uploaded file.')
        return

    # Read the file content
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
convert_button = document.getElementById('btn-convert')
convert_button.onclick = convertCsvToJson
