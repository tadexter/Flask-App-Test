from fastapi import FastAPI

app = FastAPI()


@app.get('/fetch')
def fetch_website():
    return {'welcome': 'Done!'}
