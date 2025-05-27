# 🚀 Pull Request: Benchmarks finales + Informe técnico

## 📋 Descripción

Este pull request incluye las siguientes contribuciones principales:

- [x] **Sergio Morales**: Integración de resultados de benchmarks (`benchmarks/results_all.csv`) y análisis en `docs/tablas_metricas.md`. Generación de gráficos de rendimiento.
- [x] **Juan Riaño**: Redacción y subida del informe final en `docs/informe_final.md`, incluyendo resumen ejecutivo, descripción de arquitectura, resultados y conclusiones.

## 🧪 Pasos para probar

1. Ejecutar `python run_pipeline.py benchmarks/program1.py` y verificar la salida de métricas.
2. Revisar el archivo `benchmarks/results_all.csv` y confirmar los resultados de los tres programas.
3. Verificar que el informe final se encuentra completo en `docs/informe_final.md`.
4. Confirmar que las gráficas se generaron correctamente (`docs/imgs/*.png` si se usaron).
5. Revisar formato y ortografía del informe.

## 🏷️ Etiqueta

`documentation`, `benchmarking`, `final`

## ✅ Checklist

- [x] Los resultados del pipeline fueron recolectados correctamente.
- [x] Se ejecutaron sin errores los scripts de prueba (`program1.py`, `program2.py`, `program3.py`).
- [x] El informe cumple con la estructura solicitada por el docente.
- [x] Código formateado con `black` y pasó `flake8`.
- [x] Todas las pruebas `pytest` siguen pasando.
