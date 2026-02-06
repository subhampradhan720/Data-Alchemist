def detect_factors(conversation):

    factors = {
        "billing_issue": False,
        "delay": False,
        "frustration": False
    }

    for turn in conversation["turns"]:

        text = turn["text"].lower()

        if "bill" in text or "payment" in text:
            factors["billing_issue"] = True

        if "wait" in text or "processing" in text:
            factors["delay"] = True

        if "complain" in text or "again" in text:
            factors["frustration"] = True

    return factors
