import unicodedata
from random import choice

estado = 0

romanos = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
           6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
           11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV'}  
cores = {
         'laranja': color(255, 100, 0),
         'azul': color(50, 50, 255),
         'verde': color(0, 200, 0),
         'vermelho': color(255, 0, 0),
         'roxo': color(128, 0, 128),
         'amarelo': color(240, 240, 0),
         'escuro': color(0, 0, 100),  # azul escuro
         } 

imagens_elementos = {}

def setup():
    # size(640, 480)
    fullScreen()
    global ac, ms, margem, lc, e, ai, mi, tam_letra
    ac = height * 0.75  # 120mm altura da carta
    ms = ac / 24.0  # 5mm  margem de seguranca
    ai = ac * 93.3 / 120
    mi = ac / 11.0
    margem = height * 0.125
    lc = ac / 3.0 * 2  # largura da carta
    tam_letra = ac / 28
    e = (width - 3 * lc) / 4   # espacamento horizontal
    ler_dados()
    sorteio()
    textAlign(CENTER, CENTER) # alinhamento horiz, alinhamento vertical
    
def draw():
    background(100)
    # text(estado, 200, 200)    
    if estado == 0:
        boas_vindas()    
        # image(imagens_elementos['fogo'] , 200, 200, 100, 100)
    elif estado == 1:
        primeira_carta_virada(False)  
        segunda_carta_virada(False)  
        terceira_carta_virada(False)  
    elif estado == 2:
        primeira_carta_virada(True)  
        segunda_carta_virada(False)  
        terceira_carta_virada(False)  
    elif estado == 3:
        primeira_carta_virada(True)  
        segunda_carta_virada(True)  
        terceira_carta_virada(False)  
    elif estado == 4:
        primeira_carta_virada(True)  
        segunda_carta_virada(True)  
        terceira_carta_virada(True)  

                                                                                
def boas_vindas():
    textAlign(CENTER, CENTER)
    textFont(fonte_bold) 
    textSize(24)   
    fill(0)
    text("Bem-vindas todas as pessoas!", width / 2, height / 2)

def primeira_carta_virada(virada):
    fill(255)
    rect(e, margem, lc , ac)
    if virada:
        fill(0)
        textAlign(CENTER)
        pergunta_formatada = quebra_frase(pergunta, lc * 0.7)
        textFont(fonte) 
        textSize(tam_letra)   
        text(pergunta_formatada, e + lc / 2, margem + ac / 2)
        nome_cor = cor_perguntas[nq]
        nome_elemento =  elemento_perguntas[nq]
        numero_cor_elemento(e * 1, nq, '', nome_cor, nome_elemento)
    else:
        imageMode(CORNER)
        image(verso1, e, margem, lc, ac)

def segunda_carta_virada(virada):
    fill(255)
    rect(e * 2 + lc, margem, lc , ac)
    if virada:
        textAlign(CENTER, CENTER)
        fill(0)
        separador = texto.find(':')
        titulo = texto[:separador]
        corpo = texto[separador + 2:]
        texto_formatado = quebra_frase(corpo, lc * 0.7)
        textFont(fonte)   
        textSize(tam_letra) 
        text(texto_formatado, e * 2 + lc * 1.5, margem + ac / 2)
        nome_cor = cor_textos[nt]
        nome_elemento =  elemento_textos[nt]
        numero_cor_elemento(e * 2 + lc, nt, titulo, nome_cor, nome_elemento)
    else:
        imageMode(CORNER)
        image(verso2, e * 2 + lc, margem, lc, ac)     

def terceira_carta_virada(virada):
    fill(255)
    rect(e * 3 + lc * 2, margem, lc , ac)
    if virada:
        if desenho_personagem:
            imageMode(CORNER)
            image(desenho_personagem, e * 3 + lc * 2 + ms,
                  margem + ms, lc - 2 * ms, ai )
        nome_elemento = elemento_personagens[np]
        nome_cor = cor_personagens[np]
        numero_cor_elemento(e * 3 + lc * 2, np, personagem, nome_cor, nome_elemento)
    else:
        imageMode(CORNER)
        image(verso3, e * 3 + lc * 2, margem, lc, ac)  
    
