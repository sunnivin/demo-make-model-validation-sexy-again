# Demo make model validation sexy again

This repository contains some simple examples of how you can use [`pydantic`](https://pydantic-docs.helpmanual.io/) and [`pandera`](https://pandera.readthedocs.io/en/stable/dataframe_schemas.html) for data model validation.

## Usage
Start with activating the virtual environment and installing needed packages from the `pyproject.toml` and `poetry.lock`

    sunnivin@NGI-R910LQ9W:~/demo-make-model-validation-sexy-again(main)$ poetry shell
    (demo-model-validation)sunnivin@NGI-R910LQ9W:~/demo-make-model-validation-sexy-again$ poetry install


You can now play with the data models in the `demo_model_validation`-folder

    (demo-model-validation)sunnivin@NGI-R910LQ9W:~/demo-make-model-validation-sexy-again$ python demo_model_validation/turbine_model.py
    My turbine model: soil_layers=[SoilLayer(depth=0.0, number_of_elements=2), SoilLayer(depth=2.0, number_of_elements=3)] load_step_num=20


## Development usage

This repo contains an example set-up for using pre-commit hooks with your python environment.

The file `.pre-commit-config.yaml` controls the type of pre-commit you are currently using. There exists [several](https://towardsdatascience.com/pre-commit-hooks-you-must-know-ff247f5feb7e) ways to do automatic formatting with Python. This is just an example.

Original documentation for [pre-commit](https://pre-commit.com/).

### Automatic run each time you try to commit something

Make sure that you have activated your virtual environment first (see usage)

    (demo-model-validation)sunnivin@NGI-R910LQ9W:~/NGI/demo-make-model-validation-sexy-again(main)$ pre-commit install

To later bypass the hook use the `--no-verify` option
    (demo-model-validation)sunnivin@NGI-R910LQ9W:~/NGI/demo-make-model-validation-sexy-again(main)$ git commit -m "wip: my quick fix" --no-verify

### Manual run
You can do a manual `pre-commit` run on all files with the command

    (demo-model-validation)sunnivin@NGI-R910LQ9W:~/demo-make-model-validation-sexy-again(main)$ pre-commit run --all-files

or you can run only `mypy`

    (demo-model-validation)sunnivin@NGI-R910LQ9W:~/demo-make-model-validation-sexy-again(main)$ pre-commit run mypy --all
    mypy.....................................................................Passed
