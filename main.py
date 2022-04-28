from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder

from starlette.responses import JSONResponse

from src.api import router


def create_app():
    application = FastAPI(title='chat', version="1")

    @application.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request,
                                           exc: RequestValidationError):
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder(
                {"detail": exc.errors(), "body": exc.body}),
        )

    application.include_router(router.router)

    return application


app = create_app()
