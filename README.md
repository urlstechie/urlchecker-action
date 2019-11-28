# URLcheck

A GitHub action to collect and check URLs in a project (code and documentation).
The action aims at detecting and reporting broken links.

# Inputs

| variable name | variable type                                |      variable description                                      |
|---------------|----------------------------------------------|----------------------------------------------------------------|
| `git_path`    | <span style="color:red"> required </span>  | The path to the start directory of the project.                  |
| `file_types`  | <span style="color:green"> optional </span>| A comma-separated list of file types to cover in the URLs checks.|
| `print_all`   | <span style="color:green"> optional </span>| Choose whether to include file with no URLs in the prints.       |

## Example usage

```
uses: actions/URLcheck@v1
with:
  git_path: "path link to project"
  file_types: ".md,.py,.rst"
  print_all: False
```

## Demo

<img src="demo.gif" width="1100" height="600" />
