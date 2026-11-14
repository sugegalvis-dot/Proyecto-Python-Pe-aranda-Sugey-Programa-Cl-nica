# Gestor de Diagnóstico Clínico - ACME Clinic

Programa en Python que sistematiza el proceso de diagnóstico de pacientes.

- Sugey Nathalia Peñaranda Galvis

## Funcionalidades
1. Login: acceso con e-mail y contraseña.
2. Registro de usuarios: médicos y administrativos.
3. Registro de pacientes.
4. Diagnosticar pacientes: síntomas, diagnóstico y prescripción médica (solo médicos).
5. Historia clínica: consulta por número de identificación del paciente.

## Archivos
- `main.py`: archivo principal y menú.
- `almacenamiento.py`: lee y guarda los archivos JSON.
- `login.py`: modulo-inicio de sesión.
- `usuarios.py`: m-registro de usuarios.
- `pacientes.py`: m-registro y búsqueda de pacientes.
- `diagnostico.py`: m-diagnóstico y prescripción.
- `historia.py`: m-historia clínica.
- `datos.json`: almacena usuarios, pacientes y consultas.

## Cómo ejecutarlo
1. Ejecutar `main.py`.
2. Iniciar sesión con el usuario inicial:
   - E-mail: admin@acmeclinic.com
   - Contraseña: admin123
3. crear usuario médico para que pueda diagnosticar

## Notas
- Cada diagnóstico genera un archivo JSON de prescripción, asociado a una fecha, un paciente y un médico.
- Los roles son `medico` y `administrativo`; solo los médicos pueden diagnosticar. (es necesario crear el usuario médico)
