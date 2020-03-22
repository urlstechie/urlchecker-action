# Examples

The following examples are added for your convenience. Each of these files
would be added to a .github/workflows folder to be run on some [github event](https://help.github.com/en/actions/reference/events-that-trigger-workflows).

## General

- [GitHub Checkout](urlchecker-checkout.yml): the most likely case of usage for this action is checking out the repository that the action is running for, meaning we use the active branch for the check.
- [GitHub Clone](urlchecker-clone.yml): while it's more a niche use case, you might want to clone one or more repos to check for an action run.

## White Listing

- [urlchecker-whitelist-files.yml](urlchecker-whitelist-files.yml): in this example, we have a repository where we want to check only a README.md file at the root, and importantly, skip over an entire subfolder that serves a rendered site at docs. We want to run the check whenever someone opens a pull request.

If you'd like to see an example added, please [open an issue](https://github.com/urlstechie/urlchecker-action/issues).
