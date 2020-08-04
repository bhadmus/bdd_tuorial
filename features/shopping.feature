Feature: Shopping

    As a shopper,
    I should be able to select and add item to cart
    So that I can checkout.

    Scenario: A Guest Shopper with no credentials on Amazon

        Given I am on "amazon" website
        And I inserted an item to search
        And I select an item from the result
        And I add the item to cart
        When I proceed to checkout
        Then I should be redirected to the Sign-in page