# 🚌 Sistema Inteligente de Rutas en Transporte Masivo  

## 📌 Descripción  
Este proyecto implementa un **sistema inteligente basado en conocimiento** que permite calcular la **mejor ruta entre dos estaciones** dentro de un sistema de transporte masivo local.  

El sistema utiliza:  
- Una **base de conocimiento** escrita como hechos y reglas en Python.  
- Un algoritmo de **búsqueda heurística (A\*)**, con penalización por transbordos y opción de heurística basada en coordenadas.  
- Pruebas automáticas para verificar el correcto funcionamiento.  

La solución está inspirada en la idea de los **sistemas expertos basados en reglas**, que aplican estrategias de búsqueda para resolver problemas de decisión.  

---

## ⚙️ Tecnologías utilizadas  
- **Python 3.10+** → lenguaje principal.  
- **pytest** → framework para pruebas automáticas.  
- *(opcional)* **networkx** → para manipulación de grafos, si se amplía el proyecto.  

---

## 📥 Instalación  

### 1. Clonar el repositorio  
```bash
git clone https://github.com/kevinruiz1811/ibero_inteligencia_artificial
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv

venv\Scripts\activate   # en Windows CMD/PowerShell
source venv/bin/activate # en Linux/Mac
```

# USO
```bash
python src/main.py
```