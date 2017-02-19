from behave import *
import urllib

use_step_matcher("parse")
hostname = "https://graph.facebook.com"

@given('a "{method}" request is made to "{path}"')
def step_make_request(context, method, path):
    context.uri = hostname + path
    context.callMethod = method
    pass


@when(u'these parameters are supplied in URL')
def step_verify_parameters(context):
    print (context.uri)
    context.uri += "?"
    for row in context.table:
        context.uri = context.uri + urllib.urlencode({ row[0]: row[1] })
        context.uri += "&"
    context.uri = context.uri[:-1]
    print (context.uri)
    pass


@step("the api call should succeed")
def step_verify_api_call_succeed(step):
    """
    :type step: lettuce.core.Step
    """
    pass



@step("value of access token is saved in a global variable")
def step_verify_access_token_stored_in_var(step):
    """
    :type step: lettuce.core.Step
    """
    pass
