import pandas as pd
import pandera as pa
from pandera.typing import Series

df = pd.DataFrame(
    {
        "column1": [1, 4, 0, 10, 9],
        "column2": [-1.4, -1.4, -2.9, -10.1, -3],
        "column3": ["value_1", "value_2", "value_3", "value_2", "value_1"],
    }
)


class MyValidator(pa.SchemaModel):

    column1: Series[int] = pa.Field(le=10)
    column2: Series[float] = pa.Field(lt=-1.2)
    column3: Series[str] = pa.Field(str_startswith="value_")


if __name__ == "__main__":

    print(f"my dataframe before validation:\n {df}")

    df_valid = MyValidator.validate(df)

    print(f"my validated dataframe:\n {df_valid}")
