def check_response(response):
    issues = []

    if not response.strip():
        issues.append("Empty response")

    if len(response.split()) < 5:
        issues.append("Response too short")

    banned_words = ["hate", "kill", "stupid"]

    for word in banned_words:
        if word in response.lower():
            issues.append(f"Banned word detected: {word}")

    if response.count(".") > 0:
        sentences = response.split(".")
        unique_sentences = set(sentences)

        if len(sentences) != len(unique_sentences):
            issues.append("Repeated sentences detected")

    if issues:
        print("FAIL")
        print("Issues found:")

        for issue in issues:
            print("-", issue)

    else:
        print("PASS")
        print("Response looks good")


sample_response = input("Enter AI response: ")

check_response(sample_response)