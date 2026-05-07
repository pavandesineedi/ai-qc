def check_response(response):
    issues = []
    score = 100

    if not response.strip():
        issues.append("Empty response")
        score -= 40

    if len(response.split()) < 4:
        issues.append("Response too short")
        score -= 20

    banned_words = ["hate", "kill", "stupid"]

    for word in banned_words:
        if word in response.lower():
            issues.append(f"Banned word detected: {word}")
            score -= 30

    words = response.lower().split()

    if len(words) != len(set(words)):
        repeated_count = len(words) - len(set(words))

        if repeated_count >= 2:
            issues.append("Too many repeated words detected")
            score -= 25

    if "." in response:
        sentences = [s.strip() for s in response.split(".") if s.strip()]

        if len(sentences) != len(set(sentences)):
            issues.append("Repeated sentences detected")
            score -= 20
    
    if response.isupper():
        issues.append("Response contains excessive uppercase text")
        score -= 15

    if "!!!" in response or "???" in response:
        issues.append("Spam punctuation detected")
        score -= 10

    score = max(score, 0)

    print("\n===== AI RESPONSE ANALYSIS =====")

    if issues:
        print("Status : FAIL")
        print(f"Quality Score : {score}/100")
        print("\nIssues Found:")

        for issue in issues:
            print("-", issue)

    else:
        print("Status : PASS")
        print(f"Quality Score : {score}/100")
        print("Response looks good")


with open("data1/responses.txt", "r") as file:
    responses = file.readlines()

for response in responses:
    print("\nChecking Response:")
    print(response.strip())

    check_response(response.strip())