[![GitHub Marketplace](https://img.shields.io/static/v1?label=Marketplace&message=urlchecker-action&color=blue?style=flat&logo=github)](https://github.com/marketplace/actions/urlchecker-action)
[![CodeFactor](https://www.codefactor.io/repository/github/urlstechie/urlchecker-action/badge)](https://www.codefactor.io/repository/github/urlstechie/urlchecker-action)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](https://github.com/urlstechie/urlchecker-action/blob/master/LICENSE)

# urlchecker-action

A GitHub action to collect and check URLs in a project (code and documentation).
The action aims at detecting and reporting broken links.

## How to use it?

A set of examples are included in the [examples](examples) folder. A few detailed 
examples are also included below.

### Example with Checkout

For most use cases, you will want to use the git repository that is being checked
for a GitHub actions, and we do this by way of the [actions/checkout](https://github.com/actions/checkout) action.

```
name: Check URLs

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: urls-checker
      uses: urlstechie/urlchecker-action@0.1.9
      with:
        # A subfolder or path to navigate to in the present or cloned repository
        subfolder: docs

        # A comma-separated list of file types to cover in the URL checks
        file_types: .md,.py,.rst

        # Choose whether to include file with no URLs in the prints.
        print_all: false

        # The timeout seconds to provide to requests, defaults to 5 seconds
        timeout: 5

        # How many times to retry a failed request (each is logged, defaults to 1)
        retry_count: 3

        # A comma separated links to exclude during URL checks
        white_listed_urls: https://github.com/SuperKogito/URLs-checker/issues/1,https://github.com/SuperKogito/URLs-checker/issues/2

        # A comma separated patterns to exclude during URL checks
        white_listed_patterns: https://github.com/SuperKogito/Voice-based-gender-recognition/issues

        # choose if the force pass or not
        force_pass : true
```


### Example with Custom Clone

It could, however, be the case that you've set up a repository with one or more uses of the URLChecker
that must clone one or more repos (possibly with varying branches) before doing the check.
In this case, you might want to define `git_path` and `branch` for each section.
An example is below:

```
name: Check URLs

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: URLs-checker
      uses: urlstechie/urlchecker-action@0.1.9
      with:
        # A project to clone. If not provided, assumes already cloned in the present working directory.
        git_path: https://github.com/urlstechie/URLs-checker-test-repo

        # If a git_path is defined to clone, clone this branch (defaults to master)
        branch: devel

        # A subfolder or path to navigate to in the present or cloned repository
        subfolder: docs

        # Delete the cloned repository after running URLchecked (default is false)
        cleanup: true

        # A comma-separated list of file types to cover in the URL checks
        file_types: .md,.py,.rst

        # Choose whether to include file with no URLs in the prints.
        print_all: false

        # The timeout seconds to provide to requests, defaults to 5 seconds
        timeout: 5

        # How many times to retry a failed request (each is logged, defaults to 1)
        retry_count: 3

        # A comma separated links to exclude during URL checks
        white_listed_urls: https://github.com/SuperKogito/URLs-checker/issues/1,https://github.com/SuperKogito/URLs-checker/issues/2

        # A comma separated patterns to exclude during URL checks
        white_listed_patterns: https://github.com/SuperKogito/Voice-based-gender-recognition/issues

        # A comma separated list of file patterns (direct paths work as well) to exclude
        white_listed_files: README.md,/github/workspace/_config.yml

        # choose if the force pass or not
        force_pass : true
```
## Inputs


| variable name               | variable type                                |      variable description                                        |
|-----------------------------|----------------------------------------------|------------------------------------------------------------------|
| `git_path`                  | <span style="color:green"> optional </span>  | A git url to clone, if the repository isn't already in $PWD      |
| `branch`                    | <span style="color:green"> optional </span>  | If we do a clone, clone this branch (defaults to master          |
| `cleanup`                   | <span style="color:green"> optional </span>  | If we do a clone, delete the cloned folder after (false)         |
| `subfolder`                 | <span style="color:green"> optional </span>  | A subfolder to navigate to in the repository to check            |
| `file_types`                | <span style="color:green"> optional </span>  | A comma-separated list of file types to cover in the URLs checks.|
| `print_all`                 | <span style="color:green"> optional </span>  | Choose whether to include file with no URLs in the prints.       |
| `retry_count`               | <span style="color:green"> optional </span>  | If a request fails, retry this number of times. Defaults to 1    |
| `save`                      | <span style="color:green"> optional </span>  | A path to a csv file to save results to                          |
| `timeout`                   | <span style="color:green"> optional </span>  | The timeout to provide to requests to wait for a response.       |
| `white_listed_urls`         | <span style="color:green"> optional </span>  | A comma separated links to exclude during URL checks.            |
| `white_listed_patterns`     | <span style="color:green"> optional </span>  | A comma separated patterns to exclude during URL checks.         |
| `white_listed_files`        | <span style="color:green"> optional </span>  | Full paths to files to exclude (comma separated list).           |
| `force_pass`                | <span style="color:green"> optional </span>  | Choose whether to force a pass when checks are done.             |

## Demo
- Using version > 0.1.4
<img src="demo2.gif"/>

- Using version =< 0.1.4
<img src="demo.gif"/>

## Support

Do you have a question or an issue? Please [open an issue](https://github.com/urlstechie/urlchecker-action/issues) and we can help!
The following communities are using the url checker! You can look here for examples
or inspiration. If you want to add your community, please let us know with an issue.

- [awesome-rseng](https://github.com/rseng/awesome-rseng)
- [buildtest](https://github.com/HPC-buildtest/buildtest-framework)
- [The United States Research Software Engineer Assocation](https://github.com/USRSE/usrse.github.io)
