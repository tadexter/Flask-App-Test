from fastapi import FastAPI

app = FastAPI()


@app.route('/fetch')
def fetch_website():
    return {'welcome': 'Done!'}
