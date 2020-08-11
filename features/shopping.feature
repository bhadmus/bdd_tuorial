Feature: Shopping

    As a shopper,
    I should be able to select and add item to cart
    So that I can checkout.

    Scenario: A Guest Shopper with no credentials on Amazon

        Given I am on "amazon" website
        And I inserted an item to search on "amazon"
        And I select an item from the "amazon" result page
        And I added the selected item to cart on "amazon"
        When I proceed to checkout on "amazon"
        Then I should be redirected to the Sign-in page on "amazon"

    Scenario: A Guest Shopper with no credentials on Aliexpress

        Given I am on "aliexpress" website
        And I inserted an item to search on "aliexpress"
        And I select an item from the "aliexpress" result page
        And I added the selected item to cart on "aliexpress"
        When I proceed to checkout on "aliexpress"
        Then I should be redirected to the Sign-in page on "aliexpress"