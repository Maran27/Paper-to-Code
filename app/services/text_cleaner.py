# Remove extra spaces
# Remove multiple blank lines
# Strip leading/trailing whitespace
class TextCleaner():
    def __init__(self):
        pass

    def clean_text(self, text: str):
        """
        Cleans the given text by removing unnecessary whitespace and formatting.
        Args:
            text (str): The text to be cleaned.
        Returns:
            str: The cleaned text.
        """
        # Remove extra spaces
        cleaned_text = ' '.join(text.split())
        # Remove multiple blank lines
        cleaned_text = '\n'.join([line for line in cleaned_text.splitlines() if line.strip() != ''])
        # Strip leading/trailing whitespace
        cleaned_text = cleaned_text.strip()
        return cleaned_text