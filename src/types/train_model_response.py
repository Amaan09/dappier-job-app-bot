class TrainModelResponse:
    def __init__(self, status: str, namespace_id: str):
        self.status = status
        self.namespace_id = namespace_id

    def to_dict(self) -> dict:
        return {
            "status": self.status,
            "namespace_id": self.namespace_id,
        }
