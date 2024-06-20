Caso Fundamentos de Machine Learning
CONTEXTO CASO

Valve, los ha contactado como equipo de análisis de datos y modelado de Machine Learning para analizar y realizar modelos predictivos sobre los datos.

En cada partida de Counter Strike: GO dos equipos de 5 jugadores (denominados terroristas y contra-terroristas) se enfrentan.

El objetivo del equipo terrorista es plantar una bomba con timer de 45 segundos en uno de dos sitios específicos dentro de un mapa. Por otro lado, el objetivo del equipo contra-terrorista es evitar que la bomba sea plantada o desactivarla antes de que esta explote cuando ya ha sido plantada. Los datos a utilizar corresponden a sobre 7000 partidas del juego (con un máximo de 10 jugadores c/u)

Los datos han sido extraídos de replays, los cuales son archivos propietarios con la información de cada una de las acciones realizadas por cada jugador dentro de una partida. Los replays han sido extraídos de la red utilizando un scrapper y pre-procesados utilizando un script.

En este caso, la data corresponde a un archivo CSV con 79.157 filas, cada una correspondiente a un jugador dentro de una partida. El archivo contiene 29 columnas correspondientes a variables que describen las acciones del jugador dentro del juego.

 Dato 
 Descripción 
M
a
p
Nombre  del Mapa donde se jugó la partida
 Team
 Nombre de equipo al que pertenece el jugador
 InternalTeamId
 Identificador del equipo al que pertenece el jugador.
 MatchId
 Identificador de la partida.
 RoundId
 Identificador de la ronda (los equipos se enfrentan en rondas de 5 partidas seguidas)
 MatchWinner
 Indica si el jugador ganó o no la partida.
 RoundWinner
 Indica si el jugador ganó o no la ronda analizada.
 Survived
 Indica si el jugador sobrevivió o no a la partida (sobrevivir no es sinónimo de ganar).
 AbnormalMatch
 Indica si la partida del jugador tuvo un error por conexión de red
 TimeAlive
 Indica el tiempo en segundos que el jugador estuvo vivo durante el juego
 TravelledDistance
 Distancia viajada por el jugador durante la partida.
 RLethalGrenadesThrown/RNonLethalGrenadesThrown
 Cantidad de granadas lanzadas, categorizadas en letales y no-letales.
 PrimaryXXXX
 Porcentaje de uso arma clasificada como primaria. Categorizada en AssaultRifle, SniperRifle, SMG, Heavy y Pistol.
 [Match|Round] Assists
 Cantidad de asistencias efectuadas por el jugador durante la partida o la ronda.
 [Match|Round] Kills
 Cantidad de kills efectuados por el jugador durante la partida o la ronda.
 [Match|Round] FlankKills
 Cantidad de kills efectuados por el jugador sin que la víctima lo viese durante la partida o la ronda.
 [Match|Round] HeadShots
 Cantidad de kills efectuados por el jugador a través de un tiro en la cabeza durante la partida o la ronda.
 RoundStartingEquipmentValue
 Valor del equipamiento llevado por el jugador al inicio de la ronda.
 TeamStartingEquipmentValue
 Valor promedio del equipamiento llevado por el equipo del jugador al inicio de la ronda.
