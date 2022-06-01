def note_to_json(note):
    return {
        "id": note.id,
        "title": note.title,
        "message": note.message,
        "public": note.public,
            }

def note_created(note):
    return {
        "id": note.id,
        "title": note.title,
        "message": note.message,
        "public": note.public,
        "created_at": note.create_at,
        "updated_at": note.update_at
    }