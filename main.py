from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def fetch_website():
    return {'welcome': 'Done!'}
