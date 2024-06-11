Nombre_completo = input("Ingresar nombre")











def buscar_datos(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print("key", key, "value", value)
        for k, v in value.items():
            print("k", k, "v", v)

database = {
    "persona1": {
        "primer_nombre": "Pablo",
        "segundo_nombre": "Diego",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Picasso"
    },
    "persona2": {
        "primer_nombre": "Lionel",
        "segundo_nombre": "Andres",
        "primer_apellido": "Messi",
        "segundo_apellido": "Cuccitini"
    }

}
buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)