# 🧬 COX1 Translator Tool

Herramienta en Python para traducir secuencias COX1 mitocondriales usando Biopython.

---

## 📌 Descripción

Este script permite:

- Leer un archivo FASTA con secuencias de COX1.
- Traducir las secuencias usando la tabla mitocondrial de vertebrados.
- Contar codones STOP (*) en la traducción completa.
- Opcionalmente eliminar el STOP final con el flag --remove_stop.
- Generar:
  - Un archivo FASTA con las proteínas traducidas.
  - Un archivo CSV con un resumen por secuencia.

---

## 🚀 Uso

Comando básico:
python cox1_translator.py -i input.fasta -o carpeta_salida

Con eliminación del codón STOP:
python cox1_translator.py -i input.fasta -o carpeta_salida --remove_stop

---

## 🔧 Dependencias

- Python 3
- Biopython

Instalación rápida con pip:
pip install biopython

O con mamba:
mamba install biopython

---

## 📂 Ejemplo de ejecución

python cox1_translator.py -i dbCOX1.fasta -o results/ --remove_stop

---

## 🗂 Archivos del proyecto

Archivo | Descripción
-------|-------------
cox1_translator.py | Script principal de traducción
dbCOX1.fasta | Secuencias COX1 de ejemplo
dbCOX1_Mitoproteins.fasta | Traducciones generadas
dbCOX1_Mitoresumen.csv | Resumen de traducciones

---

## 👨‍🔬 Autor

Fabricio Villegas Quesada  
Bioinformática • Biotecnología

---

Proyecto desarrollado como parte del entrenamiento profesional en Bioinformática.

