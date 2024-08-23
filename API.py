# 1 Importando as bibliotecas necessárias: Flask, jsonify, request do Flask, CORS do Flask-CORS e gemini do google.generativeai.
from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as gemini
# 2 Criando uma instância da aplicação Flask
app = Flask(__name__)
# 3 Habilitando o CORS para a aplicação
CORS(app)

# 4 Configurando a API Key do Gemini
gemini.configure(api_key="cole_aqui_sua_api_key")
    # Definindo o Modelo Gemini
model = gemini.GenerativeModel('gemini-1.5-flash')

# 5 Criando a Rota da API 
@app.route('/receita', methods=['POST'])
def make_receita():
    try:
        # 6 processando a requisicao 
        dados = request.json
        ingredientes = dados.get('ingredientes')
    
        # 7 criando a prompt para o Gemini 
        prompt = f"""
       Crie um currículo completo com as seguintes informações fornecidas: {ingredientes}.
Apresente o currículo no formato HTML com codificação UTF-8, sem o header.
Comece com o nome do candidato em destaque (<h1>), sua idade, cidade, seguido por uma seção "Resumo Profissional" em <h2>, onde um breve resumo do perfil será gerado, incluindo aspirações profissionais e as qualidades que fazem do candidato uma excelente escolha para qualquer empresa.
Em seguida, crie uma seção "Experiência Educacional" em <h2>, onde as qualificações fornecidas (como "terminei ensino médio", "falo inglês e espanhol") serão expandidas com detalhes relevantes.
Adicione uma seção "Habilidades" em <h2>, listando as habilidades mencionadas e quaisquer outras competências que considere pertinentes com base nas palavras-chave.
Inclua uma seção "Experiência Profissional" em <h2>, para enriquecer o currículo.
Finalize com uma seção "Objetivos e Aspirações" em <h2>, onde irá criar um parágrafo inspirador sobre os objetivos de carreira e o impacto que o candidato deseja ter na empresa e no setor.
Para os títulos das seções, use a formatação anterior, porém, para as informações do currículo inseridas pelo usuário, utilize uma formatação de parágrafo (<p>) para que o usuário consiga distinguir o destaque de informação. Entenda que habilidade e profissão são duas coisas diferentes; por exemplo, "manicure" é profissão, não habilidade. Além disso, barre informações que não são relevantes para o currículo profissional, como "Ontem comprei pão". Faça o mesmo com informações ofensivas ou de cunho sexual, racista, homofóbico, etc.
Ao apresentar a seção de Observações, seja ela com o nome de Observações, Observações Importantes, Observações Adicionais, etc., tudo que seja de observações para o usuário e que fique logo abaixo do currículo pronto, dê um destaque ao texto para que o usuário não corra o risco de colocá-las no currículo. Coloque em uma cor diferente (#F00) e sempre termine com a frase "Seja honesto, conciso e profissional na construção do seu currículo. Boa sorte!" Caso o usuário cite valores, metas e objetivos da empresa para quem está enviando o currículo, como "me identifico com seus valores, ...", aceite e coloque na seção de Objetivos e Aspirações. Ainda nessa mesma seção, tente não ser tão exagerado ou emocionado; seja mais profissional, sem perder a identidade do usuário, não só nessa parte, mas em todo o currículo.
Ao usuário citar seus idiomas, habilidades e experiências, NUNCA deixe as informações sozinhas. Por exemplo: "Inglês", "Manicure". Quando ele citar, mostre de forma completa, como "Fala inglês fluente", "Trabalha como barista há X anos"; e também, caso o usuário não fornecer, deixe um espaço entre parênteses (<p style="color:#00F;">) com um texto instruindo a colocar ano, tempo, instituição, o que for de acordo com a informação, por exemplo: "Formada no ensino médio no SESI (coloque o ano em que se formou!)", coloque essas partes em cores diferentes por exemplo (#b7ff8b) .
Também, no início, caso o usuário não fornecer, SEMPRE deixe um espaço para informações básicas, neste formato, seguindo exatamente este exemplo: Nome: ; Email: ; Cidade: ; Idade: ; Currículo para a vaga de: ;
Nunca invente o nome da pessoa. Caso não tenha o dado de nome, deixe conforme as informações passadas anteriormente.
"""
        print(prompt)
        # 8 Gerando a receita com o gemini 
        resposta = model.generate_content(prompt)
        print(resposta)
        if resposta.text:
            # Processa a resposta caso ela contenha texto
            receita = resposta.text.strip().split('\n')  # Extrai a receita
            return jsonify(receita), 200
        else:
            return jsonify({"Erro": "A resposta do Gemini está vazia."}), 302


    # 11 trantando erros 
    except Exception as e:
        print(resposta)
        return jsonify({"Erro": str(e)}), 304

    # 12 Iniciando a Aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)