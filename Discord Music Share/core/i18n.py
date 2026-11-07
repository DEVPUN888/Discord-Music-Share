import json
import os
from dotenv import load_dotenv

class I18n:
    def __init__(self, default_lang="th"):
        self.default_lang = default_lang
        self.current_lang = self._load_lang_from_env()
        self.translations = {}
        self._load_translations()

    def _load_lang_from_env(self):
        load_dotenv()
        return os.getenv("APP_LANGUAGE", self.default_lang)

    def _load_translations(self):
        # Load current language
        self._load_file(self.current_lang)
        # Load default language as fallback
        if self.current_lang != self.default_lang:
            self._load_file(self.default_lang)

    def _load_file(self, lang):
        file_path = f"locales/{lang}.json"
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.translations[lang] = data
            except Exception as e:
                print(f"Error loading language file {file_path}: {e}")

    def get(self, key, *args):
        # Try current language first
        lang_data = self.translations.get(self.current_lang, {})
        text = lang_data.get(key)

        # Fallback to default language
        if text is None:
            lang_data = self.translations.get(self.default_lang, {})
            text = lang_data.get(key, key)

        if args:
            return text.format(*args)
        return text

    def set_language(self, lang):
        self.current_lang = lang
        self._load_translations()

# Singleton instance
i18n = I18n()
