# Pre-commit hooks with Python

This repo contains an example set-up for using pre-commit hooks with your python environment.

The file `.pre-commit-config.yaml` controls the type of pre-commit you are currently using. There exists [several](https://towardsdatascience.com/pre-commit-hooks-you-must-know-ff247f5feb7e) ways to do automatic formatting with Python. This is just an example.

Original documentation for [pre-commit](https://pre-commit.com/).

## Usage

Start with activating the virtual environment and installing needed packages from the `Pipfile` and `Pipefile.lock`

```
sunnivin@NGI-R910LQ9W:~/NGI/pre-commit(main)$ pipenv shell
(pre-commits-python-example)sunnivin@NGI-R910LQ9W:~/NGI/pre-commit(main)$ pipenv install
```

### Automatic run each time you try to commit something
```
(pre-commits-python-example)sunnivin@NGI-R910LQ9W:~/NGI/pre-commit(main)$ pre-commit install
```
To later bypass the hook use the `--no-verify` option
```
(pre-commits-python-example)sunnivin@NGI-R910LQ9W:~/NGI/pre-commit(main)$ git commit -m "wip: quick fix of data" --no-verify
```

### Manual run
You can do a manual `pre-commit` run on all files with the command
```
(pre-commits-python-example)sunnivin@NGI-R910LQ9W:~/NGI/pre-commit(main)$ pre-commit run --all-files
```
