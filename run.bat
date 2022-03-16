pytest -v -m "regression" --html="./Report/rep.html" testCases\ --browser chrome

::pytest -v -m "regression" --html="./Report/rep.html" testCases\ --browser firefox
::pytest -v -m "sanity" --html="./Report/rep.html" testCases\ --browser chrome

::pytest -v -m "regression and sanity" --html="./Report/rep.html" testCases\ --browser chrome
::pytest -v -m "regression or sanity" --html="./Report/rep.html" testCases\ --browser chrome