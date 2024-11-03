from behave import given, when, then

@when('I click the button with the text "{button_text}"')
def step_impl(context, button_text):
    button = context.browser.find_element_by_link_text(button_text)
    button.click()
