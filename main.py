
from openai import OpenAI
import getpass


OPENAI_API_KEY = getpass.getpass('Введите ваш OpenAI API ключ: ')
client = OpenAI(api_key=OPENAI_API_KEY)




def classify_sentiment_with_openai(text):
    completion = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "Вы эксперт в определении настроения. Вам будет дан текст, и вы должны определить его настроение как 'positive' или 'negative'. Верни ответ в формате json с полем mode, в котором будет указано настроение (positive или negative)"},
                        {"role": "user", "content": text}
                    ],
                    response_format={"type": "json_object"},
                )
    response_message = completion.choices[0].message.content
    print(response_message)
    try:
        sentiment = eval(response_message)['mode']
    except:
        sentiment = 'positive'
    return sentiment
    

# print(classify_sentiment_with_openai('ачрван'))

def generate_response(text, role):
    response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                         {"role": "user", "content": f"Ответь на сообщение, как {role}. Сообщение: {text}"}
                    ],

                )
    response_message = response.choices[0].message.content
    return response_message


def respond_to_query(query):
    sentiment = classify_sentiment_with_openai(query)
    
    if sentiment == 'positive':
        role = 'Бетмен'
    else:
        role = 'Джокер'
    
    return generate_response(query, role)



test_queries = [
    "Я заболела (( Горлышко болит",
    "Ура! Наконец, я выполняю тестовое задание для УИИ!",
    "Скоро сентябрь, и снова эта школа ((",
    "А лето-то какое хорошее в этом году!",
    "Представляешь, я такой крутой код написала!",
    "Кот опять бесится!",
    "Ох, забыла сахар купить.",
    "Как же я рада тебя видеть!",
    "Вот думаю, как же мне мой день рождения необычно отпраздновать",
    "Спасибо тебе огромное!"
]



for query in test_queries:
    response = respond_to_query(query)

    print(f"Query: {query}\nResponse: {response}\n")