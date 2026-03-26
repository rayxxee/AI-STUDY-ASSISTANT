class ChatMemory:
    def __init__(self, limit=5):
        self.limit = limit
        self.history = []
        
    def add_message(self, role, content):
        """
        Appends a message to the history. Role should be 'user' or 'assistant'.
        Maintains the size to the latest `limit` Q&A pairs.
        """
        self.history.append({"role": role, "content": content})
        
        # A pair is 2 messages (user + assistant), so the max elements is limit * 2
        max_elements = self.limit * 2
        if len(self.history) > max_elements:
            # Pop from the left (oldest) to maintain window
            self.history = self.history[-max_elements:]
            
    def get_history(self, limit=None):
        """
        Returns the chat history. Limit implicitly handles pairs if provided.
        """
        if limit is None:
            limit = self.limit
            
        max_elements = limit * 2
        return self.history[-max_elements:]

    def format_history_string(self):
        """
        Returns the history nicely formatted for LLM prompts.
        """
        if not self.history:
            return "No previous conversation."
            
        formatted = ""
        for msg in self.history:
            role = "User" if msg["role"] == "user" else "Assistant"
            formatted += f"{role}: {msg['content']}\n"
        return formatted.strip()

# Global singleton store for MVP
memory_store = ChatMemory(limit=5)
