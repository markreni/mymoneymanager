import unittest
import sys
from mainWindow import *
from user import *
from fileManager import *


class Test(unittest.TestCase):

    def test_1(self):  # Test that file loads correctly with ok file
        self.reader = FileManager()
        self.user = User(self.reader)
        self.file = "/Users/markrenssi/!Mark Renssi/!School/!Aalto/KESKEN/Ohjelmoinnin peruskurssi Y2 (CS-A1121)/Projekti/y2_2022_74702/Code/test_files/test.csv"
        boolean, message = self.user.import_file(self.file)
        self.expenses = self.user.get_expenses()
        self.income = self.user.get_income()
        self.assertEqual(boolean, True, "Not correct")
        self.assertEqual(sum([values[0] for values in self.expenses.values()]), -1000, "Not correct")
        self.assertEqual(sum([values[0] for values in self.income.values()]), 800, "Not correct")

    def test_2(self):  # Test that file loads correctly with ok file with empty rows
        self.reader = FileManager()
        self.user = User(self.reader)
        self.file = "/Users/markrenssi/!Mark Renssi/!School/!Aalto/KESKEN/Ohjelmoinnin peruskurssi Y2 (CS-A1121)/Projekti/y2_2022_74702/Code/test_files/test2.csv"
        boolean, message = self.user.import_file(self.file)
        self.expenses = self.user.get_expenses()
        self.income = self.user.get_income()
        self.assertEqual(boolean, True, "Not correct")
        self.assertEqual(sum([values[0] for values in self.expenses.values()]), 0, "Not correct")
        self.assertEqual(sum([values[0] for values in self.income.values()]), 0, "Not correct")

    def test_3(self):  # Test that file loads correctly with faulty file
        self.reader = FileManager()
        self.user = User(self.reader)
        self.file = "/Users/markrenssi/!Mark Renssi/!School/!Aalto/KESKEN/Ohjelmoinnin peruskurssi Y2 (CS-A1121)/Projekti/y2_2022_74702/Code/test_files/test3.csv"
        boolean, message = self.user.import_file(self.file)
        self.expenses = self.user.get_expenses()
        self.income = self.user.get_income()
        self.assertEqual(boolean, True, "Not correct")
        self.assertEqual(sum([values[0] for values in self.expenses.values()]), 0, "Not correct")
        self.assertEqual(sum([values[0] for values in self.income.values()]), 0, "Not correct")

    def test_4(self):  # Test that file loads correctly with multiple files
        self.reader = FileManager()
        self.user = User(self.reader)
        self.file = "/Users/markrenssi/!Mark Renssi/!School/!Aalto/KESKEN/Ohjelmoinnin peruskurssi Y2 (CS-A1121)/Projekti/y2_2022_74702/Code/test_files/test.csv"
        boolean, message = self.user.import_file(self.file)
        self.file = "/Users/markrenssi/!Mark Renssi/!School/!Aalto/KESKEN/Ohjelmoinnin peruskurssi Y2 (CS-A1121)/Projekti/y2_2022_74702/Code/test_files/test4.csv"
        boolean, message = self.user.import_file(self.file)
        self.expenses = self.user.get_expenses()
        self.income = self.user.get_income()
        self.assertEqual(boolean, True, "Not correct")
        self.assertEqual(sum([values[0] for values in self.expenses.values()]), -3950, "Not correct")
        self.assertEqual(sum([values[0] for values in self.income.values()]), 2000, "Not correct")

    def test_5(self):  # Test that setting importance works properly
        self.reader = FileManager()
        self.user = User(self.reader)
        self.file = "/Users/markrenssi/!Mark Renssi/!School/!Aalto/KESKEN/Ohjelmoinnin peruskurssi Y2 (CS-A1121)/Projekti/y2_2022_74702/Code/test_files/test.csv"
        boolean, message = self.user.import_file(self.file)
        self.user.set_importance("Masku Helsinki Helsinki")
        self.expenses = self.user.get_expenses()
        self.assertEqual(self.expenses["Masku Helsinki Helsinki"][1], True, "Not correct")

    def test_6(self):  # Test that unsetting importance works properly
        self.reader = FileManager()
        self.user = User(self.reader)
        self.file = "/Users/markrenssi/!Mark Renssi/!School/!Aalto/KESKEN/Ohjelmoinnin peruskurssi Y2 (CS-A1121)/Projekti/y2_2022_74702/Code/test_files/test.csv"
        boolean, message = self.user.import_file(self.file)
        self.user.set_importance("Masku Helsinki Helsinki")
        self.user.unset_importance("Masku Helsinki Helsinki")
        self.expenses = self.user.get_expenses()
        self.assertEqual(self.expenses["Masku Helsinki Helsinki"][1], False, "Not correct")

    def test_7(self):  # Test that deleting a row works properly
        self.reader = FileManager()
        self.user = User(self.reader)
        self.file = "/Users/markrenssi/!Mark Renssi/!School/!Aalto/KESKEN/Ohjelmoinnin peruskurssi Y2 (CS-A1121)/Projekti/y2_2022_74702/Code/test_files/test.csv"
        boolean, message = self.user.import_file(self.file)
        self.user.delete_row(["Masku Helsinki Helsinki"])
        self.expenses = self.user.get_expenses()
        self.assertNotIn("Masku Helsinki Helsinki", self.expenses.keys(), "Not correct")
        self.assertIn("CLAS OHLSON 257 HELSINKI", self.expenses.keys(), "Not correct")

    def test_8(self):  # Test that grouping works properly
        self.reader = FileManager()
        self.user = User(self.reader)
        self.file = "/Users/markrenssi/!Mark Renssi/!School/!Aalto/KESKEN/Ohjelmoinnin peruskurssi Y2 (CS-A1121)/Projekti/y2_2022_74702/Code/test_files/test.csv"
        boolean, message = self.user.import_file(self.file)
        self.user.set_grouping(["Masku Helsinki Helsinki", "CLAS OHLSON 257 HELSINKI"], "Ryhmän nimi")
        self.expenses = self.user.get_expenses()
        self.assertNotIn("Masku Helsinki Helsinki", self.expenses.keys(), "Not correct")
        self.assertIn("Ryhmän nimi", self.expenses.keys(), "Not correct")
        self.assertEqual(self.expenses["Ryhmän nimi"][0], -840, "Not correct")

    def test_9(self):  # Test that savings algorithm works properly
        app = QApplication(sys.argv)
        self.reader = FileManager()
        self.user = User(self.reader)
        self.mainWind = MainWindow(self.user)
        self.file = "/Users/markrenssi/!Mark Renssi/!School/!Aalto/KESKEN/Ohjelmoinnin peruskurssi Y2 (CS-A1121)/Projekti/y2_2022_74702/Code/test_files/test.csv"
        boolean, message = self.user.import_file(self.file)
        self.user.set_importance("Masku Helsinki Helsinki")
        self.user.set_importance("Telia Finland Oyj")
        self.user.set_importance("CLAS OHLSON 257 HELSINKI")
        self.user.set_importance("CLAS OHLSON 228 HELSINKI")
        self.mainWind.savings_amount = 30
        self.mainWind.file_imported = True
        self.mainWind.savings_algorithm()
        self.savings_expenses = self.mainWind.savings_expenses
        self.assertEqual(self.savings_expenses["KING KEBAB FINL Helsinki"][0], -20, "Not correct")
        app.quit()

    def test_10(self):  # Test that savings algorithm works properly with wrong input
        app = QApplication(sys.argv)
        self.reader = FileManager()
        self.user = User(self.reader)
        self.mainWind = MainWindow(self.user)
        self.file = "/Users/markrenssi/!Mark Renssi/!School/!Aalto/KESKEN/Ohjelmoinnin peruskurssi Y2 (CS-A1121)/Projekti/y2_2022_74702/Code/test_files/test.csv"
        boolean, message = self.user.import_file(self.file)
        self.user.set_importance("Masku Helsinki Helsinki")
        self.user.set_importance("Telia Finland Oyj")
        self.user.set_importance("CLAS OHLSON 257 HELSINKI")
        self.user.set_importance("CLAS OHLSON 228 HELSINKI")
        self.mainWind.savings_amount = -30
        self.mainWind.file_imported = True
        self.mainWind.savings_algorithm()
        self.assertEqual(self.mainWind.warning_label.text(), "  Savings amount should be a positive number.", "Not correct")
        self.mainWind.savings_amount = "yes"
        self.mainWind.savings_algorithm()
        self.assertEqual(self.mainWind.warning_label.text(), "  Please type in savings amount as a numeric value.", "Not correct")
        app.quit()

    def test_11(self):  # Test that clearing window works properly
        app = QApplication(sys.argv)
        self.reader = FileManager()
        self.user = User(self.reader)
        self.mainWind = MainWindow(self.user)
        self.file = "/Users/markrenssi/!Mark Renssi/!School/!Aalto/KESKEN/Ohjelmoinnin peruskurssi Y2 (CS-A1121)/Projekti/y2_2022_74702/Code/test_files/test.csv"
        boolean, message = self.user.import_file(self.file)
        self.expenses = self.mainWind.expenses
        self.income = self.mainWind.income
        self.mainWind.clear_window()
        self.assertEqual(sum([values[0] for values in self.expenses.values()]), 0, "Not correct")
        self.assertEqual(sum([values[0] for values in self.income.values()]), 0, "Not correct")
        app.quit()

    def test_12(self):  # Test multiple operations simultaneously
        app = QApplication(sys.argv)
        self.reader = FileManager()
        self.user = User(self.reader)
        self.mainWind = MainWindow(self.user)
        self.file = "/Users/markrenssi/!Mark Renssi/!School/!Aalto/KESKEN/Ohjelmoinnin peruskurssi Y2 (CS-A1121)/Projekti/y2_2022_74702/Code/test_files/test4.csv"
        boolean, message = self.user.import_file(self.file)
        self.mainWind.file_imported = True
        message, success = self.mainWind.user.set_grouping(["Jumbo HELSINKI", "Stockmann HELSINKI"], "Clothes")
        self.expenses = self.mainWind.user.get_expenses()
        self.user.set_importance("Masku Helsinki Helsinki")
        self.user.set_importance("Telia Finland Oyj")
        self.user.set_importance("KING KEBAB FINL Helsinki")
        self.user.set_importance("CLAS OHLSON 257 HELSINKI")
        self.user.set_importance("CLAS OHLSON 228 HELSINKI")
        self.user.unset_importance("Clothes")
        self.mainWind.savings_amount = 1000
        self.mainWind.savings_algorithm()
        self.savings_expenses = self.mainWind.savings_expenses
        self.assertTrue(boolean)
        self.assertTrue(success)
        self.assertNotIn("Stockmann Helsinki", self.expenses.keys(), "Not correct")
        self.assertNotIn("Jumbo Helsinki", self.expenses.keys(), "Not correct")
        self.assertIn("Clothes", self.expenses.keys(), "Not correct")
        self.assertEqual(self.savings_expenses["Clothes"][0], -950, "Not correct")
        message, success = self.mainWind.user.set_grouping(["wrongname", "wrongname2"], "Title")
        self.assertFalse(success)
        message, success = self.mainWind.user.set_grouping(["Clothes"], "")
        self.assertEqual(message, "Set group title.", "Not correct")
        message, success = self.mainWind.user.set_grouping([], "Magazine")
        self.assertEqual(message, "No rows checked.", "Not correct")
        self.user.delete_row(["Clothes", "Telia Finland Oyj"])
        self.expenses = self.user.get_expenses()
        self.assertNotIn("Clothes", self.expenses.keys(), "Not correct")
        self.assertNotIn("Telia Finland Oyj", self.expenses.keys(), "Not correct")
        self.file = "/Users/markrenssi/!Mark Renssi/!School/!Aalto/KESKEN/Ohjelmoinnin peruskurssi Y2 (CS-A1121)/Projekti/y2_2022_74702/Code/test_files/test.csv"
        boolean, message = self.user.import_file(self.file)
        self.mainWind.file_imported = True
        message, success = self.mainWind.user.set_grouping(["CLAS OHLSON 257 HELSINKI", "CLAS OHLSON 228 HELSINKI", "Masku Helsinki Helsinki"], "Stores")
        self.expenses = self.mainWind.user.get_expenses()
        self.assertTrue(boolean)
        self.assertTrue(success)
        self.assertEqual(self.expenses["Stores"][0], -1860, "Not correct")
        self.mainWind.user.unset_importance("Stores")
        self.user.set_importance("Telia Finland Oyj")
        self.user.set_importance("KING KEBAB FINL Helsinki")
        self.mainWind.savings_amount = 1860
        self.mainWind.savings_algorithm()
        self.savings_expenses = self.mainWind.savings_expenses
        self.assertEqual(self.savings_expenses["Stores"][0], 0, "Not correct")
        app.quit()


