from .articles import router as articles_router
from .mailing import router as mailing_router
from .tags import router as tags_router
from .files import router as files_router

MAIN_ROUTER = [
    articles_router,
    mailing_router,
    tags_router,
    files_router
]