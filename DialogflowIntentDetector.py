def detect_intent_texts(project_id, session_id, texts, language_code):
    from google.cloud import dialogflow
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/reflect9/mysite/firstbot-nbnd-0ecb8e859ec7.json"

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    responses = []
    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
        responses.append({
            "query":response.query_result.query_text,
            "intent":response.query_result.intent.display_name,
            "confidence": response.query_result.intent_detection_confidence,
            "answer":  response.query_result.fulfillment_text
        })
    return responses










