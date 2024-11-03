Feature: Search Products by Category

  Scenario: Searching a product based on category
    Given the following products exist:
      | id  | name              | category         | price | stock |
      | 1   | "Garden Shovel"   | "Gardening"      | 15.99 | 30    |
      | 2   | "Tennis Racket"   | "Sports"         | 49.99 | 15    |
      | 3   | "Plant Fertilizer" | "Gardening"      | 9.99  | 100   |
    When I search for products in the "Gardening" category
    Then I should see the following products:
      | id  | name              | category         | price | stock |
      | 1   | "Garden Shovel"   | "Gardening"      | 15.99 | 30    |
      | 3   | "Plant Fertilizer" | "Gardening"      | 9.99  | 100   |
