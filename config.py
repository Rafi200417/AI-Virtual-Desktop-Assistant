import wolframalpha


def WolfRamAlpha(query):
    apikey = "E2HK4P-9WJG6JLJ3G"
  # Paste your actual key here
    client = wolframalpha.Client(apikey)

    try:
        result = client.query(query)
        answer = next(result.results).text
        return answer
    except Exception as e:
        print("Error:", e)
        return "Sorry, I couldn't find the answer."
