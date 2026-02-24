import pandera.pandas as pa
from pandera.typing import Series


class VendasSchema(pa.DataFrameModel):
    Produto: Series[str]
    Categoria: Series[str]
    Quantidade: Series[int] = pa.Field(ge=0)
    Venda: Series[int] = pa.Field(ge=0)
    Data: Series[str]

    class Config:
        coerce = True
        strict = True