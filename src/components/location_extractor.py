import os
import re
import sys

from src.logger.logger import logger
from src.exception.exception import CustomException


class LocationExtractor:

    def __init__(self, dictionary_path: str):
        self.dictionary_path = dictionary_path
        self.locations = self._load_dictionary()


    def _load_dictionary(self):

        try:

            if not os.path.exists(self.dictionary_path):
                raise FileNotFoundError(
                    f"Location dictionary not found: {self.dictionary_path}"
                )

            locations = {}

            with open(
                self.dictionary_path,
                "r",
                encoding="utf-8",
            ) as file:

                for line in file:

                    line = line.strip()

                    if not line:
                        continue

                    if "=" in line:

                        english, hindi = line.split("=", 1)

                        locations[
                            english.lower().strip()
                        ] = hindi.strip()


            logger.info(
                f"{len(locations)} location mappings loaded successfully."
            )

            return locations


        except Exception as e:
            logger.error(CustomException(e, sys))
            raise CustomException(e, sys)



    def extract_location(self, sender_text: str) -> str:

        try:

            sender = str(sender_text).lower()

            sender = re.sub(
                r"[,./()\-]",
                " ",
                sender
            )

            sender = re.sub(
                r"\s+",
                " ",
                sender
            ).strip()


            matched_locations = []


            for location in self.locations.keys():

                pattern = r"\b" + re.escape(location) + r"\b"

                if re.search(pattern, sender):

                    matched_locations.append(location)



            if matched_locations:

                return self._normalize_locations(
                    matched_locations
                )


            return "unknown"



        except Exception as e:
            logger.error(CustomException(e, sys))
            raise CustomException(e, sys)




    def _normalize_locations(self, matched_locations):

        unique_locations = []


        for location in matched_locations:

            if location not in unique_locations:

                unique_locations.append(location)



        hindi_locations = [

            self.locations[location]

            for location in unique_locations

        ]


        return " ".join(hindi_locations)