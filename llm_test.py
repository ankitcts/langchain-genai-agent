from model import llama_response, granite_response, mistral_response

def call_all_models(system_prompt, user_prompt):
    llama_result = llama_response(system_prompt, user_prompt)
    granite_result = granite_response(system_prompt, user_prompt)
    mistral_result = mistral_response(system_prompt, user_prompt)
    print("Llama Response:")
    print("  Summary  :", llama_result["summary"])
    print("  Sentiment:", llama_result["sentiment"])
    print("  Response :", llama_result["response"])

    print("\nGranite Response:")
    print("  Summary  :", granite_result["summary"])
    print("  Sentiment:", granite_result["sentiment"])
    print("  Response :", granite_result["response"])

    print("\nMistral Response:")
    print("  Summary  :", mistral_result["summary"])
    print("  Sentiment:", mistral_result["sentiment"])
    print("  Response :", mistral_result["response"])
# Example call to test all models
call_all_models("You are a helpful assistant who provides concise and accurate answers", "What is the capital of Canada? Tell me a cool fact about it as well")
