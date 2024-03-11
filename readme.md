# Python automation project using Selenium

## Requirements

* Python 3

* Selenium (run `pip install requirements.txt` to automatically install required packages)

* Browser drivers: they are included in the `/resources` folder in the project. Add their path to PATH environment variable in your OS.

## Run project

In terminal, cd into the project's root folder and execute file `runner.py`:

`python runner.py`

## Run and generate test report

In order to get an html report, instead of using the provided runner, use `pytest`'s runner with html-report _(this method requires Pytest and Pytest Html Report_:

`python -m pytest testcases --html=report.html --self-contained-html`

To run a specific file (e.g.: test_search):

`python -m pytest testcases/test_search.py --html=report.html --self-contained-html`

## Select browser

In `webdriver.py` browser is selected by a line that looks like the following:

`self.instance = webdriver.Chrome()`

Uncomment (remove `#`) from the line with the browser you wish to use. Similarly, comment (add `#`) to the browser line you wish not to use.

> Please note: the `Safari WebDriver` extension is no longer supported on Safari versions under 10. Safari 10+ browser versions are available only for macOS. The driver is now by default shipped with the Mac OS.

## Notes

This project was developed using Python 3.8.6.
