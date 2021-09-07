
# Thyroid Prediction

#### Download Python3: [Python](https://www.python.org/downloads/)

### Installation
* Download or clone this project
* Go to the project directory through command line
* Install dependencies: `pip install -r requirements.txt`

### Running project
* For any data in csv format, to convert it to json, `python csvtojson.py`
* Generating random sentences from `dataset.json` file: `python generate_sentences.py`
* The sentences will be saved to `dataset.txt`
* Extracting vitals data from sentence: `python extract_data_nltk.py`
* The data will be saved to `revised_dataset.json` as well as `revised_dataset.csv` which will work as knowledge base

### Prediction
* Running Jupyter notebook: `jupyter notebook`
* Browse to: `localhost:8888` if browser don't redirect by its own
* Open `prediction.ipynb`

