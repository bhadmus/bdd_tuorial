from behave import *
from pages.page_objects import GuestShopper

driver = GuestShopper()

use_step_matcher("parse")

@given(u'I am on "{text}" website')
def step_impl(context, text):
    if text == "amazon":
        driver.setup()
    elif text == "konga":
        pass


@step(u'I inserted an item to search')
def step_impl(context):
    driver.search_and_click()


@step(u'I select an item from the result')
def step_impl(context):
    driver.select_item()


@step(u'I add the item to cart')
def step_impl(context):
    driver.add_to_cart()


@when(u'I proceed to checkout')
def step_impl(context):
    driver.proceed_to_checkout()


@then(u'I should be redirected to the Sign-in page')
def step_impl(context):
    driver.verify_page()