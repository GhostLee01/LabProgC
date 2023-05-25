import openai
#Debe ejecutar "pip install openai" en la terminal para instalar la libreria

# Configurar la clave de API de OpenAI
#La cosigue en https://platform.openai.com/account/api-keys
api_key = 'aquí va la api key'

openai.api_key = api_key

def hacer_consulta(query):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=query,
        max_tokens=60
    )
    return response.choices[0].text.strip()

query_inicial = "El plastico PET"

# Consultas relacionadas basadas en la respuesta inicial
consulta_1 = hacer_consulta("Qué es " + query_inicial + "?")
consulta_2 = hacer_consulta("Otros usos de " + query_inicial + ".")
consulta_3 = hacer_consulta("Más información sobre " + query_inicial + ".")

# Realiza otras dos consultas independientes
consulta_4 = "¿Cuál es la capital de Francia?"
respuesta_4 = hacer_consulta(consulta_4)

consulta_5 = "Dime 3 alimentos saludables."
respuesta_5 = hacer_consulta(consulta_5)

print("Consulta relacionada 1:", consulta_1)
print("Consulta relacionada 2:", consulta_2)
print("Consulta relacionada 3:", consulta_3)
print("Respuesta 4:", respuesta_4)
print("Respuesta 5:", respuesta_5)
