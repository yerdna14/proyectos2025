#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
import re

mayus = string.ascii_uppercase[:13] + 'Ñ' + string.ascii_uppercase[13:]
minus = string.ascii_lowercase[:13] + 'ñ' + string.ascii_lowercase[13:]


def descifrar_a1z27(mensaje):
    # 1) Secuencias de números unidos por guiones -> letras SIN guiones
    #    Ej: "12-05-27"  ->  "lem"
    def convertir_secuencia(m):
        return ''.join(
            minus[int(p) - 1] if 1 <= int(p) <= 27 else p
            for p in m.group().split('-')
        )
    mensaje = re.sub(r'\b\d{2}(?:-\d{2})+\b', convertir_secuencia, mensaje)

    # 2) Números aislados -> letra minúscula
    #    Ej: "12"  ->  "l"
    def convertir_numero(m):
        num = int(m.group())
        return minus[num - 1] if 1 <= num <= 27 else m.group()
    mensaje = re.sub(r'\b\d{2}\b', convertir_numero, mensaje)

    # 3) Limpieza de guiones residuales
    mensaje = mensaje.strip()                    # quitar espacios extremos
    mensaje = re.sub(r'-{2,}', '-', mensaje)     # colapsar "---" en "-"
    mensaje = mensaje.strip('-').strip()         # quitar guiones inicio/final

    # 4) Solo la primera letra en mayúscula, todo lo demás en minúscula
    mensaje = mensaje.lower()
    for i, c in enumerate(mensaje):
        if c.isalpha():
            mensaje = mensaje[:i] + c.upper() + mensaje[i + 1:]
            break

    return mensaje


if __name__ == "__main__":
    print("🔓 DESCIFRADOR A1Z27")
    print("=" * 50)
    while True:
        msg = input("\n📩 Mensaje a descifrar (o Enter para salir): ").strip()
        if not msg:
            break
        print(f"✅ Resultado: '{descifrar_a1z27(msg)}'")