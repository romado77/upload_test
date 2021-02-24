from aiohttp import web
from rororo import setup_openapi

import views


def create_app():
    app = setup_openapi(
        web.Application(),
        "./openapi.json",
        views.operations,
        use_cors_middleware=False,
        use_error_middleware=False,
    )

    app.router.add_view("/api/v2/", views.UploadView)
    return app


if __name__ == "__main__":
    app = create_app()
    web.run_app(app)
