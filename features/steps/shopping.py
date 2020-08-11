from behave import *
from pages.page_objects import GuestShopper
from file import ref

driver = GuestShopper()

use_step_matcher("parse")

@given(u'I am on "{text}" website')
def step_impl(context, text):
    if text == "amazon":
        driver.setup(ref.amazon_url)
    elif text == "aliexpress":
        driver.setup(ref.aliexpress_url)
        # driver.close_banner(ref.aliexpress_banner)


@step(u'I inserted an item to search on "{text}"')
def step_impl(context, text):
    if text == "amazon":
        driver.search_and_click(ref.amazon_search_box, ref.amazon_search_item, ref.amazon_search_button)
    elif text == "aliexpress":
        driver.search_and_click(ref.aliexpress_search_box, ref.aliexpress_search_item, ref.aliexpress_search_button)


@step(u'I select an item from the "{text}" result page')
def step_impl(context, text):
    if text == "amazon":
        driver.select_item(ref.amazon_item)
    elif text == "aliexpress":
        driver.select_item(ref.aliexpress_item)


@step(u'I added the selected item to cart on "{text}"')
def step_impl(context, text):
    if text == "amazon":
        driver.buy_option(ref.amazon_buy_button)
        driver.add_to_cart(ref.amazon_add_button)
    elif text == "aliexpress":
        driver.pick_location(ref.aliexpress_location)
        driver.add_to_cart(ref.aliexpress_add_button)


@when(u'I proceed to checkout on "{text}"')
def step_impl(context, text):
    if text == "amazon":
        driver.proceed_to_checkout(ref.amazon_checkout_button)
    elif text == "aliexpress":
        driver.view_cart(ref.aliexpress_view_cart)
        driver.proceed_to_checkout(ref.aliexpress_checkout_button)


@then(u'I should be redirected to the Sign-in page on "{text}"')
def step_impl(context, text):
    if text == "amazon":
        driver.verify_page(ref.amazon_word)
    elif text == "aliexpress":
        driver.verify_page(ref.aliexpress_word)