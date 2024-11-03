Feature: Update Product

  Scenario: Updating a product successfully
    Given a product with ID "123" exists
    When I update the product with the following details:
      | field      | value              |
      | name       | "New Product Name" |
      | price      | "19.99"            |
      | stock      | "50"               |
    Then the product should be updated successfully
    And I should see a confirmation message "Product updated successfully"
