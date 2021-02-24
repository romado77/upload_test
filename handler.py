from aiohttp import web


async def upload(request):

    filename = None

    content = request.content_type

    try:
        if content == "multipart/form-data":
            reader = await request.multipart()
            filename = await save_file(reader)
    except Exception as e:
        return web.Response(text=str(e), status=500)

    if filename:
        return web.Response(status=200)

    return web.Response(status=503)


async def save_file(reader):
    filename = None

    while True:
        part = await reader.next()

        if part is None:
            break
        elif part.name == "prt_file" or part.name == "zipFileName":
            filename = part.filename

            with open(filename, "wb") as f:
                while True:
                    chunk = await part.read_chunk()
                    if not chunk:
                        break
                    f.write(chunk)

    return filename