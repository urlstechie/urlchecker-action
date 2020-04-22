# Examples

The following examples are added for your convenience. Each of these files
would be added to a .github/workflows folder to be run on some [github event](https://help.github.com/en/actions/reference/events-that-trigger-workflows).

## General

- [GitHub Checkout](urlchecker-checkout.yml): the most likely case of usage for this action is checking out the repository that the action is running for, meaning we use the active branch for the check.
- [GitHub Clone](urlchecker-clone.yml): while it's more a niche use case, you might want to clone one or more repos to check for an action run.

## White Listing

- [urlchecker-whitelist-files.yml](urlchecker-whitelist-files.yml): in this example, we have a repository where we want to check only a README.md file at the root, and importantly, skip over an entire subfolder that serves a rendered site at docs. We want to run the check whenever someone opens a pull request.

## Include Files

- [urlchecker-include-files.yml](urlchecker-include-files.yml): as an alternative to white listing files or patterns, you can specify an explicit file path or pattern to check. This is useful if you want to set some comma separated listing of files or patterns in another step, and then set for the action here.

## Saving

- [urlchecker-save-artifact.yml](urlchecker-save-artifact.yml) save an artifact on success for the results file.

## Pull request

- [urlchecker-pr-label.yml](urlchecker-pr-label.yml) checks URLs in files modified by a PR when you apply a "needs-url-checks" label, then it removes the "needs-url-checks" label. You need to create the label first. The PR can be labelled and unlabelled several times. The workflow creates a check run.

If you'd like to see an example added, please [open an issue](https://github.com/urlstechie/urlchecker-action/issues).
