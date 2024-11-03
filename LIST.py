Feature: List Products

  Scenario: Listing all products
    Given the following products exist:
      | id  | name              | price | stock |
      | 1   | "Product One"     | 29.99 | 100   |
      | 2   | "Product Two"     | 39.99 | 50    |
      | 3   | "Product Three"   | 19.99 | 200   |
    When I request to list all products
    Then I should see the following products:
      | id  | name              | price | stock |
      | 1   | "Product One"     | 29.99 | 100   |
      | 2   | "Product Two"     | 39.99 | 50    |
      | 3   | "Product Three"   | 19.99 | 200   |
