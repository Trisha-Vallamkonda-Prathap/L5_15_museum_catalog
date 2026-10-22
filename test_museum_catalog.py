"""Unit tests for museum_catalog module."""

import io
import unittest
from unittest.mock import patch

import museum_catalog


class TestMuseumCatalog(unittest.TestCase):
    """Test suite covering museum catalog functionality and edge cases."""

    def test_parameterized_insert_special_characters(self):
        """Verify inserting titles with single quotes succeeds safely."""
        title = "Queen's Royal Scepter"
        era = "Chola"
        value = 50000
        museum_catalog.add_artifact(title, era, value, on_display=0)
        cursor = museum_catalog.conn.execute(
            "SELECT era, value, on_display FROM artifacts WHERE title = ?",
            (title,),
        )
        row = cursor.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row, (era, value, 0))

    def test_display_status_storage_and_display(self):
        """Verify display_status returns correct string for storage/display."""
        museum_catalog.add_artifact("Storage Relic", "Maurya", 30000, 0)
        cursor = museum_catalog.conn.execute(
            "SELECT id FROM artifacts WHERE title = 'Storage Relic'"
        )
        storage_id = cursor.fetchone()[0]
        self.assertEqual(
            museum_catalog.display_status(storage_id), "in storage"
        )

        museum_catalog.move_to_display(storage_id)
        self.assertEqual(
            museum_catalog.display_status(storage_id), "on display"
        )

    def test_display_status_missing_id(self):
        """Verify display_status handles non-existent IDs gracefully."""
        self.assertEqual(museum_catalog.display_status(99999), "unknown")

    def test_total_value_calculation(self):
        """Verify total_value sums values accurately for a given era."""
        initial_chola = museum_catalog.total_value("Chola")
        museum_catalog.add_artifact("Gold Coin", "Chola", 25000, 0)
        updated_chola = museum_catalog.total_value("Chola")
        self.assertEqual(updated_chola, initial_chola + 25000)

    def test_backup_note_output(self):
        """Verify backup_note prints the expected completion message."""
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            museum_catalog.backup_note()
            self.assertEqual(
                fake_out.getvalue().strip(), "catalog backup complete"
            )

    def test_main_execution(self):
        """Verify main workflow executes successfully."""
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            museum_catalog.main()
            output = fake_out.getvalue().splitlines()
            self.assertIn("catalog backup complete", output)
            self.assertIn("on display", output)


if __name__ == "__main__":
    unittest.main()
