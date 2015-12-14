__author__ = 'xorduna'


class Step:

    def __init__(self, name, response, next=None):
        self.name = name
        self.response = response
        self.next_step = next
        self.answers = {}

    def add_answer(self, answer, next_step):
        self.answers[answer] = next_step

    def has_answers(self):
        return len(self.answers.keys()) > 0

    # net step is to make this independent from arguments!
    def response(self, answer):
        return self.response(answer)

    #def next_step(self):
    #    return self.next_step

    def available_answers(self):
        return self.answers.keys()

class ChatBot:

    def __init__(self):
        self.steps = {}
        self.current = None
        self.start = None
        pass

    def add_step(self, name, response=None, next=None):
        self.steps[name] = Step(name=name, response=response, next=next)

    def add_answer(self, step, answer, next_step, response=None):
        # check if step exists, if not, create!
        if not self.steps.has_key(step):
            self.add_step(step, response)
        self.steps[step].add_answer(answer, next_step)

    def has_answers(self, step):
        return self.steps[step] is not {}

    def set_start_step(self, name):
        self.start = name

    def start_conversation(self):
        self.current = self.start
        return self.steps[self.current]

    def next_step(self, current, answer):

        if self.steps[current.name].has_answers() is not None:
            if answer in self.steps[current.name].answers:
                new_step = self.steps[current.name].answers[answer]
            elif self.steps[current.name].next_step is not None:
                new_step = self.steps[current.name].next_step
            else:
                new_step = current.name

        #open answer
        elif self.steps[current].next_step is not None:
            new_step = self.steps[current.name].next_step

        return self.steps[new_step]

    #decorator code!
    def default_next(self, next, callback=None):
        def decorator(callback):
            name = callback.__name__
            self.add_step(name, response=callback, next=next)
            return callback
        return decorator(callback) if callback else decorator

    def answer(self, answer, next, callback=None):
        def decorator(callback):
            name = callback.__name__
            self.add_answer(name, answer, next, response=callback)
            return callback
        return decorator(callback) if callback else decorator

    def set_start(self, callback):
        def decorator(callback):
            name = callback.__name__
            self.set_start_step(name)
            if name not in self.steps:
                self.add_step(name, response=callback)
            return callback
        return decorator(callback) if callback else decorator


