
# No borrar esta función ya que debe utilizarla para obtener
# los datos de secuencia en forma de lista
# para que el programa funcione debe estar conectado a internet
# ya que los datos se obtienen en línea

def obtenerSecuencias():
    return [
    "GLDIHTKTAMDIFH",
    "DLDIHTKTAMDIFH",
    "DLDIHTKTAMDIFH",
    "DLDIHTKTAMDIFQ",
    "GKDIHTQTASWMFG",
    "GKDIHTQTASWMFG",
    "GRDIHTETASWMFG",
    "GKDIHTETAAWMFG",
    "GRDIHTQTASWMFG",
    "DMDIHTKTAMDVFH",
    "GADIHTSTAMRVFG",
    "GKDIHRATAAEVFG",
    "GLDIHAATASRLFG",
    "GADIHRRTAAQVLG",
    "GADIHTSTAMRVFG",
    "GKDIHRSTAAEIFG",
    "GEDLHSFVASRAFG",
    "GEDLHSFVASRAFG",
    "HIDIHALTAAYIFN",
    "NVDIHSQTAAEVFG",
    "NKDIHTETASKLFK",
    "KEDIHTQTACQIFN",
    "RQDVHGVTAKLLFG",
    "GEDIHAFTASQVFN",
    "GRDIHLETSKALFG",
    "GADLHKAVASDAFG"
    ]

def analizar(secuencias):
    diccionario = {}

    for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        frecs = []

        for pos in range(len(secuencias[0])):
            frecuencia = sum(secuencia[pos].count(letra) 
                            for secuencia in secuencias)
            frecs.append(frecuencia)

        diccionario[letra] = frecs

    diccionario = {letra: frecuencias 
                for letra, frecuencias in diccionario.items() 
                if sum(frecuencias) != 0}
    
    print("\n      |                                 F  R  E  C  U  E  N  C  I  A  S                                      |")
    print("      |                                                                                                      |")
    print("LETRA | Pos1 | Pos2 | Pos3 | Pos4 | Pos5 | Pos6 | Pos7 | Pos8 | Pos9 | Pos10 | Pos11 | Pos12 | Pos13 | Pos14 |")

    for letra, frecuencias in diccionario.items():
        print(f"  {letra}       {frecuencias[0]}      {frecuencias[1]}      {frecuencias[2]}      {frecuencias[3]}      {frecuencias[4]}      {frecuencias[5]}      {frecuencias[6]}      {frecuencias[7]}     {frecuencias[8]}      {frecuencias[9]}       {frecuencias[10]}       {frecuencias[11]}        {frecuencias[12]}      {frecuencias[13]}")

### Programa principal ###

lista = obtenerSecuencias()
analizar(lista)
