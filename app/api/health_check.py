from fastapi import APIRouter

health_check_router = APIRouter(
    prefix="/health",
)


@health_check_router.get(
    "/",
)
def health_checking():
    try:
        # TODO: should add any logic for checking service healh
        return True
    except Exception as e:
        return False
