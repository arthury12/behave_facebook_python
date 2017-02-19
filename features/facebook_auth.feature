Feature: getting app token

  Scenario: As facebook developer, I need to generate app token
    Given a "GET" request is made to "/oauth/access_token"
    When these parameters are supplied in URL
      |query         | param                            |
      |grant_type    | client_credentials               |
      |client_id     | 931957476934241                  |
      |client_secret | 68b3a63cfb0a6e961978ddd205e005f2 |
#    Then the api call should succeed
#    And value of access token is saved in a global variable