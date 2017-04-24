"""
classes for holding credential data
"""

import json

def load_service_account_json(filepath):
    """
    loads service account json
    """
    with open(filepath, "r") as file_h:
        return json.loads(file_h.read())

class ServiceAccountCredentials(object):
    """
    a class that loads and presents service account json credentials
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self._json = load_service_account_json(filepath)

    def json(self):
        """
        full credentials file json object
        """
        return self._json.copy()

    def client_email(self):
        """
        service account "client_email" field
        """
        return self._json["client_email"]

    def private_key(self):
        """
        service account "private_key" field
        """
        return self._json["private_key"]

    def project_id(self):
        """
        service account "project_id" field
        """
        return self._json.get("project_id")
