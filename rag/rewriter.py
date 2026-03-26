import os
import google.generativeai as genai

def rewrite_query(current_query, chat_history_str, api_key=None):
    """
    Given the recent conversational history and the newest query,
    this uses the LLM to rewrite vague sub-queries (e.g. "tell me more about it")
    into standalone declarative searches (e.g. "Tell me more about the python loop syntax").
    If the query is already standalone, it returns it normally.
    """
    key = api_key or os.getenv("GEMINI_API_KEY")
    if not key:
        return current_query  # Fail safely by just passing the query
        
    if not chat_history_str or chat_history_str == "No previous conversation.":
        return current_query
        
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = f"""
You are an intelligent search formulation AI bounding system. 
Your goal is to look at a conversational history and the latest user query, and rewrite the current query to be a completely standalone, declarative search statement.
This is necessary because the query will be passed to a semantic vector database that cannot read the chat history.
If the current user query has pronouns like "it", "they", "this", or vague instructions like "explain more", replace them with the explicit context from the history.
If the current user query is already explicitly standalone, output the exact same query without modifying it.
DO NOT ANSWER THE QUERY. ONLY OUTPUT THE REWRITTEN QUERY ITSELF.

Chat History:
{chat_history_str}

Current Query: {current_query}
Rewritten Standalone Query:
"""
    try:
        response = model.generate_content(prompt)
        # Strip any accidental newlines or surrounding quotes
        rewritten = response.text.strip().strip('"').strip("'")
        return rewritten
    except Exception as e:
        print(f"Query rewriter error: {e}")
        return current_query # fallback to original
