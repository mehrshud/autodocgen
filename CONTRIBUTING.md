# Contributing to AutoDocGen
=====================================

Thank you for considering contributing to AutoDocGen, the AI-powered documentation generator for open-source projects. We appreciate your help in making this project better.

## Setup
---------

To get started, you'll need to have the following dependencies installed:

* Python 3.9+
* Redis
* Celery

You can install the required Python packages using pip:
pip install -r requirements.txt
Then, set up your local environment:
python setup.py develop
Make sure to also install the pre-commit hook to ensure code quality:
pre-commit install

## Branch Naming Conventions
---------------------------

We follow a specific branch naming convention to keep our repository organized. Use the following prefixes for your branches:

* `feat/` for new features
* `fix/` for bug fixes
* `docs/` for documentation changes
* `refactor/` for code refactoring
* `test/` for test additions or modifications
* `chore/` for miscellaneous changes

Example branch names:
feat/new-documentation-feature
fix/missing-import
docs/update-README

## Conventional Commits
----------------------

We use Conventional Commits to keep our commit messages consistent and informative. Commit messages should follow this format:
type(scope): brief description

body
Where `type` is one of:

* `feat` for new features
* `fix` for bug fixes
* `docs` for documentation changes
* `refactor` for code refactoring
* `test` for test additions or modifications
* `chore` for miscellaneous changes

Example commit message:
feat(doc generation): add support for markdown tables

* Added markdown table support to doc generation
* Updated tests to cover new functionality

## Pull Request Checklist
-------------------------

Before submitting a pull request, make sure to:

* Run `pre-commit` to ensure code quality and formatting
* Run `pytest` to ensure tests pass
* Update documentation where necessary
* Follow Conventional Commits for commit messages
* Use a clear and descriptive pull request title and description
* Link to any relevant issues or discussions

### PR Template

When creating a pull request, use the following template:
## Description

* Briefly describe the changes made in this PR

## Related Issues

* Link to any relevant issues or discussions

## Changes

* List the changes made in this PR
Example PR:
## Description

 Added support for markdown tables in doc generation

## Related Issues

* Closes #123

## Changes

* Added markdown table support to doc generation
* Updated tests to cover new functionality

## Code of Conduct
------------------

By contributing to AutoDocGen, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). We strive to maintain a welcoming and inclusive community, and we appreciate your help in keeping our community positive and respectful.