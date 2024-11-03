Feature: Search Products by Availability

  Scenario: Searching a product based on availability
    Given the following products exist:
      | id  | name              | availability | price | stock |
      | 1   | "Garden Shovel"   | "in stock"   | 15.99 | 30    |
      | 2   | "Tennis Racket"   | "out of stock" | 49.99 | 0     |
      | 3   | "Plant Fertilizer" | "in stock"   | 9.99  | 100   |
    When I search for products that are "in stock"
    Then I should see the following products:
      | id  | name              | availability | price | stock |
      | 1   | "Garden Shovel"   | "in stock"   | 15.99 | 30    |
      | 3   | "Plant Fertilizer" | "in stock"   | 9.99  | 100   |
