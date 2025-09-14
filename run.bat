@echo off
call venv\scripts\activate
pytest -s -v -m "sanity" --html .\reports\test_report_chrome.html --browser chrome
rem "the \ is used while you want to create reports from outside pycharm"
rem "the / is used while you want to create reports from inside pycharm"
rem pytest -s -v -m "regression" --html .\reports\test_report_chrome.html --browser chrome
rem pytest -s -v -m "sanity and regression" --html .\reports\test_report_chrome.html --browser chrome
rem pytest -s -v -m "sanity or regression" --html .\reports\test_report_chrome.html --browser chrome
pause