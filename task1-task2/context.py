class Context:

    def __init__(self):
        self.event = None
        self.factors = None
        self.evidence = None
        self.conversations = None

    def update(self, event, factors, evidence, conversations):
        self.event = event
        self.factors = factors
        self.evidence = evidence
        self.conversations = conversations
