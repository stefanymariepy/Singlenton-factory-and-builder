// ── Singleton en C++ ──────────────────────────
#include <iostream>
using namespace std;

class Config {
private:
    static Config* instance;  // puntero a la única instancia
    Config() {}               // constructor privado → nadie puede hacer new Config()

public:
    // Si no existe instancia, la crea; si ya existe, devuelve la misma
    static Config* getInstance() {
        if (!instance) instance = new Config();
        return instance;
    }

    string mensaje;           // atributo de configuración global

    void showMessage() {
        cout << mensaje << "\n";
    }
};

// Inicializar el puntero estático en nullptr
Config* Config::instance = nullptr;

int main() {
    Config* obj1 = Config::getInstance();  // crea la instancia
    Config* obj2 = Config::getInstance();  // devuelve la MISMA

    obj1->mensaje = "Configuración global cargada.";
    obj1->showMessage();
    
    // obj1 y obj2 apuntan al mismo objeto
    cout << "¿Son iguales? " << (obj1 == obj2) << endl;
}