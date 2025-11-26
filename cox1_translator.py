#!/usr/bin/env python

import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import csv
import os

def parse_args():
    parser = argparse.ArgumentParser(
        description="Análisis simple de secuencias Mitocondriales (longitud, %GC, traducción, stops)."
    )
    parser.add_argument(
        "-i", "--input",
        required=True,
        help="Archivo FASTA de entrada (por ejemplo: dbCOX1.fasta)"
    )
    parser.add_argument(
        "-o", "--output_prefix",
        default="results/COX1",
        help="Prefijo para los archivos de salida (por defecto: results/COX1)"
    )

    parser.add_argument(
        "--remove_stop",
        action="store_true",
        help="Si se usa, elimina el STOP final durante la traduccion (to_stop=True)"
    )
    return parser.parse_args()

def main():

    args = parse_args()

    input_fasta = args.input
#Devolver si no existe fasta
    if not os.path.isfile(input_fasta):
        print(f"❌ Error: El archivo FASTA '{input_fasta}' no existe.")
        return

    output_prefix = args.output_prefix

    # Crear carpeta de salida si no existe
    out_dir = os.path.dirname(output_prefix)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    output_csv = output_prefix + "_Mitoresumen.csv"
    output_prot_fasta = output_prefix + "_Mitoproteins.fasta"

    # Leer secuencias
    registros = list(SeqIO.parse(input_fasta, "fasta"))

    if len(registros) == 0:
        print(f"⚠ No se encontraron secuencias en {input_fasta}")
        return

    resumen = []
    traducciones = []

    for record in registros:
        seq = record.seq
        length = len(seq)

        # %GC
        gc = 0
        if length > 0:
            gc = (seq.count("G") + seq.count("C")) / length * 100

        # Traducción
        prot_full  = seq.translate("Vertebrate Mitochondrial")
        n_stops = prot_full.count("*")

        if args.remove_stop:
            prot=seq.translate("Vertebrate Mitochondrial", to_stop=True)
        else:
            prot = prot_full

        resumen.append({
            "id": record.id,
            "length_nt": length,
            "gc": round(gc, 2),
            "length_aa": len(prot),
            "stops": n_stops
        })

        nuevo_record = SeqRecord(
            prot,
            id=record.id + "_prot",
            description=f"Traduccion | Longitud: {len(prot)} aa | Stops: {n_stops}"
        )
        traducciones.append(nuevo_record)

    # Guardar CSV
    with open(output_csv, "w", newline="") as f:
        campos = ["id", "length_nt", "gc", "length_aa", "stops"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(resumen)

    # Guardar proteínas traducidas
    SeqIO.write(traducciones, output_prot_fasta, "fasta")

    print("\n📌 Resultado del análisis")
    print(f"✅ Analizadas {len(registros)} secuencias.")
    print(f"📄 Resumen guardado en: {output_csv}")
    print(f"🧬 Proteínas traducidas en: {output_prot_fasta}")
    print(f"🔎 STOPs detectados (antes de aplicar --remove_stop): {n_stops}")


if __name__ == "__main__":
    main()
