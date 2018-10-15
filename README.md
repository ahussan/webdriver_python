# webdriver_python

This is web automation framework, implemented using Python & Webdriver. Page Object Model (POM) is used to make the code more readable, maintainable, and reusable.

This automation testing framework is using Page Object Model Concept which can be used to execute cross browser and cross platform tests


## Requirements:

1. Python
2. pip
3. Selenium/WebDriver
4. ddt
5. Browsers (Firefox, Chrome, IE)
6. Respective Browser drivers
7. Pycharm - or any other text editor

### How to run?
**Test scripts can be executed by py.test:**

py.test -s -v tests/courses/<name of the python file.py> --browser firefox

**Execute different suite of test:**

To run test suite
py.test tests/test_suite_demo.py --browser firefox

This automation framework can also be used to execute Data Driven Testing


