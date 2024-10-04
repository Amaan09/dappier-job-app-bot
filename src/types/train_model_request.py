class TrainModelRequest:
    def __init__(self, user_email: str, reference_id: str, resume_filepath: str, job_description: str):
        self.user_email = user_email
        self.reference_id = reference_id
        self.resume_filepath = resume_filepath
        self.job_description = job_description

