Feature: Search Products by Name

  Scenario: Searching a product based on its name
    Given the following products exist:
      | id  | name              | category         | price | stock |
      | 1   | "Garden Shovel"   | "Gardening"      | 15.99 | 30    |
      | 2   | "Tennis Racket"   | "Sports"         | 49.99 | 15    |
      | 3   | "Plant Fertilizer" | "Gardening"      | 9.99  | 100   |
    When I search for a product named "Tennis Racket"
    Then I should see the following product:
      | id  | name            | category | price | stock |
      | 2   | "Tennis Racket" | "Sports" | 49.99 | 15    |
