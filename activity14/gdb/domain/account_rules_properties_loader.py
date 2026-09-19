import os

class AccountRulesPropertiesLoader:
    """Utility loading external .properties files."""

    @staticmethod
    def load_rules(account_type: str) -> dict:
        filename = account_type.lower() + ".properties"

        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..",
            "resources",
            "config",
            "rules",
            filename
        )

        if not os.path.exists(file_path):
            return {}

        rules = {}

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                if "=" in line:
                    key, value = line.split("=", 1)
                    rules[key.strip()] = value.strip()

        return rules