def numero_cor_elemento(x, numero, titulo, nome_cor, elemento):
        textFont(fonte_bold)
        textSize(tam_letra)
        textAlign(CENTER, CENTER)
        fill(cores[nome_cor])
        noStroke()
        ellipse(x + ms * 2, margem + ac - mi, ms * 2, ms * 2)
        fill(cor_texto(nome_cor))
        text(romanos[numero], x + ms * 2, margem + ac - mi)
        fill(0)
        text(titulo, x + (lc/2), margem + ac - mi)
        imageMode(CENTER)
        image(imagens_elementos[elemento],
               x + lc - ms * 2, margem + ac - mi, ms * 3, ms * 3 )

def cor_texto(nome_cor):
    if brightness(cores[nome_cor]) < 150:
        return 255
    else:
        return 0

def quebra_frase(frase, largura):
    resultado = ""
    parcial = ""
    for letra in frase:
        parcial += letra
        if textWidth(parcial) > largura:
            ultimo_espaco = parcial.rfind(' ')
            resultado += '\n' + parcial[:ultimo_espaco]
            parcial = parcial[ultimo_espaco + 1:]
    resultado += '\n' + parcial
    return resultado    
    
def ler_dados():
    global fonte, fonte_bold
    global verso1, verso2, verso3
    global elemento_personagens, cor_personagens
    global elemento_textos, cor_textos
    global elemento_perguntas, cor_perguntas
    global numeros_e_perguntas, numeros_e_personagens, numeros_e_textos
    fonte_bold = loadFont("Montserrat-Bold-24.vlw")
    fonte = loadFont("Montserrat-Regular-24.vlw")

    verso1 = loadImage('fundo_pergunta.png')
    verso2 = loadImage('fundo_texto.png')
    verso3 = loadImage('fundo_personagem.png')

    perguntas = loadStrings('perguntas.txt')
    numeros_e_perguntas = []
    for n, pergunta in enumerate(perguntas, 1):
        numeros_e_perguntas.append((n, pergunta))
    dados_perguntas = loadStrings('dados_perguntas.txt')
    elemento_perguntas, cor_perguntas = {}, {}
    for n, linha in enumerate(dados_perguntas, 1):
        palavras = linha.split(' ')
        elemento = strip_accents(palavras[-1])
        elemento_perguntas[n] = elemento
        cor = strip_accents(palavras[0])
        cor_perguntas[n] = cor

    numeros_e_textos = []
    textos = loadStrings('textos.txt')
    for n, t in enumerate(textos, 1):
        numeros_e_textos.append((n, t))
    dados_textos = loadStrings('dados_textos.txt')
    elemento_textos, cor_textos = {}, {}
    for n, linha in enumerate(dados_textos, 1):
        palavras = linha.split(' ')
        elemento = strip_accents(palavras[-1])
        elemento_textos[n] = elemento
        cor = strip_accents(palavras[0])
        cor_textos[n] = cor
                        
    personagens = loadStrings('personagens_secos.txt')
    numeros_e_personagens = []
    for n, perso in enumerate(personagens, 1):
        numeros_e_personagens.append((n, perso))
    dados_personagem = loadStrings('personagens.txt')
    elemento_personagens, cor_personagens = {}, {}
    for n, linha in enumerate(dados_personagem, 1):
        palavras = linha.split(' ')
        elemento = strip_accents(palavras[-1].replace('.', ''))
        elemento_personagens[n] = elemento
        cor = strip_accents(palavras[-2].replace(',', ''))
        cor_personagens[n] = cor
                        
        
    for nome in ['fogo', 'agua', 'trovao', 'madeira', 'terra', 'ar', 'eter']:
        arquivo = nome + '.png'
        imagens_elementos[nome] = loadImage(arquivo)




def strip_accents(s):
   return ''.join((c for c in unicodedata.normalize('NFD', unicode(s)) if unicodedata.category(c) != 'Mn'))
    
def sorteio():
    global nq, pergunta, np, personagem, nt, texto, desenho_personagem
    nq, pergunta = choice(numeros_e_perguntas)
    np, personagem = choice(numeros_e_personagens)
    nt, texto = choice(numeros_e_textos)
    arquivo_personagem = str(np) + '.jpg'
    desenho_personagem = loadImage(arquivo_personagem)
    print(desenho_personagem)

def keyReleased():
    muda_estado()
    
def mouseReleased():
    muda_estado()
    
def muda_estado():
    global estado
    if key == ' ':
        if estado < 4:
            estado = estado + 1
        else:
            estado = 0
            sorteio()

        
