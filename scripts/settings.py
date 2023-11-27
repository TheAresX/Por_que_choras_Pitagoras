#script que armazena constantes
#configurações Gerais
WIDTH = 1280 #largura da tela
HEIGHT = 720 #altura da tela
PRIMARY_COLOR = 'dark blue' #cor primária do texto dos botoes menu/gameover
SECONDARY_COLOR = 'white' #cor secundária do texto dos botoes menu/gameover
TEXT_COLOR = (46,255,136) #cor texto perguntas e opções
FONTE = 'assets/fonts/DePixelKlein.ttf' #diretorio da fonte do game

#texto de perguntas, opcoes, caminho de imagem e posicao de imagem das fases
FASE1 = {
    'pergunta0': [
        'Shelly atira 5 projéteis, sendo o dano MÁXIMO de 1550.',
        'Sabendo que todos os projéteis tem o mesmo dano,',
        'Qual o dano de cada projétil?'
    ], #lista de perguntas
    'certa0': '( )  310', #resposta certa
    'errada0': [
        '( )  305', '( )  315'
    ], #lista resposta errada
    'img0': [
        'assets/level/shelly.png',
        [843, 292],
    ], #lista diretório da imagem do personagem e posicao na tela

    'pergunta1': [
        'Nita tem 3.800 ponto de Saúde, e 3 projéteis de Shelly',
        'a acerta. Se cada projétil de Shelly causa 420 de dano,',
        'quanto de saúde Nita ficou após receber o dano?'
    ],
    'certa1': '( )  2.540',
    'errada1': [
        '( )  2.120', '( )  1.700'
    ],
    'img1': [
        'assets/level/nita.png',
        [857,299],
    ],

    'pergunta2': [
        '',
        'Colt tem um dano total de 1.800, dividido em 6 projéteis.',
        'Quanto de dano causa cada projétil de Colt?'
    ],
    'certa2': '( )  300',
    'errada2': [
        '( )  350', '( )  400'
    ],
    'img2': [
        'assets/level/colt.png',
        [875, 286],
    ],

    'pergunta3': [
        'O dano máximo de Bull é 2.800, em 5 balas. Se Bull',
        'erra 2 de suas balas em um oponente, quanto de dano',
        'Bull causou?'
    ],
    'certa3': '( )  1.680',
    'errada3': [
        '( )  2.280', '( )  1.240'
    ],
    'img3': [
        'assets/level/bull.png',
        [879, 217],
    ],

    'pergunta4': [
        'O super da arma de choque de Jessie causa 3.920 de dano',
        'máximo. O dano mínimo que ela pode causar é 392. Quantas',
        'vezes maior é o dano máximo comparado ao mínimo?'
    ],
    'certa4': '( )  10 vezes',
    'errada4': [
        '( )  5 vezes', '( )  8 vezes'
    ],
    'img4': [
        'assets/level/jessie.png',
        [892, 221],
    ],

    'pergunta5': [
        'O dano de um foguete disparado de Brock é 1.100.',
        'No super, Brock dispara até 9 foguetes. Qual o dano total',
        'possível dos 9 foguetes disparados?'
    ],
    'certa5': '( )  9.900',
    'errada5': [
        '( )  9.000', '( )  10.000'
    ],
    'img5': [
        'assets/level/brock.png',
        [780, 237],
    ],

    'pergunta6': [
        'As dinamites de Dynamike causam 760 de dano mínimo e',
        '1.064 de dano máximo. Se Dynamike jogar uma com o dano',
        'mínimo e outra com o máximo, qual o dano causado?'
    ],
    'certa6': '( )  1.824',
    'errada6': [
        '( )  2.128', '( )  1.520'
    ],
    'img6': [
        'assets/level/dynamike.png',
        [886, 202],
    ],

    'pergunta7': [
        '',
        'Bo atirou 2 flechas com 520 de dano e uma com 728 de',
        'dano em um oponente. Qual o dano total causado por Bo?'
    ],
    'certa7': '( )  1.768',
    'errada7': [
        '( )  1.976', '( )  2.184'
    ],
    'img7': [
        'assets/level/bo.png',
        [858, 256],
    ],

    'pergunta8': [
        'El Primo causa 360 de dano por soco a cada 0,8 segundos.',
        'Quantos segundos El Primo precisa para causar 2.160 de',
        'dano, socando sem parar?'
    ],
    'certa8': '( )  4.8 seg',
    'errada8': [
        '( )  4.0 seg', '( )  5.6 seg'
    ],
    'img8': [
        'assets/level/el_primo.png',
        [877, 211],
    ],

    'pergunta9': [
        'Spike atira uma bomba que dispara 6 espinhos na explosão.',
        'Se cada espinho causa um dano de 560, qual o dano',
        'máximo possível pode ser causado?'
    ],
    'certa9': '( )  3.360',
    'errada9': [
        '( )  2.800', '( )  3.920'
    ],
    'img9': [
        'assets/level/spike.png',
        [805, 247],
    ],
}

