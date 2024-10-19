from aiogram import Router


def get_handlers_router() -> Router:
    from . import common, uptime

    router = Router()
    router.include_router(common.router)
    router.include_router(uptime.router)

    return router
