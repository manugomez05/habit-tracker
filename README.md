# Manual del sistema Habit Tracker

Este sistema permite administrar personas, usuarios, roles y tareas. La aplicacion esta pensada para que cada persona vea sus tareas asignadas, mientras que los usuarios con permisos de gestion puedan crear, editar, asignar y controlar el trabajo del equipo.

## 1. Objetivo general

Habit Tracker sirve para organizar tareas dentro de un grupo de personas. Cada tarea puede tener titulo, descripcion, fecha de vencimiento, estado, dificultad y personas asignadas. La dificultad define a que tipo de usuario se le puede asignar la tarea.

El sistema tambien puede conectarse con Google Calendar para crear o actualizar un evento de calendario cuando se guarda una tarea con fecha de vencimiento.

## 2. Componentes principales

El proyecto esta dividido en varios modulos:

- Personas: registra los datos de cada persona del sistema.
- Usuarios: permite iniciar sesion y vincula un usuario de Django con una persona.
- Roles: definen permisos y responsabilidades.
- Tareas: permite crear, consultar, modificar, completar y eliminar tareas.
- Google Calendar: sincroniza tareas con un calendario externo cuando esta configurado.

## 3. Roles del sistema

El sistema usa tres roles principales:

- Integrante: usuario comun. Puede ver sus tareas asignadas y marcarlas como completadas o pendientes.
- Lider: puede gestionar personas y tareas. Puede crear tareas y asignarlas segun la dificultad permitida.
- Administrador: tiene permisos completos. Puede gestionar tareas, personas, roles y eliminar tareas.

## 4. Permisos por rol

Los permisos generales son:

- Integrante:
  - Puede iniciar sesion.
  - Puede ver las tareas que tiene asignadas.
  - Puede completar o desmarcar sus tareas.

- Lider:
  - Puede ver tareas.
  - Puede crear tareas.
  - Puede editar tareas.
  - Puede asignar tareas de dificultad 1 o 2.
  - Puede gestionar personas.

- Administrador:
  - Puede hacer todo lo anterior.
  - Puede asignar tareas de cualquier dificultad.
  - Puede eliminar tareas.
  - Puede cambiar roles.

## 5. Personas

Una persona representa a alguien dentro del sistema. Tiene:

- Nombre.
- Apellido.
- Documento.
- Rol.

Las personas pueden existir aunque todavia no tengan usuario de acceso. Esto permite cargar primero los datos de una persona y luego crear su usuario.

## 6. Usuarios

Un usuario es la cuenta que permite iniciar sesion. Esta vinculado a una persona mediante un perfil. El usuario usa las credenciales de Django, pero el sistema toma el rol desde la persona asociada.

Cuando se registra un usuario comun, se crea automaticamente una persona relacionada y se le asigna el rol Integrante por defecto.

## 7. Tareas

Una tarea tiene:

- Titulo.
- Descripcion.
- Fecha de creacion.
- Fecha de vencimiento.
- Dificultad.
- Estado completada o pendiente.
- Personas asignadas.
- Datos de sincronizacion con Google Calendar.

Las tareas se pueden crear desde la pantalla de tareas si el usuario tiene permiso para gestionarlas.

## 8. Dificultad de tareas

Cada tarea tiene una dificultad de 1 a 3:

- Dificultad 1 - Baja:
  - Se puede asignar a cualquier rol.
  - Roles permitidos: Integrante, Lider y Administrador.

- Dificultad 2 - Media:
  - Se puede asignar a usuarios con mas responsabilidad.
  - Roles permitidos: Lider y Administrador.

- Dificultad 3 - Alta:
  - Solo se puede asignar a administradores.
  - Rol permitido: Administrador.

Esta regla se aplica en dos lugares:

- En la pantalla, porque al cambiar la dificultad se actualiza la lista de personas disponibles.
- En el servidor, porque el formulario valida que las personas seleccionadas puedan resolver esa dificultad.

Esto evita que se guarde una tarea mal asignada aunque alguien intente enviar datos incorrectos desde fuera de la pantalla.

## 9. Crear una tarea

Para crear una tarea:

