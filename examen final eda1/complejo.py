import datetime
#vamos a establecer todas las funciones y atributos en privado, ya que en tweeter solo los programadores pueden acceder a estas funcionalidades
#y pueden modificar los atributos y las funciones, el resto de usuarios deben de solicitar la informacion o pueden hacer un print pero no acceder 
#a modificar los atributos o funciones. De eso se encarga el programador que bajo ciertas condiciones les da las herramientas para modificar 
#algunos atributos, pero nunca las funciones ya que esto se cargaria el programa.

class Usuario:
    def __init__(self, nombre, username):
        self._nombre = nombre
        self._username = username
        self._tweets = []
        self._seguidores = []
        self._seguidos = []
        self._bandeja_entrada = []
        self._notificaciones = []

    def _publicar_tweet(self, contenido):
        tweet = Tweet(contenido, self)
        self._tweets.append(tweet)
        tweet.autor = self
        return tweet

    def _seguir_usuario(self, usuario):
        usuario._seguidores.append(self)
        self._seguidos.append(usuario)

    def _recibir_mensaje(self, mensaje):
        self.bandeja_entrada.append(mensaje)

    def _enviar_mensaje(self, receptor, contenido):
        mensaje = Mensaje(contenido, self, receptor)
        receptor.recibir_mensaje(mensaje)
        return mensaje

    def _obtener_timeline(self):
        timeline = []
        for usuario in self.seguidos:
            timeline.extend(usuario.tweets)
        timeline.sort(key=lambda x: x.fecha, reverse=True)
        return timeline

    def _dar_me_gusta(self, tweet):
        tweet.dar_me_gusta(self)
        if tweet.autor != self:
            notificacion = f'@{self._username} ha dado me gusta a tu tweet: "{tweet._contenido}"'
            tweet.autor._notificaciones.append(notificacion)

    def _retwittear(self, tweet):
        retweet = self._publicar_tweet(tweet._contenido)
        retweet.origen = tweet
        if tweet.autor != self:
            notificacion = f'@{self._username} ha retwitteado tu tweet: "{tweet._contenido}"'
            tweet.autor._notificaciones.append(notificacion)

    def _responder_tweet(self, tweet, contenido):
        respuesta = self._publicar_tweet(contenido)
        respuesta.origen = tweet
        tweet._respuestas.append(respuesta)
        if tweet.autor != self:
            notificacion = f'@{self._username} ha respondido a tu tweet: "{tweet._contenido}"'
            tweet.autor._notificaciones.append(notificacion)
        return respuesta

    def _establecer_perfil(self, nombre, bio, foto):
        self.nombre = nombre
        self.bio = bio
        self.foto = foto

    def _buscar_usuarios(self, keyword):
        resultados = []
        for usuario in self._seguidos:
            if keyword.lower() in usuario.nombre.lower() or keyword.lower() in usuario.username.lower():
                resultados.append(usuario)
        return resultados

    def _ver_notificaciones(self):
        for notificacion in self._notificaciones:
            print(notificacion)
        self.notificaciones = []





class Tweet:
    MAX_CARACTERES = 140

    def __init__(self, contenido, autor):
        if len(contenido) > self.MAX_CARACTERES:
            raise ValueError("El contenido del tweet excede el límite de caracteres.")
        self._contenido = contenido
        self._autor = autor
        self._fecha = datetime.datetime.now()
        self._me_gusta = []
        self._retwits = []
        self._origen = None
        self._respuestas = []

    def __str__(self):
        return f'@{self.autor.username}: {self.contenido}'

    def dar_me_gusta(self, usuario):
        self._me_gusta.append(usuario)

    def obtener_cantidad_me_gusta(self):
        return len(self.me_gusta)

    def obtener_cantidad_retwits(self):
        return len(self.retwits)

    def obtener_respuestas(self):
        return self.respuestas


class Mensaje(Tweet):
    def __init__(self, contenido, autor, receptor):
        super().__init__(autor)
        self._contenido = contenido
        self._remitente = autor
        self._receptor = receptor
        self._fecha = datetime.datetime.now()

    def __str__(self):
        return f'De: @{self.remitente.username}\nPara: @{self.receptor.username}\nContenido: {self.contenido}'

class Retweet(Tweet):
    def __init__(self, contenido, autor, origen):
        super().__init__(contenido, autor)
        self._origen = origen
        self._origen.retwits.append(self)

    def __str__(self):
        return f'@{self.autor.username} ha retwitteado: "{self.origen.contenido}"'
# Ejemplo de uso
usuario1 = Usuario("John Doe", "johndoe")
usuario2 = Usuario("Jane Smith", "janesmith")

usuario1._seguir_usuario(usuario2)

tweet1 = usuario1._publicar_tweet("¡Hola, mundo!")
tweet2 = usuario2._publicar_tweet("Estoy emocionada por usar Twitter.")

usuario1._dar_me_gusta(tweet2)
usuario1._retwittear(tweet2)

respuesta = usuario2._responder_tweet(tweet1, "Hola, John!")
usuario1._dar_me_gusta(respuesta)

usuario2._establecer_perfil("Jane Smith", "Amante de la tecnología y los gatos.", "foto.jpg")

resultados_busqueda = usuario1._buscar_usuarios("Jane")

for usuario in resultados_busqueda:
    print(f"Nombre: {usuario._nombre}")
    print(f"Username: {usuario._username}")
    print("---")

usuario2._ver_notificaciones()



import random

nombres = ["Liam", "Emma", "Noah", "Olivia", "Sophia", "Jackson", "Ava", "Aiden", "Isabella", "Mia", "Lucas", "Charlotte",
           "Oliver", "Amelia", "Caden", "Harper", "Elijah", "Evelyn", "Grayson", "Abigail"]

apellidos = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson",
             "Thomas", "Jackson", "White", "Harris", "Clark", "Lewis", "Lee", "Walker", "Hall"]

def generar_usuario():
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    username = f"{nombre.lower()}{apellido.lower()}{random.randint(100, 999)}"
    return Usuario(f"{nombre} {apellido}", username)

# Crear 10 usuarios
usuarios = []
for _ in range(10):
    usuario = generar_usuario()
    usuarios.append(usuario)
    print(f"Nombre: {usuario._nombre}")
    print(f"Username: {usuario._username}")
    print("---")






print(usuario2.bio)