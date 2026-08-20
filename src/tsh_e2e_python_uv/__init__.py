from io import StringIO

from pydantic import BaseModel, PositiveInt
from rich.console import Console


class BuildManifest(BaseModel):
    service: str
    attempts: PositiveInt


def main() -> None:
    manifest = BuildManifest.model_validate(
        {"service": "tsh-e2e-python-uv", "attempts": 3}
    )
    output = StringIO()
    Console(file=output, force_terminal=False, color_system=None).print(
        f"{manifest.service}:{manifest.attempts}"
    )
    assert output.getvalue().strip() == "tsh-e2e-python-uv:3"
    print("tsh-e2e-python-uv-ok")