FASE2 = {
    'pergunta0': [
        'O Bárbaro dá 75 de dano a cada 1,3 segundos. Se a torre ',
        'adversária tem 375 de vida, quanto tempo o Bárbaro',
        'irá levar para derrubá-la, em segundos?'
    ],
    'certa0': '( )  6,5',
    'errada0': [
        '( )  5,2', '( )  7,8'
    ],
    'img0': [
        'assets/level/barbaro.png',
        [859, 227],
    ],

    'pergunta1': [
        'A Valquíria tem um alcance de 1,2 metros e se encontra a',
        'uma distância da torre adversária 12 vezes maior que seu',
        'alcance. A qual distancia ela se encontra da torre?'
    ],
    'certa1': '( )  14,4 metros',
    'errada1': [
        '( )  12 metros', '( )  13,2 metros'
    ],
    'img1': [
        'assets/level/valquiria.png',
        [729,261],
    ],

    'pergunta2': [
        'A X-Besta realiza 26 de dano a cada 0,3 segundos. Se três',
        'X-Bestas forem mobilizadas no campo, quanto tempo levará,',
        'para as 3 juntas, causarem 228 de dano ao adversário?'
    ],
    'certa2': '( )  3 segundos',
    'errada2': [
        '( )  5 segundos', '( )  7 segundos'
    ],
    'img2': [
        'assets/level/x-besta.png',
        [686, 244],
    ],

    'pergunta3': [
        'O Bebê Dragão causa 121 de dano a cada 1,5 segundos,',
        'chegou a torre adversária, que está com 1089 de vida.',
        'Quanto tempo o Bebê Dragão levará para destuir a torre?'
    ],
    'certa3': '( )  13,5 segundos',
    'errada3': [
        '( )  12 segundos', '( )  16,5 segundos'
    ],
    'img3': [
        'assets/level/bebe-dragao.png',
        [804, 242],
    ],

    'pergunta4': [
        'A Mini-Pekka dá um ataque a cada 1,6 segundos e você',
        'contabilizou que ela realizou 7 ataques antes de ser ',
        'destruída. Quanto tempo ela ficou em campo atacando?'
    ],
    'certa4': '( )  11,2 segundos',
    'errada4': [
        '( )  12,8 segundos', '( )  16 segundos'
    ],
    'img4': [
        'assets/level/mini-pekka.png',
        [876, 438],
    ],

    'pergunta5': [
        'O Príncipe corre incríveis 6 metros a cada segundo.',
        'Localizado a uma distancia de 21 metros de uma torre,',
        'quantos segundos o Príncipe levará para chegar à Torre?'
    ],
    'certa5': '( )  3,5 segundos',
    'errada5': [
        '( )  4 segundos', '( )  5,33 segundos'
    ],
    'img5': [
        'assets/level/principe.png',
        [758, 241],
    ],

    'pergunta6': [
        'A P.E.K.K.A realiza um ataque a cada 1,8 segundos. Se ela',
        'causar 3240 de dano em 5,4 segundos. Quanto de dano a ',
        'P.E.K.K.A causou por segundo?'
    ],
    'certa6': '( )  600',
    'errada6': [
        '( )  720', '( )  740'
    ],
    'img6': [
        'assets/level/pekka.png',
        [710, 199],
    ],

    'pergunta7': [
        'O Corredor, personagem mais rápido do jogo, percoreu',
        '54 metros com sua velocidade em apenas 4,5 segundos.',
        'Sabendo disso, quantos metros ele corre por segundo?'
    ],
    'certa7': '( )  12 metros',
    'errada7': [
        '( )  14 metros', '( )  8 metros'
    ],
    'img7': [
        'assets/level/corredor.png',
        [904, 143],
    ],

    'pergunta8': [
        'A Bruxa causa 76 de dano por segundo, e demora',
        '1,1 segundos para lançar seu ataque. Quando de dano',
        'a Bruxa consegue causar por ataque?'
    ],
    'certa8': '( )  84',
    'errada8': [
        '( )  82', '( )  92'
    ],
    'img8': [
        'assets/level/bruxa.png',
        [718, 222],
    ],

    'pergunta9': [
        'O Mago lança uma rajada de fogo a cada 1,4 segundos.',
        'Sabendo que o dano por rajada é de 133, quantos segundos',
        'ele levou para derrubar uma X-Besta com 1596 de vida?'
    ],
    'certa9': '( )  16,8 segundos',
    'errada9': [
        '( )  18,2 segundos', '( )  19,6 segundos'
    ],
    'img9': [
        'assets/level/mago.png',
        [767, 189],
    ],
}

