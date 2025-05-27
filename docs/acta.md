# Actas de Reunión — Proyecto Final ARQ 2025-1

**Grupo:** Juan Riaño, Samuel Ramírez, Gabriela Delgado, Sergio Morales  
**Docente:** Oscar Andrés Arias  
**Repositorio:** https://github.com/JuanjoRiano/cpu-simulator-arquitectura

---

## 📅 Reunión 29 de abril

**Asistentes:** Todos  
**Temas tratados:**
- Revisión del documento oficial de proyecto.
- Distribución de roles según fortalezas individuales.
- Acuerdo en usar Python y GitHub para control de versiones.
- Juan creará la estructura base del repositorio y el README inicial.

**Acuerdos:**
- Juan es el líder del proyecto.
- Samuel tomará el diseño de CPU y pipeline.
- Gabriela se encargará de caché e I/O.
- Sergio será responsable de benchmarks, informe y presentación.

---

## 📅 Reunión 2 — 6 de mayo

**Asistentes:** Todos  
**Temas tratados:**
- Validación de carpetas base (`cpu/`, `cache/`, `io/`, `benchmarks/`, `docs/`, `slides/`).
- Confirmación de plantillas para PR y actas (pendiente implementación).
- Samuel presentó el esqueleto de `instruction.py` y `pipeline.py`.

**Acuerdos:**
- Agregar `run_pipeline.py` para integración.
- Gabriela empezará `cache.py` con mapeo directo.
- Sergio comenzará con `memory_bench.py`.

---

## 📅 Reunión 3 — 13 de mayo

**Asistentes:** Todos
**Temas tratados:**
- Samuel integró forwarding en el pipeline.
- Gabriela ya simula `read()`/`write()` en caché.
- Se revisó `memory_bench.py`, aún sin guardar resultados CSV.

**Acuerdos:**
- Juan subirá guía de estilo PEP8.
- Gabriela empezará el módulo `io_device.py`.
- Samuel comenzará tests con `pytest`.

---

## 📅 Reunión 4 — 20 de mayo

**Asistentes:** Todos  
**Temas tratados:**
- Revisión del `test_forwarding.py`, pasando con éxito.
- Gabriela ya maneja interrupciones en `io_device.py`.
- Sergio tiene esqueleto de informe `.docx`, pero benchmarks aún en borrador.

**Acuerdos:**
- Sergio entregará `program1.py`, `program2.py`, `program3.py` antes del 25.
- Agregar `results_all.csv` como consolidado de métricas.
- Preparar estructura de presentación (`slides/`).

---

## 📅 Reunión 5 — 26 de mayo

**Asistentes:** Todos  
**Temas tratados:**
- Confirmado: Samuel y Gabriela han terminado sus módulos y pruebas.
- Revisión de la estructura actual del proyecto con `tree /F`.
- Sergio aún no ha entregado los benchmarks ni el informe final.

**Acuerdos:**
- Sergio debe entregar todo lo pendiente antes del 27 de mayo.
- Juan revisará PRs y hará última verificación general del repositorio.

---

## 📅 Reunión Final — 26 de mayo

**Asistentes:** Todos  
**Temas tratados:**
- Verificación final de todos los entregables.
- Revisión de benchmarks, resultados y presentación.
- Ensayo de la exposición oral.

**Acuerdos:**
- El proyecto fue completado en su totalidad:
  - CPU funcional con manejo de hazards.
  - Caché parametrizable e I/O con interrupciones.
  - Benchmarks listos y resultados consolidados.
  - Informe final redactado y formateado.
  - Presentación preparada.

**Observación final:**  
Se subieron todos los archivos al repositorio y el equipo está listo para la entrega oficial y presentación ante el docente.

---

