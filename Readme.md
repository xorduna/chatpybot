### ChatPyBot

A simple library to create markov chain based bots easly!

## Howto use

Each function is a step in the markov chain. Each function receives a parameter (which is the answer of the previous step from the user) and returns a response that the conversation engine will send back to the user.

There are 3 main decorators:

# @set_start

This defines which is the initial state of the conversation

# @answer(answer, next)

This decorator defines the next step if the user gives an answer. A decorator should be added for each answer.

# @step(next)

This decorator defines the default step the user will be redirected to in case it does not provide one of the given answers.

## Comments

The idea of predefined answers is to make the conversation to be oriented to an specific direction. Giving less option to the user and therefore incrementing the speed of interaction with the user.

It is possible to give always an open answer, but if different options are provided, the interaction will be faster.

For example, in case this is implemented using a telegram bot, it is possible to convert those answers into a keyboard.