FASE3 = {
    'pergunta0': [
        'Mario viu que gastou 3,5 minutos para completar uma',
        'corrida. Sabendo que 1 MINUTO (min) tem 60 SEGUNDOS (s),',
        'quantos SEGUNDOS Mario gatou para completar a corrida?'
    ],
    'certa0': '( )  210 segundos',
    'errada0': [
        '( )  350 segundos', '( )  180 segundos'
    ],
    'img0': [
        'assets/level/mario.png',
        [787, 250],
    ],

    'pergunta1': [
        'Peach ganhou uma corrida a 0,25 km na frente de Mario.',
        'Se 1.000 METROS (m) é 1 QUILOMETRO (Km), qual foi a ',
        'diferença entre Peach e Mario em metros?'
    ],
    'certa1': '( )  250 m',
    'errada1': [
        '( )  2500 m', '( )  25 m'
    ],
    'img1': [
        'assets/level/peach.png',
        [758,238],
    ],

    'pergunta2': [
        'No tanque do carro de Bowser cabem 25L (litros) e está',
        'faltando 378 mL (mililitros) para encher. Quanto está',
        'faltando, exatamente, em litros para completar o tanque?'
    ],
    'certa2': '( )  0,378 L',
    'errada2': [
        '( )  3,78 L', '( )  0,0378 L'
    ],
    'img2': [
        'assets/level/bowser.png',
        [752, 203],
    ],

    'pergunta3': [
        'Yoshi está a 20 m/s na pista, porém seu painel marca',
        'em km/h. Sabendo que 1km = 1000m e 1h = 3600s. Qual a ',
        'Velocidade marcada no painel da moto de Yoshi?'
    ],
    'certa3': '( )  72 km/h',
    'errada3': [
        '( )  7,2 km/h', '( )  36 km/h'
    ],
    'img3': [
        'assets/level/yoshi.png',
        [783, 234],
    ],

    'pergunta4': [
        'Para finalizar Copa Shell em primeiro, Luigi gastou 4250s.',
        'Se 1h = 60min e 1min = 60s, qual foi o tempo total gasto',
        'por Luigi nas quatro pistas da Copa Shell?'
    ],
    'certa4': '( )  1h 10min 50s',
    'errada4': [
        '( )  2h 5min 30s', '( )  1h 0min 30s'
    ],
    'img4': [
        'assets/level/luigi.png',
        [717, 189],
    ],
}