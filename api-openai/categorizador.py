from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
cliente = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))
modelo = 'gpt-3.4-turbo'

prompt_sistema = """
    Você é um categorizador de produtos.
    Você deve assumir as categorias presentes na lista abaixo.

    # Lista de categorias válidas
    - Moda sustentável
    - Produtos para o lar
    - Beleza natural
    - Eletrônicos verdes
    - Higiene pessoal

    # Formato de saída
    Produto: Nome do produto
    Categoria: apresente a categoria do produto

    # Exemplo de saída
    Produto: Escova elétrica com recarga solar
    Categoria: Eletrônicos verdes
"""

prompt_usuario = input("Apresente o nome de um produto: ")

resposta = cliente.chat.completions.create(
    messages = [
        {
            "role": "system",
            "content": prompt_sistema
        },
        {
            "role": "user",
            "content": prompt_usuario
        }
    ],
    model = modelo,
    temperature = 0, # relativa a criatividade da resposta -> 0 = não fugir do que é proposto
    max_tokens = 200
)

print(resposta.choices[0].message.content)