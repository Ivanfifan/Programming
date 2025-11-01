from google import genai

client = genai.Client(api_key="AIzaSyDrY7daQTpCQVd9QfLFbruraOhsm9Mz5ns")

response = client.models.generate_content(
    model="gemini-2.5-flash-lite", contents="бібізяна чічічі собірала кірпічі"
)
print(response.text)