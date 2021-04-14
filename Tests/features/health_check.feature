@health_check

Feature: Get the api and validate result

  Scenario: Get the api and validate result
     Given the API is ready
     When send a get request to tandem api "https://jsonplaceholder.typicode.com/posts/1/comments"
     Then we will received a "200" response code

