[![Build Status](https://travis-ci.org/SuperKogito/URLs-checker.svg?branch=master)](https://travis-ci.org/SuperKogito/URLs-checker)
[![codecov](https://codecov.io/gh/SuperKogito/URLs-checker/branch/master/graph/badge.svg)](https://codecov.io/gh/SuperKogito/URLs-checker)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-URLs--checker-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAM6wAADOsB5dZE0gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAERSURBVCiRhZG/SsMxFEZPfsVJ61jbxaF0cRQRcRJ9hlYn30IHN/+9iquDCOIsblIrOjqKgy5aKoJQj4O3EEtbPwhJbr6Te28CmdSKeqzeqr0YbfVIrTBKakvtOl5dtTkK+v4HfA9PEyBFCY9AGVgCBLaBp1jPAyfAJ/AAdIEG0dNAiyP7+K1qIfMdonZic6+WJoBJvQlvuwDqcXadUuqPA1NKAlexbRTAIMvMOCjTbMwl1LtI/6KWJ5Q6rT6Ht1MA58AX8Apcqqt5r2qhrgAXQC3CZ6i1+KMd9TRu3MvA3aH/fFPnBodb6oe6HM8+lYHrGdRXW8M9bMZtPXUji69lmf5Cmamq7quNLFZXD9Rq7v0Bpc1o/tp0fisAAAAASUVORK5CYII=)](https://github.com/marketplace/actions/urls-checker)
[![Python](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue)](https://www.python.org/doc/versions/)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](https://github.com/SuperKogito/URLs-checker/blob/master/LICENSE)
[![CodeFactor](https://www.codefactor.io/repository/github/superkogito/urls-checker/badge/master)](https://www.codefactor.io/repository/github/superkogito/urls-checker/overview/master)

# URLs-checker

A GitHub action to collect and check URLs in a project (code and documentation).
The action aims at detecting and reporting broken links.

# How to use?
## Example
```
name: Check URLs

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: URLs-checker
      uses: SuperKogito/URLs-checker@0.1.2
      with:
        # The project base path.
        git_path: https://github.com/SuperKogito/SuperKogito.github.io

        # A comma-separated list of file types to cover in the URL checks
        file_types: .md,.py,.rst

        # Choose whether to include file with no URLs in the prints.
        print_all: false

        # The timeout seconds to provide to requests, defaults to 5 seconds
        timeout: 5

        # How many times to retry a failed request (each is logged, defaults to 1)
        retry_count: 3

        # A comma separated links to exclude during URL checks
        white_listed_urls: https://superkogito.github.io/figures/fig2.html,https://superkogito.github.io/figures/fig4.html

        # A comma separated patterns to exclude during URL checks
        white_listed_patterns: https://superkogito.github.io/tables
        
        # choose if the force pass or not 
        force_pass = true
```
## Inputs

| variable name              | variable type                                |      variable description                                        |
|----------------------------|----------------------------------------------|------------------------------------------------------------------|
| `git_path`                 | <span style="color:red"> required </span>    | The path to the start directory of the project.                  |
| `file_types`               | <span style="color:green"> optional </span>  | A comma-separated list of file types to cover in the URLs checks.|
| `print_all`                | <span style="color:green"> optional </span>  | Choose whether to include file with no URLs in the prints.       |
| `retry_count`              | <span style="color:green"> optional </span>  | If a request fails, retry this number of times. Defaults to 1    |
| `timeout`                  | <span style="color:green"> optional </span>  | The timeout to provide to requests to wait for a response.       |
| `white_listed_urls`        | <span style="color:green"> optional </span>  | A comma separated links to exclude during URL checks.            |
| `white_listed_patterns`    | <span style="color:green"> optional </span>  | A comma separated patterns to exclude during URL checks.         |
| `force_pass`               | <span style="color:green"> optional </span>  | Choose whether to force a pass when checks are done.             |

## Demo

<img src="demo.gif"/>
