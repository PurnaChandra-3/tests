from behave import then

@then('I should not see "{text}" on the page')
def step_impl(context, text):
    assert text not in context.browser.page_source, f'Expected text "{text}" was found in the page source'
