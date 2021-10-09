def arrodonir(variable, decimals):
    variable = float(variable)
    variable = round(variable, decimals)
    return (variable)


def termodinamica():

  def pregunta(pregunta):
    while True:
      x = input(pregunta)
      try:
        x = float(x)
        return (x)
      except ValueError:
        if x == "no" or x == "No" or x == "NO":
          x = calc_x(x)
          return(x)
        print("Torna a introduïr la variable")


  # Càlcul de incognita

  def calc_x(x):
    if x == "E":
      calc_E()

  def calc_F():
    m = pregunta("Massa (kg) = ")
    g = gravetat()
    F = m * g
    print("Tindrà una Força de: ", F, "N")
    return (F)

  def calc_E():
    m = massa()
    h = alçada()
    g = gravetat()
    v0 = velocitat_inicial()
    E = m * g * h + 0.5 * m * (v0**2) 
    E = arrodonir(E, 2)
    print("Tindrà una energia de: ", E, "J")
    return (E)

  def calc_W():
    F = Força()
    x = desplaçament()
    W = F * x
    W = arrodonir(W, 2)
    print("Tindra un treball de: ", W, "J")
    return (W)

  def calc_Pu():
    W = treball()
    t = temps()
    Pu = W / t
    Pu = arrodonir(Pu, 2)
    print("Tindrà una potència Útil de: ", Pu, "W")
    return (Pu)

  def calc_Pc():
    η = rendiment()
    Pu = potencia_util()
    Pc = Pu / η
    Pc = arrodonir(Pc, 2)
    print("Necessitaràs una potència consumida de: ", Pc, "W")
    return (Pc)

  def calc_m():
    g = gravetat()
    F = Força()
    m = F / g
    m = arrodonir(m, 2)
    print("Tindrà una massa de: ", m, "kg")
    return (m)

  def calc_vf():
    E = energia()
    m = massa()
    hf = alçada_final()
    g = gravetat()
    vf = (((E - m * g * hf) * 2) / m)**0.5
    vf = arrodonir(vf, 2)
    print("Anirà a una velocitat final de: ", vf, "m/s")
    return (vf)

  def calc_t():
    W = treball()
    Pu = potencia_util()
    t = W / Pu
    print("Tardarà", t, "s")
    return (t)

  def calc_η():
    Pu = potencia_util()
    Pc = potencia_consumida()
    η = Pu / Pc
    print("Tindrà un rendiment del", η * 100, "%")
    return (η)


  while True:
    incognita = input("F = Força\nE = Energia \nw = Treball\nPu = Potència útil \nPc = Potència consumida \nm = Massa \nvf = Velocitat final \nt = Temps\nn o r = Rendiment\n\nQuina incògnita vols calcular? Introdueix només la inicial ")
    print("La teva incognita és ", incognita)
    if incognita == "F" or incognita == "f":
      calc_F()
      break
    if incognita == "E" or incognita == "e":
      calc_E()
      break
    if incognita == "W" or incognita == "w":
      calc_W()
      break
    if incognita == "Pu" or incognita == "pu":
      calc_Pu()
      break
    if incognita == "Pc" or incognita == "pc":
      calc_Pc()
      break
    if incognita == "m":
      calc_m()
      break
    if incognita == "vf":
      calc_vf()
      break
    if incognita == "t":
      calc_t()
      break
    if incognita == "η" or incognita == "n":
      calc_η()
      break
    print("\nUi t'has equivocat, torna a introduïr la incògnita sisplau:\n")