1. Iniciar sesion con un usuario Lider o Administrador.
2. Entrar a Tareas.
3. Presionar Crear tarea.
4. Completar el titulo.
5. Agregar descripcion si corresponde.
6. Elegir fecha de vencimiento si se quiere agendar o controlar una fecha.
7. Seleccionar dificultad.
8. Elegir personas asignadas.
9. Guardar.

Al elegir la dificultad, el sistema muestra solo personas compatibles con esa dificultad.

Si Google Calendar esta habilitado y la tarea tiene fecha de vencimiento, se crea un evento de dia completo en el calendario configurado.

## 10. Modificar una tarea

Para modificar una tarea:

1. Entrar a Tareas.
2. Presionar Editar en la tarea correspondiente.
3. Cambiar titulo, descripcion, vencimiento, dificultad, estado o personas.
4. Guardar cambios.

Cuando se guarda una tarea modificada, el sistema vuelve a intentar sincronizarla con Google Calendar. Si ya tenia un evento asociado, se actualiza ese evento.

## 11. Completar una tarea

Una tarea puede marcarse como completada desde el listado. Si ya estaba completada, puede desmarcarse.

Un Integrante solo puede completar o desmarcar tareas asignadas a su persona. Un Lider o Administrador puede hacerlo sobre las tareas que gestiona.

## 12. Eliminar una tarea

Solo un Administrador puede eliminar tareas. La eliminacion se hace desde la pantalla de confirmacion para evitar borrados accidentales.

## 13. Listado de tareas

La pantalla de tareas muestra:

- ID de la tarea.
- Titulo.
- Descripcion resumida.
- Estado.
- Fecha de vencimiento.
- Dificultad.
- Cantidad de personas asignadas.
- Estado de Google Calendar si corresponde.

Los Lideres y Administradores ven todas las tareas. Los Integrantes ven solamente las tareas asignadas a ellos.

## 14. Detalle de una tarea

El detalle de una tarea muestra:

- Titulo.
- Descripcion.
- Estado.
- Fecha de vencimiento.
- Dificultad.
- Personas asignadas.
- Fecha de creacion.
- Estado de Google Calendar.

Si la tarea fue agendada, se muestra como agendada. Si no se pudo sincronizar, se muestra el mensaje de error guardado.

## 15. Google Calendar

La integracion con Google Calendar permite crear o actualizar un evento cuando se guarda una tarea.

La tarea se agenda como evento de dia completo usando la fecha de vencimiento. El evento incluye:

- Titulo de la tarea.
- Descripcion.
- Dificultad.
- Personas asignadas.

## 16. Activar Google Calendar

La integracion esta controlada por variables de entorno. Esto permite que el sistema funcione aunque no haya credenciales cargadas.

Variables necesarias:

- GOOGLE_CALENDAR_ENABLED=True
- GOOGLE_CALENDAR_ID=primary
- GOOGLE_CALENDAR_SERVICE_ACCOUNT_FILE=ruta/al/archivo/service-account.json

GOOGLE_CALENDAR_ID puede ser primary o el ID de un calendario especifico.

GOOGLE_CALENDAR_SERVICE_ACCOUNT_FILE debe apuntar al archivo JSON de una cuenta de servicio de Google.

## 17. Preparar Google Calendar en Google Cloud

Pasos generales:

1. Entrar a Google Cloud Console.
2. Crear un proyecto o usar uno existente.
3. Habilitar Google Calendar API.
4. Crear una cuenta de servicio.
5. Descargar el archivo JSON de credenciales.
6. Compartir el calendario de Google con el email de la cuenta de servicio.
7. Dar permisos para crear y modificar eventos.
8. Configurar las variables de entorno en el entorno donde corre Django.

El email de la cuenta de servicio aparece dentro del archivo JSON o en Google Cloud.

## 18. Funcionamiento de la sincronizacion

Cuando se crea o modifica una tarea:

1. El sistema guarda la tarea.
2. Revisa si Google Calendar esta habilitado.
3. Revisa si la tarea tiene fecha de vencimiento.
4. Revisa si existen credenciales configuradas.
5. Crea o actualiza el evento.
6. Guarda el ID del evento en la tarea.
7. Si ocurre un error, guarda el mensaje en la tarea.

