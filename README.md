[![GitHub Marketplace](https://img.shields.io/static/v1?label=Marketplace&message=urlchecker-action&color=blue?style=flat&logo=github)](https://github.com/marketplace/actions/urlchecker-action)
[![CodeFactor](https://www.codefactor.io/repository/github/urlstechie/urlchecker-action/badge)](https://www.codefactor.io/repository/github/urlstechie/urlchecker-action)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](https://github.com/urlstechie/urlchecker-action/blob/master/LICENSE)

# urlchecker-action

A GitHub action to collect and check URLs in a project (code and documentation).
The action aims at detecting and reporting broken links.

## How to use it?

A set of examples are included in the [examples](examples) folder. A few detailed
examples are also included below. Note that examples always reference the master branch,
however you should change them to reference a [release](https://github.com/urlstechie/urlchecker-action/releases).

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
      uses: urlstechie/urlchecker-action@master
      with:
        # A subfolder or path to navigate to in the present or cloned repository
        subfolder: docs

        # A comma-separated list of file types to cover in the URL checks
        file_types: .md,.py,.rst

        # Whether to include files without URLs in the action output
        print_all: false

        # The timeout seconds to provide to requests, defaults to 5 seconds
        timeout: 5

        # How many times to retry a failed request (each is logged, defaults to 1)
        retry_count: 3

        # A comma-separated list of URLs to exclude from checks
        exclude_urls: https://github.com/SuperKogito/URLs-checker/issues/1,https://github.com/SuperKogito/URLs-checker/issues/2

        # A comma-separated list of substrings that exclude matching URLs from checks
        exclude_patterns: localhost:3030,https://github.com/SuperKogito/Voice-based-gender-recognition/issues

        # Whether to force success, even if broken links are found
        force_pass : true
```

Note that as of version 0.2.2, references to `white_listed_*` have been changed to
`exclude_*` to be consistent with the `include_*` variables.


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
      uses: urlstechie/urlchecker-action@master
      with:
        # A project to clone. If not provided, assumes already cloned in the present working directory.
        git_path: https://github.com/urlstechie/URLs-checker-test-repo

        # If a git_path is defined to clone, clone this branch (defaults to master)
        branch: devel

        # A subfolder or path to navigate to in the present or cloned repository
        subfolder: docs

        # Whether to delete the cloned repo after the check (default is `false`)
        cleanup: true

        # A comma-separated list of file types to cover in the URL checks
        file_types: .md,.py,.rst

        # Whether to include files without URLs in the action output
        print_all: false

        # The timeout seconds to provide to requests (in seconds, defaults to `5`)
        timeout: 5

        # How many times to retry a failed request (each is logged, defaults to `1`)
        retry_count: 3

        # A comma-separated list of URLs to exclude from checks
        exclude_urls: https://github.com/SuperKogito/URLs-checker/issues/1,https://github.com/SuperKogito/URLs-checker/issues/2

        # A comma-separated list of substrings that exclude matching URLs from checks
        exclude_patterns: https://github.com/SuperKogito/Voice-based-gender-recognition/issues

        # A comma-separated list of file paths to exclude from checks (supports regex)
        exclude_files: README.md,/github/workspace/_config.yml

        # Whether to force success, even if broken links are found
        force_pass : true
```
## Inputs


| variable name               | variable type                                |      variable description                                                             |
|-----------------------------|----------------------------------------------|---------------------------------------------------------------------------------------|
| `git_path`                  | <span style="color:green"> optional </span>  | Git URL to clone (if the repository isn't already in `$PWD`)                          |
| `branch`                    | <span style="color:green"> optional </span>  | Branch to clone (if `git_path` is used, defaults to `master`)                         |
| `cleanup`                   | <span style="color:green"> optional </span>  | Whether to delete the cloned repo after the check (defaults to `false`)               |
| `subfolder`                 | <span style="color:green"> optional </span>  | Subfolder to navigate to in the repository to check                                   |
| `file_types`                | <span style="color:green"> optional </span>  | Comma-separated list of file types to check                                           |
| `include_files`             | <span style="color:green"> optional </span>  | Comma-separated list of files to check (supports regex)                               |
| `print_all`                 | <span style="color:green"> optional </span>  | Whether to include files without URLs in the action output (defaults to `true`)       |
| `retry_count`               | <span style="color:green"> optional </span>  | Number of times to retry a request upon failure (defaults to `3`)                     |
| `save`                      | <span style="color:green"> optional </span>  | File path where `.csv` results are written                                            |
| `timeout`                   | <span style="color:green"> optional </span>  | Request timeout (in seconds, defaults to `1`)                                         |
| `exclude_urls`              | <span style="color:green"> optional </span>  | Comma-separated list of URLs to exclude                                               |
| `exclude_patterns`          | <span style="color:green"> optional </span>  | Comma-separated list of substrings that exclude matching URLs                         |
| `exclude_files`             | <span style="color:green"> optional </span>  | Comma-separated list of file paths to exclude (supports regex)                        |
| `force_pass`                | <span style="color:green"> optional </span>  | Whether to force action success, even if broken links are found (defaults to `false`) |

## Demo
- Using version > 0.1.4
<img src="demo2.gif"/>

- Using version =< 0.1.4
<img src="demo.gif"/>

## Support

Do you have a question or an issue? Please [open an issue](https://github.com/urlstechie/urlchecker-action/issues) and we can help!
The following communities are using the url checker! You can look here for examples
or inspiration. If you want to add your community, please let us know with an issue.

| Repository                                                                                          | Workflow (with permalink to YAML) | Example runs |
|-----------------------------------------------------------------------------------------------------|-----------------------------------|-------------|
| [awesome-rseng](https://github.com/rseng/awesome-rseng)  | [Check URLs in PRs, exclude docs](https://github.com/rseng/awesome-rseng/blob/5f5cb78f8392cf10aec2f3952b305ae9611029c2/.github/workflows/urlchecker.yml)                                   | [Logs](https://github.com/rseng/awesome-rseng/actions?query=workflow%3AURLChecker) |
| [buildtest](https://github.com/buildtesters/buildtest) |  [Check URLs in all commits](https://github.com/buildtesters/buildtest/blob/v0.9.1/.github/workflows/urlchecker.yml)  |  [Logs](https://github.com/HPC-buildtest/buildtest-framework/actions?query=workflow%3A%22Check+URLs%22)           |
| [us-rse](https://github.com/USRSE/usrse.github.io) |  [Check URLs in PRs, exclude some URL patterns](https://github.com/USRSE/usrse.github.io/blob/abcbed5f5703e0d46edb9e8850eea8bb623e3c1c/.github/workflows/urlchecker.yml)                                 |      [Logs](https://github.com/USRSE/usrse.github.io/actions?query=workflow%3A%22Check+URLs%22)       |
| [R-hub docs](https://github.com/r-hub/docs)  | [Check URLs when on PR labelling](https://github.com/r-hub/docs/blob/bc1eac71206f7cb96ca00148dcf3b46c6d25ada4/.github/workflows/pr.yml) |  [Logs](https://github.com/r-hub/docs/actions?query=workflow%3ACommands)  |
| [Berlin Hack & Tell](https://github.com/berlin-hack-and-tell/berlinhackandtell.rocks)  | [Check URLs when on PR labelling](https://github.com/berlin-hack-and-tell/berlinhackandtell.rocks/blob/master/.github/workflows/urlchecker-pr-label.yml) |  [Logs](https://github.com/berlin-hack-and-tell/berlinhackandtell.rocks/actions?query=workflow%3ACommands)  |
