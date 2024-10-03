class TrainModelRequest:
    def __init__(self, user_email: str, resume_id: str, resume_filepath: str, job_description: str):
        self.user_email = user_email
        self.resume_id = resume_id
        self.resume_filepath = resume_filepath
        self.job_description = job_description