Si Google Calendar no esta habilitado, la tarea se guarda igual.

## 19. Campos de Google Calendar en tareas

Cada tarea tiene dos campos internos:

- google_calendar_event_id: guarda el ID del evento creado en Google Calendar.
- google_calendar_sync_error: guarda el ultimo error de sincronizacion.

Estos campos ayudan a saber si la tarea fue agendada correctamente.

## 20. Instalacion del proyecto

Pasos recomendados:

1. Crear un entorno virtual.
2. Instalar dependencias desde requirements.txt.
3. Aplicar migraciones.
4. Crear roles iniciales.
5. Crear un usuario administrador.
6. Iniciar el servidor.

Comandos habituales:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py create_default_roles
python manage.py createsuperuser
python manage.py runserver
```

Tambien existe un comando propio para hacer administrador a un usuario, segun la configuracion del proyecto.

## 21. Migraciones

Las migraciones registran los cambios de base de datos. En este sistema se agrego:

- Campo dificultad en tareas.
- Campos de Google Calendar.
- Conversion de dificultades anteriores Baja, Media y Alta hacia 1, 2 y 3.

Esto permite conservar datos existentes.

## 22. API interna de personas por dificultad

La pantalla de crear y editar tarea usa una ruta interna:

```text
/personas_por_dificultad/?dificultad=1
```

Devuelve las personas que pueden recibir una tarea con esa dificultad. La usa la pantalla para actualizar el selector sin recargar toda la pagina.

Esta ruta requiere iniciar sesion y tener permiso para gestionar tareas.

## 23. Seguridad

El sistema protege las pantallas con login. Tambien revisa permisos segun rol.

Reglas importantes:

- Si un usuario no inicio sesion, se redirige al login.
- Si un Integrante intenta entrar a una tarea no asignada, recibe error de permiso.
- Si un usuario sin permisos intenta crear, editar o eliminar tareas, recibe error de permiso.
- La dificultad se valida en servidor, no solo en pantalla.

## 24. Administracion de roles

El Administrador puede cambiar roles desde la pantalla correspondiente. Esto permite promover o degradar personas entre Integrante, Lider y Administrador.

El rol impacta directamente en:

- Acceso a pantallas.
- Capacidad de gestionar tareas.
- Capacidad de gestionar personas.
- Posibilidad de recibir tareas de dificultad 1, 2 o 3.

## 25. Flujo recomendado de uso

1. Crear roles iniciales.
2. Crear usuario administrador.
3. Cargar personas.
4. Crear usuarios para las personas que van a iniciar sesion.
5. Asignar roles.
6. Crear tareas con dificultad.
7. Asignar tareas solo a personas permitidas.
8. Revisar tareas desde el listado o desde el inicio.
9. Completar tareas al finalizar.

## 26. Problemas comunes

Si no aparecen personas para asignar:

- Revisar la dificultad elegida.
- Revisar que las personas tengan rol.
- Revisar que existan personas con rol compatible.

Si Google Calendar no agenda:

- Revisar que GOOGLE_CALENDAR_ENABLED sea True.
- Revisar que GOOGLE_CALENDAR_SERVICE_ACCOUNT_FILE apunte al JSON correcto.
- Revisar que el calendario este compartido con la cuenta de servicio.
- Revisar que la tarea tenga fecha de vencimiento.
- Revisar el mensaje guardado en el detalle de la tarea.

Si un usuario no ve tareas:

- Revisar que este vinculado a una persona.
- Revisar que la tarea este asignada a esa persona.
- Si es Lider o Administrador, revisar que su persona tenga el rol correcto.

## 27. Mantenimiento

Para mantener el sistema:

- Ejecutar migraciones despues de actualizar el codigo.
- Mantener requirements.txt instalado.
- No guardar credenciales de Google dentro del repositorio.
- Usar variables de entorno para configuraciones sensibles.
- Revisar errores de sincronizacion en tareas cuando Calendar este habilitado.

## 28. Resumen de reglas de dificultad

La regla central del sistema es:

```text
Dificultad 1 -> Integrante, Lider o Administrador
Dificultad 2 -> Lider o Administrador
Dificultad 3 -> Administrador
```

Esta regla se respeta al crear y al modificar tareas.
