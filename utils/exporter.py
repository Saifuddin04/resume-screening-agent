"""
exporter.py

Exports ranked resume results to CSV and JSON.
"""

import json
import pandas as pd

from utils.logger import logger


def export_to_csv(results: list, output_path: str):
    """
    Export ranked results to CSV.
    """

    try:
        df = pd.DataFrame(results)
        df.to_csv(output_path, index=False)

        logger.info(f"CSV exported to {output_path}")

    except Exception as e:
        logger.error(f"CSV export failed: {e}")


def export_to_json(results: list, output_path: str):
    """
    Export ranked results to JSON.
    """

    try:
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(results, file, indent=4)

        logger.info(f"JSON exported to {output_path}")

    except Exception as e:
        logger.error(f"JSON export failed: {e}")