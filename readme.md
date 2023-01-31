# Requirements

* Python 3

* Selenium (`pip install selenium`)

* Browser drivers: they are included in the `/resources` folder in the project. Add their path to PATH environment variable.


# Run project

In terminal, cd into the project's root folder and execute the following command to run all tests:

<pre>python -m unittest discover \testcases -v</pre>

To run a specific test file:

<pre>python -m unittest discover \testcases -p "test_addtocart.py" -v</pre>



## Run and generate test report

In order to get an html report, instead of using `unittest`'s runner, use `pytest`'s runner with html-report option enabled (`report.html` file will be generated in the project root folder):

_(please note: this method requires Pytest (`pip install pytest`) and Pytest Html Report (`pip install pytest-html`)._

<pre>python -m pytest testcases --html=report.html --self-contained-html</pre>

To run a specific test file (e.g.: test_search):

<pre>python -m pytest testcases/test_search.py --html=report.html --self-contained-html</pre>


## Select browser

In `webdriver.py` browser is selected by a line that looks like the following: 
<pre>self.instance = webdriver.Chrome()</pre>

Uncomment (remove `#`) from the line with the browser you wish to use. Similarly, comment (add `#`) 
to the browser line you wish not to use.

> Please note: the `Safari WebDriver` extension is no longer supported on Safari versions under 10. Safari 10+ browser
>versions are available only for macOS. The driver is now by default shipped with the Mac OS.


# Notes

This project was developed using Python 3.8.6 and Selenium 3.141.0

Keep in mind that the driver you use must be compatible with the browser installed. If you get an error when running the project, try [downloading an updated version of the driver](https://pypi.org/project/selenium/).
