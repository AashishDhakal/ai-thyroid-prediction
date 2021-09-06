# Thyroid Prediction

#### Download Python3: `https://www.python.org/downloads/`

### Installation
* Download or clone this project
* Go to the project directory through command line
* Install dependencies: `pip install -r requirements.txt`

### Running project
* Generating random sentences: `python generate_sentences.py`
* Extracting vitals data from sentence: `python extract_data_nltk.py`
* The data will be saved to `dataset.json` which will work as knowledge base
* For any data in csv format, to convert it to json, `python csvtojson.py`

### Prediction
* Running Jupyter notebook: `jupyter notebook`
* Browse to: `localhost:8888` if browser don't redirect by its own
* Open `prediction.ipynb`

