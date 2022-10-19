from pydantic import BaseModel, Field


class SoilLayer(BaseModel):
    depth: float = Field(description="Depth from seabed to soil later")
    number_of_elements: int = Field(
        description="Number of elements of this material at this depth"
    )


class TurbineModel(BaseModel):
    soil_layers: list[SoilLayer]
    load_step_num: int = Field(
        default=20, ge=0, description="Number of load steps in cycle"
    )


soil_layers = [
    {"depth": 0, "number_of_elements": 2},
    {"depth": 2, "number_of_elements": 3},
]

simulation_steps = -20

turbine_model = TurbineModel(soil_layers=soil_layers, load_step_num=simulation_steps)

print(f"My turbine model: {turbine_model}")
