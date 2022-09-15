from filestack import Client


class Fileshare:

    def __init__(self, filepath, api_key='Al0C1in1mR42P8CYYetstz'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url
