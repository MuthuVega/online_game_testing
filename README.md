# Test and report bugs in online game

This repo is a sample project to test and report bugs in an online game.

### Installation

Install the prerequisites using the below command:

`pip install -r requirements.txt`

### Notes

Create an environment variable named `GAME_URL` and store the game link to run the tests locally.
Or, create a .env file in the root directory and save the game link as `GAME_URL`.

This has been done to keep the game URL a secret.


### Running the tests

To run all the tests:

`pytest -v --disable-warnings`

To run individual tests based on the marker e.g. bug1

`pytest -v -m bug1 --disable-warnings`

