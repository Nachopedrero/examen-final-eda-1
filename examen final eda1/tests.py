import datetime
import unittest
from complejo import Usuario, Tweet
#algunos test de ejemplo para comprobar que estas funciones esten bien

class TestUsuario(unittest.TestCase):
    def test_creacion_usuario(self):
        usuario = Usuario("John Doe", "johndoe")
        self.assertEqual(usuario._nombre, "John Doe")
        self.assertEqual(usuario._username, "johndoe")
        self.assertEqual(usuario._tweets, [])
        self.assertEqual(usuario._seguidores, [])
        self.assertEqual(usuario._seguidos, [])
        self.assertEqual(usuario._bandeja_entrada, [])
        self.assertEqual(usuario._notificaciones, [])

    def test_publicar_tweet(self):
        usuario = Usuario("John Doe", "johndoe")
        tweet = usuario._publicar_tweet("¡Hola, mundo!")
        self.assertEqual(tweet._contenido, "¡Hola, mundo!")
        self.assertEqual(tweet._autor, usuario)
        self.assertIsInstance(tweet._fecha, datetime.datetime)
        self.assertEqual(tweet._me_gusta, [])
        self.assertEqual(tweet._retwits, [])
        self.assertIsNone(tweet._origen)
        self.assertEqual(tweet._respuestas, [])

    def test_seguir_usuario(self):
        usuario1 = Usuario("John Doe", "johndoe")
        usuario2 = Usuario("Jane Smith", "janesmith")
        usuario1._seguir_usuario(usuario2)
        self.assertIn(usuario2, usuario1._seguidos)
        self.assertIn(usuario1, usuario2._seguidores)

   

    


class TestTweet(unittest.TestCase):
    def test_creacion_tweet(self):
        usuario = Usuario("John Doe", "johndoe")
        tweet = Tweet("¡Hola, mundo!", usuario)
        self.assertEqual(tweet._contenido, "¡Hola, mundo!")
        self.assertEqual(tweet._autor, usuario)
        self.assertIsInstance(tweet._fecha, datetime.datetime)
        self.assertEqual(tweet._me_gusta, [])
        self.assertEqual(tweet._retwits, [])
        self.assertIsNone(tweet._origen)
        self.assertEqual(tweet._respuestas, [])

    


if __name__ == "__main__":
    unittest.main()

