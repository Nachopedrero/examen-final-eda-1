#importa el resto de archivos
from complejo import *
import unittest
from tests import * 


#ejecuta las pruebas
unittest.main()
def run_tests():
    suite = unittest.TestLoader().discover("tests")
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)
    
    if test_result.failures or test_result.errors:
        print("Algunas pruebas han fallado o generado errores:")
        
        for test_case, error in test_result.failures:
            print(f"Error en la prueba: {test_case.id()}")
            print(error)
        
        for test_case, error in test_result.errors:
            print(f"Error en la prueba: {test_case.id()}")
            print(error)
        
    else:
        print("Todas las pruebas se han ejecutado exitosamente!")


run_tests()