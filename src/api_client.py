from requests import Session


class APIClient:
    def __init__(self):
        self.session = Session()

    def get(self, url, headers=None, params=None):
        return self.session.get(url=url, headers=headers, params=params)

    def close_session(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("@" * 30)
        print(exc_type, exc_val, exc_tb)
        print("@" * 30)
        self.close_session()
