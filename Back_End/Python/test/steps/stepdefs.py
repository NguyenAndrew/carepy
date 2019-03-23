''' Tutorial Step file'''
# pylint: disable-msg=E0611
# pylint: disable=unused-argument
# pylint: disable=function-redefined
from behave import given, when, then
from assertpy import assert_that

@given(u'an Flask application called app')
def step_impl(context):
    ''' Given '''
    from src.app import APP
    context.app = APP


@when(u'I call the health route on app')
def step_impl(context):
    ''' When '''
    client = context.app.test_client()
    context.response = client.get('/health')

@then(u'I should see Hello World!')
def step_impl(context):
    ''' When '''
    assert_that(context.response.data).is_equal_to(b'Hello World!')

@then(u'I should see a 200 status')
def step_impl(context):
    ''' Then '''
    assert_that(context.response.status_code).is_equal_to(200)
