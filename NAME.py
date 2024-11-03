from behave import then

@then('I should see "{text}" on the page')
def step_impl(context, text):
    assert text in context.browser.page_source, f'Expected text "{text}" not found in the page source'
