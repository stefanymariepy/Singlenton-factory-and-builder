// ============================================================
// PATRON DE DISEÑO: SINGLETON
// Objetivo: garantizar que la clase Config tenga UNA SOLA
// instancia durante toda la ejecucion del programa.
// ============================================================

#include <iostream>
using namespace std;

class Config {
private:
    // Puntero estatico que guarda la unica instancia.
    // Es static porque pertenece a la clase, no a un objeto.
    static Config* instancia;

    // Constructor PRIVADO: impide que alguien haga "new Config()"
    // desde fuera de la clase. Solo la propia clase puede crearse.
    Config() {
        cout << "Config creada por primera y unica vez.\n";
    }
public:
    // Metodo estatico de acceso global.
    // Si 'instancia' es nullptr (no existe), la crea.
    // Si ya existe, simplemente la devuelve.
    // Esto garantiza que siempre sea la MISMA instancia.
    static Config* getInstance() {
        if (!instancia) {
            instancia = new Config(); // solo se ejecuta UNA vez
        }
        return instancia;
    }

    // Metodo de ejemplo que usa la instancia
    void mostrarMensaje() {
        cout << "Configuracion global cargada.\n";
    }
};

// Inicializacion obligatoria del puntero estatico fuera de la clase
Config* Config::instancia = nullptr;
int main() {
    cout << "=== PATRON SINGLETON ===\n\n";

    // Los tres punteros llaman a getInstance().
    // La primera vez crea la instancia; las demas veces
    // devuelven exactamente el mismo objeto ya creado.
    Config* obj1 = Config::getInstance();
    Config* obj2 = Config::getInstance();
    Config* obj3 = Config::getInstance();

    obj1->mostrarMensaje();

    // Las tres direcciones de memoria deben ser IDENTICAS
    cout << "\nDireccion obj1: " << obj1 << "\n";
    cout << "Direccion obj2: " << obj2 << "\n";
    cout << "Direccion obj3: " << obj3 << "\n";

    // Comparacion de punteros: deben ser iguales (mismo objeto)
    cout << "\n¿Son iguales obj1 y obj2? " << (obj1==obj2 ? "SI" : "NO") << "\n";
    cout << "¿Son iguales obj2 y obj3? " << (obj2==obj3 ? "SI" : "NO") << "\n";
    return 0;
}
