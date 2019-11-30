[![Build Status](https://travis-ci.org/SuperKogito/URLs-checker.svg?branch=master)](https://travis-ci.org/SuperKogito/URLs-checker)
[![codecov](https://codecov.io/gh/SuperKogito/URLs-checker/branch/master/graph/badge.svg)](https://codecov.io/gh/SuperKogito/URLs-checker)
# URLs-checker

A GitHub action to collect and check URLs in a project (code and documentation).
The action aims at detecting and reporting broken links.

# How to use?

```
  name: Check URLs

  on: [push]

  jobs:
    build:
      runs-on: ubuntu-latest

      steps:
      - name: URLs-checker
        uses: actions/URLs-checker@master
        with:
          # The project base path.
          git_path: https://github.com/SuperKogito/SuperKogito.github.io

          # A comma-separated list of file types to cover in the URL checks
          file_types: .md,.py,.rst

          # Choose whether to include file with no URLs in the prints.
          print_all: False
```
## Inputs

| variable name | variable type                                |      variable description                                        |
|---------------|----------------------------------------------|------------------------------------------------------------------|
| `git_path`    | <span style="color:red"> required </span>    | The path to the start directory of the project.                  |
| `file_types`  | <span style="color:green"> optional </span>  | A comma-separated list of file types to cover in the URLs checks.|
| `print_all`   | <span style="color:green"> optional </span>  | Choose whether to include file with no URLs in the prints.       |

## Demo

<img src="demo.gif"/>
