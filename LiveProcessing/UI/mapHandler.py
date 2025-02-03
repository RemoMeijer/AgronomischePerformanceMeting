import json

class MapHandler:
    def __init__(self, backend):
        self.backend = backend

    def goto_field(self, field_id):
        data = {
            "identifier": "field",  # Add an identifier
            "field_id": field_id  # Include the field ID
        }

        json_data = json.dumps(data)

        self.backend.send_data_to_js.emit(json_data)
