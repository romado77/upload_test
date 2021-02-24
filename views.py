from aiohttp import web
from rororo import OperationTableDef

import handler

operations = OperationTableDef()


@operations.register("root")
class RootView(web.View):
    async def post(self) -> web.Response:
        response = await handler.upload(self.request)
        return response


class UploadView(web.View):
    async def post(self) -> web.Response:
        response = await handler.upload(self.request)
        return response