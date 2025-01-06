from selenium import webdriver
from selenium.webdriver.chrome.options import Options # Util para criar opções novas e salvar a sessão
from selenium.webdriver.common.by import By # util para capturar as classes
from selenium.webdriver.common.keys import Keys # Util para digitação
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os # Util para manipular o SO, como criar pastas para salvar a sessão
import time # Util para gerar intervalos de tempo
import requests # Util para condctar com servidor externo, url e outras funcionalidades
from datetime import datetime

# Agente do usuário para requisição
agent = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36"
}

# API para gerenciar interações
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/<Seu_codigo>", headers=agent)
time.sleep(2)
api.raise_for_status()
api = api.text.split(".n.")
bolinha_notificacao = api[3].strip()  # Classe para bolinha de notificação
contato_cliente = api[4].strip()
# caixa_msg = api[5].strip()
# msg_cliente = api[6].strip()
# caixa_msg2 = api[7].strip()
# caixa_pesquisa = api[8].strip()

# Configuração para salvar sessão do WhatsApp Web
dir_path = os.getcwd()
chrome_options = Options()
chrome_options.add_argument(r"user-data-dir=" + dir_path + "/pasta/sessao/") 
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://web.whatsapp.com/')
print("Aguardando carregamento do WhatsApp Web...")
time.sleep(15)  # Aguarde o QR Code ou a sessão ser restaurada

# Função para ler o texto do arquivo mensagem.txt
def ler_texto_arquivo(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Erro: Arquivo {arquivo} não encontrado.")
        return "Mensagem padrão: arquivo não encontrado."

# Função para capturar e ler mensagens
def ler_mensagens(notificacoes):
    try:
        print(f"{len(notificacoes)} notificação(ões) encontrada(s). Clicando na mais recente...")
        clica_notificacoes = notificacoes.pop()
        clica_notificacoes.click()
        time.sleep(2)

        # Localizar as mensagens na conversa
        mensagem_element = driver.find_elements(By.XPATH, "//div[contains(@class, '_akbu')]//span[@dir='ltr']//span")
        mensagens_texto = "".join(i.text + "\n" for i in mensagem_element)
        time.sleep(4)
        
        contato_element = driver.find_element(By.CSS_SELECTOR, "div._amig span")
        print("contato", contato_element.text)

        print(f"- {mensagens_texto}")

        return (contato_element.text, mensagens_texto)
    except Exception as e:
        print(f"Erro ao ler mensagens: {e}")
        return []

# Função para escrever e enviar uma mensagem
def escrever_mensagem(mensagem):
    try:
        campo_mensagem = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@contenteditable="true" and @data-tab="10" and @aria-placeholder="Digite uma mensagem"]')
            )
        )
        campo_mensagem.click()
    
        campo_mensagem.send_keys(Keys.CONTROL, 'a', Keys.DELETE)

        campo_mensagem.send_keys(mensagem, Keys.SPACE)

        print("Mensagem enviada com sucesso!", mensagem)
    except Exception as e:
        print(f"Erro ao escrever mensagem: {e}")

def salvar_conversa(contato, mensagens):
    try:
        contato_formatado = contato.replace(" ", "_")

        diretorio_base = os.path.join(os.getcwd(), "conversas")

        if not os.path.exists(diretorio_base):
            os.makedirs(diretorio_base)
            print(f"Diretório '{diretorio_base}' criado com sucesso.")

        diretorio_contato = os.path.join(diretorio_base, contato_formatado)

        if not os.path.exists(diretorio_contato):
            os.makedirs(diretorio_contato)
            print(f"Diretório '{diretorio_contato}' criado com sucesso.")

        data_atual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nome_arquivo = f"{data_atual}.txt"

        caminho_arquivo = os.path.join(diretorio_contato, nome_arquivo)

        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(mensagens)

        print(f"Conversa salva em: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar a conversa: {e}")

# Função para simular envio de mensagens para uma API
def enviar_api(tupla_dados):
    try:
        contato, mensagens = tupla_dados  # Desempacotar a tupla
        salvar_conversa(contato, mensagens)
        print("Mensagens enviadas com sucesso para a API.")
    except Exception as e:
        print(f"Erro ao enviar mensagens para API: {e}")

# Capturar notificações (bolinhas)
def adquirir_mensagens():
    print("Procurando notificações...")
    return driver.find_elements(By.CLASS_NAME, bolinha_notificacao)

# Loop principal do bot
def bot():
    try:
        while True:
            # Adquirir mensagens
            notificacoes = adquirir_mensagens()

            while len(notificacoes) > 0:
                # 2. Ler mensagens recebidas
                mensagens_recebidas = ler_mensagens(notificacoes)
                time.sleep(2)

                # 2. Enviar mensagens para uma API (se houver mensagens)
                if mensagens_recebidas:
                    enviar_api(mensagens_recebidas)
                    time.sleep(1)

                    # 3. Ler mensagem do arquivo e enviar
                    mensagem_arquivo = ler_texto_arquivo("mensagem.txt")
                    escrever_mensagem(mensagem_arquivo)

                    # Intervalo para evitar sobrecarga
                    time.sleep(10)
    except KeyboardInterrupt:
        print("Bot interrompido pelo usuário.")
        driver.quit()

bot()
