import uvicorn


uvicorn.run(
    'app.main:app',
    host='localhost',
    port=7000,
    reload=True,
)