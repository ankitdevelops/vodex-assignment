import os
import uvicorn
from dotenv import load_dotenv

load_dotenv()
PORT = os.getenv("PORT")
if __name__ == "__main__":
    uvicorn.run("config.index:app", host="0.0.0.0", port=8000, reload=True)
