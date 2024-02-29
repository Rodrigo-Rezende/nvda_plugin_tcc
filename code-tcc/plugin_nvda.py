# Importa o módulo de log do NVDA
import nvdaControllerClient
# Importa a biblioteca pyautogui
import pyautogui

# Função principal do plugin
def script_echoCode(app, text, echoAll=True):
    # Converte o texto para minúsculas para facilitar a manipulação
    text = text.lower()

    # Verifica se o texto contém palavras-chave relacionadas a código
    if "def " in text or "class " in text or "for " in text or "while " in text or "if " in text or "else " in text:
        # Simula a leitura do código usando a biblioteca pyautogui
        pyautogui.alert(text, title="Código", button="OK")

# Conecta ao controlador NVDA
nvda = nvdaControllerClient.Controller()

# Registra a função do plugin
nvda.script["echoCode"] = script_echoCode
