edad = 12

# comparar usuarios
usuario_db = 'yorelacosta'
usuario_escrito = '''yorel_acosta'''
print(usuario_db == usuario_escrito)

if (edad >= 18):
    print('podes pasar')
else:
    print('no podes pasar')
    
if (usuario_db == usuario_escrito):
    print('Iniciando sesión...')
else:
    print('Contraseña equivocada')