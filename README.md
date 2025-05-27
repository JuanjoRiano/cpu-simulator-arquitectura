# 🧠 CPU Simulator - Arquitectura de Computadores 🖥️

Simulador educativo de una arquitectura de computador simplificada, desarrollado en Python como proyecto final del curso **Arquitectura de Computadores** en la Universidad Sergio Arboleda.

## 🎯 Objetivos del Proyecto

- Aplicar conceptos de jerarquía de memoria, ILP, pipeline y arquitectura VLIW.
- Diseñar un simulador modular con CPU, memoria caché e interfaces de entrada/salida.
- Evaluar el rendimiento mediante benchmarks controlados.
- Fomentar el trabajo en equipo, control de versiones, documentación y presentación de resultados.

---

## ⚙️ Estructura del Repositorio

```
cpu-simulator-arquitectura/
├── cpu/                # Lógica del procesador y pipeline
├── cache/              # Simulación de memoria caché (directo y 2-way)
├── io/                 # Dispositivos ficticios de entrada/salida
├── benchmarks/         # Scripts de prueba y resultados
├── docs/               # Documentación técnica e informes
├── slides/             # Presentación final
├── run_pipeline.py     # Script principal de ejecución del simulador
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Este archivo
```

---

## 🚀 Ejecución

1. Clona el repositorio:

```bash
git clone https://github.com/JuanjoRiano/cpu-simulator-arquitectura.git
cd cpu-simulator-arquitectura
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta un programa de prueba:

```bash
python run_pipeline.py benchmarks/program1.py
```

Esto imprimirá en consola las métricas del pipeline:

```
Ciclos totales: 105
Instrucciones ejecutadas: 34
Stalls: 4
Cache Hits: 89 | Misses: 11
```

---

## 🧪 Benchmarks

Contamos con tres programas base en `benchmarks/`:

- `program1.py`: operaciones aritméticas intensivas.
- `program2.py`: accesos masivos a memoria.
- `program3.py`: saltos condicionales frecuentes.

Los resultados se consolidan en:  
📄 `benchmarks/results_all.csv`

---

## 🛠️ Componentes Clave

- ✅ **Pipeline de 5 etapas**: IF → ID → EX → MEM → WB
- ✅ **Manejo de Hazards**: forwarding y stalling
- ✅ **Memoria caché**: mapeo directo y asociativo 2-way
- ✅ **E/S programada e interrupciones**
- ✅ **Estadísticas de rendimiento y visualización de resultados**

---

## 📚 Documentación

Consulta:

- `docs/informe_final.md`: Informe completo del proyecto
- `docs/README_cache_io.md`: Uso de caché y E/S
- `docs/tablas_metricas.md`: Comparativas y análisis
- `slides/presentation.pptx`: Presentación final del equipo

---

## 🔍 Buenas Prácticas

- Estilo de código validado con **PEP8** usando [`flake8`](https://flake8.pycqa.org/) y [`black`](https://black.readthedocs.io/).
- Pruebas automáticas con `pytest`.
- Control de versiones y ramas (`main`, `dev`) usando PRs revisados.

---

## 👥 Equipo

- **Juan Riaño** — Líder del Proyecto
- **Samuel Ramírez** — Arquitecto de CPU
- **Gabriela Delgado** — Especialista en Memoria y E/S
- **Sergio Morales** — Analista y Documentador

---

## 📄 Licencia

Proyecto académico sin fines de lucro. Uso libre con fines educativos.

