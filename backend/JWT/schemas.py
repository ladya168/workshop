from typing import Annotated

from fastapi import Depends

from JWT.auth import get_id


IdSchema = Annotated[int, Depends(get_id)]