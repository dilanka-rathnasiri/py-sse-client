class HttpRespException(Exception):
    def __init__(self, message, status, headers):
        super().__init__(message)
        self.message = message
        self.status = status
        self.headers = headers

    def __str__(self):
        return (
            f"HttpRespException:\n"
            f"  Message: {self.message}\n"
            f"  Status: {self.status}\n"
            f"  Headers: {self.headers}"
        )
