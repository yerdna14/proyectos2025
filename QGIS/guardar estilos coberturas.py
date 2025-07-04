colores_cov = {
            '1.1.1. Tejido urbano continuo': (204, 0, 0),
            '1.1.2. Tejido urbano discontinuo': (248, 0, 0),
            '1.2.1. Zonas industriales o comerciales': (204, 77, 42),
            '1.2.2. Red vial, ferroviaria y terrenos asociados': (217, 101, 69),
            '1.2.3. Zonas portuarias': (225, 132, 107),
            '1.2.4. Aeropuertos': (231, 156, 135),
            '1.2.5. Obras hidráulicas': (238, 185, 170),
            '1.3.1. Zonas de extracción minera': (167, 0, 204),
            '1.3.2. Zona de disposición de residuos': (212, 23, 255),
            '1.4.1. Zonas verdes urbanas': (255, 128, 128),
            '1.4.2. Instalaciones recreativas': (255, 176, 176),
            '2.1.1. Otros cultivos transitorios': (255, 255, 166),
            '2.1.2. Cereales': (255, 255, 95),
            '2.1.3. Oleaginosas y leguminosas': (238, 232, 0),
            '2.1.4. Hortalizas': (209, 206, 0),
            '2.1.5. Tubérculos': (181, 178, 0),
            '2.2.1. Cultivos permanentes herbáceos': (242, 205, 167),
            '2.2.2. Cultivos permanentes arbustivos': (237, 183, 128),
            '2.2.3. Cultivos permanentes arbóreos': (232, 161, 90),
            '2.2.4. Cultivos agroforestales': (227, 141, 54),
            '2.2.5. Cultivos confinados': (214, 122, 30),
            '2.3.1. Pastos limpios': (204, 255, 204),
            '2.3.2. Pastos arbolados': (158, 255, 158),
            '2.3.3. Pastos enmalezados': (158, 255, 200),
            '2.4.1. Mosaico de cultivos': (255, 230, 166),
            '2.4.2. Mosaico de pastos y cultivos': (255, 216, 117),
            '2.4.3. Mosaico de cultivos, pastos y espacios naturales': (255, 201, 64),
            '2.4.4. Mosaico de pastos con espacios naturales': (255, 183, 0),
            '2.4.5. Mosaico de cultivos con espacios naturales': (214, 154, 0),
            '3.1.1. Bosque denso': (71, 143, 0),
            '3.1.2. Bosque abierto': (85, 171, 0),
            '3.1.3. Bosque fragmentado': (97, 194, 0),
            '3.1.4. Bosque de galería y ripario': (112, 224, 0),
            '3.1.5. Plantación forestal': (128, 255, 0),
            '3.2.1. Herbazal': (204, 242, 78),
            '3.2.2. Arbustal': (172, 219, 15),
            '3.2.3. Vegetación secundaria o en transición': (150, 191, 13),
            '3.3.1. Zonas arenosas naturales': (194, 194, 194),
            '3.3.2. Afloramientos rocosos': (179, 179, 179),
            '3.3.3. Tierras desnudas y degradadas': (158, 158, 158),
            '3.3.4. Zonas quemadas': (138, 138, 138),
            '3.3.5. Zonas glaciares y nivales': (101, 101, 181),
            '4.1.1. Zonas Pantanosas': (166, 166, 255),
            '4.1.2. Turberas': (145, 145, 255),
            '4.1.3. Vegetación acuática sobre cuerpos de agua': (115, 115, 255),
            '4.2.1. Pantanos costeros': (204, 204, 255),
            '4.2.2. Salitral': (184, 184, 255),
            '4.2.3. Sedimentos expuestos en bajamar': (166, 166, 255),
            '5.1.1. Ríos': (0, 0, 248),
            '5.1.2. Lagunas, lagos y ciénagas naturales': (0, 128, 255),
            '5.1.3. Canales': (0, 178, 255),
            '5.1.4. Cuerpos de agua artificiales': (0, 206, 242),
            '5.2.1. Lagunas costeras': (69, 224, 245),
            '5.2.3. Estanques para acuicultura marina': (204, 246, 255)
        }


# Aplicar a capas por nombre
aplicar_estilo_comun_a_capas(
    capas = todas_capas,
    campo = 'nivel_3',  # Campo común en todas las capas
    colores_por_valor = colores_cov,
    borde_color='0,0,0',    # Borde negro
    grosor_borde=0.3        # 0.3 mm de grosor
)


# Opción 1: Guardar estilo predeterminado para TODAS las capas del proyecto
for capa in QgsProject.instance().mapLayers().values():
    capa.saveDefaultStyle()  # Guarda el estilo actual como predeterminado PARA ESA CAPA
    print(f"Estilo guardado como predeterminado para: {capa.name()}")