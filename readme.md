# Requirements

* Python 3

* Selenium (pip install selenium)

* Browsers: Chrome, Firefox.

* Browser drivers: they are included in the `/resources` folder in the project. Add their path to PATH environment variable.


# Run project

In terminal, cd into the project's root folder and execute file `runner.py`:

<pre>python runner.py</pre>


## Run and generate test report

In order to get an html report, instead of using the provided runner, use `pytest`'s runner with html-report option:

_(please note: this method requires Pytest (`pip install pytest`) and Pytest Html Report (`pip install pytest-html`)._

<pre>python -m pytest testcases --html=report.html --self-contained-html</pre>

To run a specific file (e.g.: test_search):

<pre>python -m pytest testcases/test_search.py --html=report.html --self-contained-html</pre>


## Select browser

In `webdriver.py` browser is selected by a line that looks like the following: 
<pre>self.instance = webdriver.Chrome()</pre>

Uncomment (remove `#`) from the line with the browser you wish to use. Similarly, comment (add `#`) 
to the browser line you wish not to use.

> Please note: the `Safari WebDriver` extension is no longer supported on Safari versions under 10. Safari 10+ browser
>versions are available only for macOS. The driver is now by default shipped with the Mac OS.
