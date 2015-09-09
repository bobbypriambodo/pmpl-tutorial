from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def test_can_see_profile_page(self):
    # User visits our site
    self.browser.get('http://localhost:8000')

    # User notices the page title and header mention Bobby Priambodo
    self.assertIn('Bobby Priambodo', self.browser.title)

    # Page shows correct header
    header_text = self.browser.find_element_by_tag_name('h1').text;
    self.assertIn('Bobby Priambodo', header_text);

    # Page shows real name and student ID
    desc_text = self.browser.find_element_by_tag_name('p').text;
    self.assertIn('Widyanto Bagus Priambodo', desc_text);
    self.assertIn('1206208315', desc_text);

    ## To-do tests
    # User is invited to enter a to-do item straight away
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(
      inputbox.get_attribute('placeholder'),
      'Enter a to-do item'
    )

    # She types "Buy peacock feathers" into a text box (the user's hobby
    # is trying fly-fishing lures)
    inputbox.send_keys('buy peacock feathers')

    # When she hits enter, the page updates, and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list table
    inputbox.send_keys(Keys.ENTER)

    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertTrue(
      any(row.text == '1: Buy peacock feathers' for row in rows)
    )

    # There is still a text box inviting her to add another item. She
    # enters "Use peacock feathers to make a fly" (Edith is very
    # methodical)
    self.fail('Finish the test!')

if __name__ == '__main__':
  unittest.main(warnings='ignore')
