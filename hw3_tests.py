import unittest
from demographics_functions import CountyDemographics, below_poverty_level_greater_than, below_poverty_level_less_than, education_greater_than, education_less_than, ethnicity_greater_than, ethnicity_less_than, population_by_education, population_by_ethnicity, population_total

class TestCountyDemographics(unittest.TestCase):

    def setUp(self):
        self.county_data = [
            CountyDemographics(
                county="Autauga County",
                age={},
                population={'2014 Population': 50000},
                education={"Bachelor's Degree or Higher": 25},
                ethnicities={'White Alone': 70, 'Black Alone': 20},
                income={'Persons Below Poverty Level': 12},
                state="AL"
            ),
            CountyDemographics(
                county="Baldwin County",
                age={},
                population={'2014 Population': 150000},
                education={"Bachelor's Degree or Higher": 35},
                ethnicities={'White Alone': 85, 'Black Alone': 10},
                income={'Persons Below Poverty Level': 18},
                state="AL"
            )
        ]

    def test_below_poverty_level_greater_than(self):
        threshold = 15
        filtered_data = below_poverty_level_greater_than(self.county_data, threshold)
        self.assertEqual(filtered_data[0].county, 'Baldwin County')

    def test_below_poverty_level_less_than(self):
        threshold = 15
        filtered_data = below_poverty_level_less_than(self.county_data, threshold)
        self.assertEqual(filtered_data[0].county, 'Autauga County')

    def test_education_greater_than(self):
        threshold = 20
        filtered_data = education_greater_than(self.county_data, threshold)
        # Since both counties meet the condition, this should test if both are returned
        self.assertIn('Autauga County', [entry.county for entry in filtered_data])
        self.assertIn('Baldwin County', [entry.county for entry in filtered_data])

    def test_education_less_than(self):
        threshold = 30
        filtered_data = education_less_than(self.county_data, threshold)
        self.assertEqual(filtered_data[0].county, 'Autauga County')

    def test_ethnicity_greater_than(self):
        ethnicity = 'White Alone'
        threshold = 75
        filtered_data = ethnicity_greater_than(self.county_data, ethnicity, threshold)
        self.assertEqual(filtered_data[0].county, 'Baldwin County')

    def test_ethnicity_less_than(self):
        ethnicity = 'Black Alone'
        threshold = 20
        filtered_data = ethnicity_less_than(self.county_data, ethnicity, threshold)
        # Baldwin County has less than 20% Black Alone, so it should be included
        self.assertIn('Baldwin County', [entry.county for entry in filtered_data])
        # Autauga County has exactly 20%, so it should not be included
        self.assertNotIn('Autauga County', [entry.county for entry in filtered_data])

    def test_population_by_education(self):
        total_education = population_by_education(self.county_data)
        self.assertGreater(total_education, 0)  # Check if result is positive

    def test_population_by_ethnicity(self):
        ethnicity = 'White Alone'
        total_ethnicity_population = population_by_ethnicity(self.county_data, ethnicity)
        self.assertGreater(total_ethnicity_population, 0)  # Check if result is positive

    def test_population_total(self):
        total_population = population_total(self.county_data)
        self.assertGreater(total_population, 0)  # Check if result is positive

if __name__ == '__main__':
    unittest.main()
