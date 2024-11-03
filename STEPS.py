from behave import then

@then('I should see the message "{message}"')
def step_impl(context, message):
    assert message in context.browser.page_source, f'Expected message "{message}" not found in the page source'
