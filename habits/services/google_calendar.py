from datetime import timedelta

from django.conf import settings


def sincronizar_tarea_con_google_calendar(tarea):
    if not getattr(settings, 'GOOGLE_CALENDAR_ENABLED', False):
        tarea.google_calendar_sync_error = ''
        tarea.save(update_fields=['google_calendar_sync_error'])
        return False, 'Google Calendar no esta habilitado.'

    if not tarea.fecha_vencimiento:
        tarea.google_calendar_sync_error = 'La tarea no tiene fecha de vencimiento.'
        tarea.save(update_fields=['google_calendar_sync_error'])
        return False, tarea.google_calendar_sync_error

    if not getattr(settings, 'GOOGLE_CALENDAR_SERVICE_ACCOUNT_FILE', ''):
        tarea.google_calendar_sync_error = 'Falta configurar GOOGLE_CALENDAR_SERVICE_ACCOUNT_FILE.'
        tarea.save(update_fields=['google_calendar_sync_error'])
        return False, tarea.google_calendar_sync_error

    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
    except ImportError:
        tarea.google_calendar_sync_error = 'Faltan instalar las librerias de Google Calendar.'
        tarea.save(update_fields=['google_calendar_sync_error'])
        return False, tarea.google_calendar_sync_error

    try:
        credentials = service_account.Credentials.from_service_account_file(
            settings.GOOGLE_CALENDAR_SERVICE_ACCOUNT_FILE,
            scopes=['https://www.googleapis.com/auth/calendar'],
        )
        service = build('calendar', 'v3', credentials=credentials)
        calendar_id = getattr(settings, 'GOOGLE_CALENDAR_ID', 'primary')
        personas = ', '.join(str(persona) for persona in tarea.personas.all()) or 'Sin asignar'
        event = {
            'summary': tarea.titulo,
            'description': (
                f'Descripcion: {tarea.descripcion or "Sin descripcion"}\n'
                f'Dificultad: {tarea.get_dificultad_display()}\n'
                f'Asignada a: {personas}'
            ),
            'start': {'date': tarea.fecha_vencimiento.isoformat()},
            'end': {'date': (tarea.fecha_vencimiento + timedelta(days=1)).isoformat()},
        }

        if tarea.google_calendar_event_id:
            event_result = service.events().update(
                calendarId=calendar_id,
                eventId=tarea.google_calendar_event_id,
                body=event,
            ).execute()
        else:
            event_result = service.events().insert(
                calendarId=calendar_id,
                body=event,
            ).execute()

        tarea.google_calendar_event_id = event_result.get('id', tarea.google_calendar_event_id)
        tarea.google_calendar_sync_error = ''
        tarea.save(update_fields=['google_calendar_event_id', 'google_calendar_sync_error'])
        return True, 'Tarea sincronizada con Google Calendar.'
    except Exception as error:
        tarea.google_calendar_sync_error = str(error)
        tarea.save(update_fields=['google_calendar_sync_error'])
        return False, tarea.google_calendar_sync_error
