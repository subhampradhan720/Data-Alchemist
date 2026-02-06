from retriever import retrieve_conversations
from causal_model import detect_factors
from evidence import extract_evidence
from explainer import generate_explanation
from context import Context


context = Context()


def detect_event(query):

    if "cancel" in query.lower():
        return "cancellation"

    if "resolve" in query.lower():
        return "resolved"

    return context.event   # fallback to memory


def main():

    print("Type 'exit' to stop.\n")

    while True:

        query = input("You: ")

        if query.lower() == "exit":
            break


        # Step 1: Detect event (new or old)
        event = detect_event(query)

        if event is None:
            print("System: No previous context.")
            continue


        # Step 2: Get conversations
        conversations = retrieve_conversations(event)


        all_factors = {}
        all_evidence = []


        # Step 3: Analyze
        for convo in conversations:

            factors = detect_factors(convo)
            evidence = extract_evidence(convo, factors)

            all_factors[convo["id"]] = factors
            all_evidence.extend(evidence)


        # Step 4: Save in context
        context.update(
            event,
            all_factors,
            all_evidence,
            conversations
        )


        # Step 5: Handle follow-ups
        if "evidence" in query.lower():

            print("\nSystem: Supporting Evidence:")

            for i, turn in context.evidence:
                print(f"Turn {i} | {turn['speaker']}: {turn['text']}")

            continue


        if "most important" in query.lower() or "main cause" in query.lower():

            counts = {
                "billing_issue": 0,
                "delay": 0,
                "frustration": 0
            }

            for f in context.factors.values():
                for k in counts:
                    if f[k]:
                        counts[k] += 1

            main_cause = max(counts, key=counts.get)

            print("\nSystem: Main Cause:", main_cause)
            continue


        # Step 6: Normal explanation
        print("\nSystem: Causal Explanation:")

        for convo_id, factors in context.factors.items():

            exp = generate_explanation(factors)

            print(f"Conversation {convo_id}: {exp}")


if __name__ == "__main__":
    main()
