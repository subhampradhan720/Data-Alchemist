def generate_explanation(factors):

    explanation = []

    if factors["billing_issue"]:
        explanation.append("Billing problems")

    if factors["delay"]:
        explanation.append("Slow responses")

    if factors["frustration"]:
        explanation.append("Repeated complaints")

    return " → ".join(explanation)
