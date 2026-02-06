def extract_evidence(conversation, factors):

    evidence = []

    for i, turn in enumerate(conversation["turns"]):

        text = turn["text"].lower()

        if factors["billing_issue"] and "bill" in text:
            evidence.append((i, turn))

        if factors["delay"] and ("processing" in text or "wait" in text):
            evidence.append((i, turn))

        if factors["frustration"] and "complain" in text:
            evidence.append((i, turn))

    return evidence
