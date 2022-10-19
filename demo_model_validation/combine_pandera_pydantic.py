import pandas as pd
import pydantic
from dataframe_validation import MyValidator
from pandera.typing import DataFrame
from turbine_model import TurbineModel


class CombinedModel(pydantic.BaseModel):
    turbine: TurbineModel
    df: DataFrame[MyValidator]


if __name__ == "__main__":

    soil_layers = [
        {"depth": 0, "number_of_elements": 2},
        {"depth": 2, "number_of_elements": 3},
    ]

    simulation_steps = 20

    turbine_model = TurbineModel(
        soil_layers=soil_layers, load_step_num=simulation_steps
    )

    df = pd.DataFrame(
        {
            "column1": [1, 4, 0, 10, 9],
            "column2": [-1.4, -1.4, -2.9, -10.1, -3],
            "column3": ["value_1", "value_2", "value_3", "value_2", "value_1"],
        }
    )

    valid_combination = CombinedModel(turbine=turbine_model, df=df)

    print(f"valid combination : {valid_combination}")

    df_invalid = pd.DataFrame(
        {
            "column1": [1, 4, 0, 10, 9],
            "column2": [-1.4, -1.4, -2.9, -10.1, 3],
            "column3": ["value_1", "value_2", "value_3", "value_2", "value_1"],
        }
    )

    invalid_combination = CombinedModel(turbine=turbine_model, df=df_invalid)

    print(f"valid combination : {invalid_combination}")
