import unittest, psycopg2, sys
sys.path.insert(0, '..')
from queries import *

class TestDowJonesIndustrials(unittest.TestCase):
    def test_average_industry_profit_margins(self):
        connection = psycopg2.connect(database="dow_jones.db", host="localhost")
        cursor = connection.cursor()
        cursor.execute(average_industry_profit_margins())
        raw = cursor.fetchall()

        result = [('Broadcasting and entertainment', 30.36), ('Conglomerate', 15.36), ('Consumer products', 23.01), ('Financial services', 35.74), ('Managed health care', 8.4), ('Manufacturing', 16.72), ('Oil & gas', 15.63), ('Pharmaceuticals', 35.1), ('Technology', 26.74), ('Telecommunication', 37.46)]

        test = []
        for el in raw:
            new = (el[0], round(el[1],2))
            test.append(new)
        self.assertEqual(test, result)


    def test_profit_margin_cte(self):
        connection = psycopg2.connect(database="dow_jones.db", host="localhost")
        cursor = connection.cursor()
        cursor.execute(profit_margin_cte())
        raw = cursor.fetchall()

        result = [('Visa', 68.44), ("McDonald's", 42.59), ('Pfizer', 40.4), ('Verizon', 37.46), ('Microsoft', 35.34), ('Johnson & Johnson', 33.16), ('Merck', 31.73), ('Apple', 30.87), ('Coca-Cola', 30.7), ('Walt Disney', 30.36), ('Cisco Systems', 30.08), ('Procter & Gamble', 27.14), ('American Express', 25.35), ('3M', 25.09), ('IBM', 21.0), ('DowDuPont', 18.6), ('Caterpillar', 18.59), ('Chevron', 17.15), ('United Technologies', 16.78), ('The Home Depot', 16.59), ('Intel', 16.41), ('Nike', 14.48), ('ExxonMobil', 14.1), ('Travelers', 13.44), ('Boeing', 12.98), ('UnitedHealth Group', 8.4), ('Walmart', 6.55), ('General Electric', 4.23)]

        test = []
        for el in raw:
            new = (el[0], round(el[1],2))
            test.append(new)
        self.assertEqual(test, result)


    def test_five_most_levered_capital_structures(self):
        connection = psycopg2.connect(database="dow_jones.db", host="localhost")
        cursor = connection.cursor()
        cursor.execute(five_most_levered_capital_structures())
        raw = cursor.fetchall()

        result = [('General Electric', 57.98), ('American Express', 38.88), ('Verizon', 38.73), ('Caterpillar', 29.45), ('IBM', 26.23)]

        test = []
        for el in raw:
            new = (el[0], round(el[1],2))
            test.append(new)
        self.assertEqual(test, result)


    def test_riskier_than_average_cos(self):
        connection = psycopg2.connect(database="dow_jones.db", host="localhost")
        cursor = connection.cursor()
        cursor.execute(riskier_than_average_cos())

        test = cursor.fetchall()
        result = [('GE',), ('MCD',), ('KO',), ('WMT',), ('PG',), ('V',), ('AXP',), ('TRV',), ('CAT',), ('DWDP',), ('CVX',), ('PFE',), ('MRK',), ('IBM',), ('CSCO',)]

        self.assertEqual(test, result)


    def test_tech_cos_with_above_average_roi(self):
        connection = psycopg2.connect(database="dow_jones.db", host="localhost")
        cursor = connection.cursor()
        cursor.execute(tech_cos_with_above_average_roi())
        raw = cursor.fetchall()

        result = [('Apple', 8.0, 6.95), ('Cisco Systems', 8.3, 6.95), ('IBM', 9.3, 6.95)]

        test = []
        for el in raw:
            new = (el[0], round(el[1],2), round(el[2],2))
            test.append(new)

        self.assertEqual(test, result)
