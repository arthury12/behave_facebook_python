from behave import given, when, then, step
import urllib
import requests

use_step_matcher("parse")
hostname = "https://graph.facebook.com"

@given('I make a "{method}" request to "{path}"')
def step_make_request(context, method, path):
    context.uri = hostname + path
    context.method = method
    pass


@when(u'these parameters are supplied in URL')
def step_verify_parameters(context):

    context.uri += "?"
    for row in context.table:
        context.uri = context.uri + urllib.urlencode({ row[0]: row[1] })
        context.uri += "&"
    context.uri = context.uri[:-1]
    pass


@then('the api call should "{condition}"')
def step_verify_api_calls(context, condition):
    # Determine method and make HTTP Request
    # No python native switch statement, workaround is more tedious than chained if-else
    # Couldnt find binary input for steps in matcher "parse" for "{condition}"

    if context.method == "GET":
        print ("Request method: GET")
        print ("Request URI: ", context.uri)
        try:
            response = requests.get(context.uri)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            context.error = err

        print ("Response status: ", response.status_code)
        print ("Response body: ", response.content)
    elif context.method == "POST":
        print ("Request method: POST")
    elif context.method == "PUT":
        print ("Request method: PUT")
    elif context.method == "DELETE":
        print ("Request method: DELETE")
    else:
        raise ("Please use correct verb!!!")

    # Determine if succeed or fail
    if condition == 'succeed':
        assert hasattr(context, 'error') is False
        # Store access token
        context.responseContent = response.content
    elif condition == 'fail':
        assert hasattr(context, 'error') is True
    else:
        raise ("Please use succeed/fail as condition!")
    print("")
    pass

@step("value of access token is saved in a global variable")
def step_verify_access_token_stored_in_context(context):
    accessToken =  context.responseContent[len("access_token="):]
    print ("Access Token: ", accessToken)
    context.accessToken = accessToken
    pass
