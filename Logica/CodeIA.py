import openai

# Substitua 'sua-chave-api-aqui' pela sua chave de API real
openai.api_key = 'sk-caiooooo-NRD2I6My8B7YlWwaYhl5T3BlbkFJctp1WRJcsUkdxoFMhcDl'

def testar_chave_api():
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": "Diga olá!"}
            ]
        )
        print("A chave API está funcionando corretamente!")
        print("Resposta da IA:", resposta.choices[0].message['content'].strip())
    except Exception as e:
        print(f"Erro ao tentar verificar a chave API: {e}")

testar_chave_api()
