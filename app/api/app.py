from fastapi import FastAPI


app = FastAPI()


@app.get("/hello")
def get_hello():
    print('message received')
    return "Cheems sayms: remsponse"
