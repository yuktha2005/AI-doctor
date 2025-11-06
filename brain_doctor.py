import os
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

import base64
image_path="acne.jpg"
image_file=open(image_path,"rb")
encoded_image= base64.b64encode(image_file.read()).decode("utf-8")

from groq import Groq

client=Groq()
model="qwen/qwen3-32b"


