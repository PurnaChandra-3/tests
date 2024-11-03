Feature: Product Management

  Scenario: Reading a product
    Given the following products exist:
      | name      | category  | available |
      | Product A | Category 1| true      |
      | Product B | Category 2| false     |
    When I request the product with name "Product A"
    Then I should receive a response with status code 200
    And the response should contain the product details:
      | name      | category  | available |
      | Product A | Category 1| true      |
