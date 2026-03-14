import google.generativeai as genai
genai.configure(api_key="AIzaSyCag3FVXY11kmuUElj_y9zLATr5DZOdWm4")
def get_model():
    model=genai.GenerativeModel("gemini-3.1-flash-lite-preview")
    return model
