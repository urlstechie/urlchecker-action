# URLcheck

A GitHub action to collect and check URLs in a project (code and documentation).
The action aims at detecting and reporting broken links.



# Inputs

### `git_path`

 The path to the start directory of the project. ***[Required]***

### `file_types`

A comma-separated list of file types to cover in the URLs checks. ***[optional]***

### `print_all`
Choose whether to include file with no URLs in the prints. ***[optional]***

## Example usage
```
uses: actions/URLcheck@v1
with:
  git_path: "path link to project"
  file_types: ".md,.py,.rst"
  print_all: False
```
