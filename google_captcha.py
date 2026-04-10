from google import genai
from PIL import Image

solved_text = ""

# add your api here at the inside of:  ""
client = genai.Client(api_key="")

def captcha_sender():
    global solved_text
    captcha_image = Image.open("cap.png")

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=[
        "What does the Captcha Says ? Only write the text.",
        captcha_image
        ]
    )
    solved_text = response.text
    print(solved_text)
    return solved_text

def get_solved_text():
    return solved_text
