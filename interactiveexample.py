from chatpybot import ChatBot


__author__ = 'xorduna'


cb = ChatBot()

@cb.answer(answer='A Barcelona', next='barcelona')
@cb.answer(answer='A Madrid', next='madrid')
@cb.step(next='altra_ciutat')
@cb.set_start
def inici(answer):
    return 'On Vols viatjar?'


@cb.answer(answer='Jove', next='bcn_jove')
@cb.answer(answer='Adult', next='bcn_adult')
@cb.step(next='edat')
def barcelona(answer):

    return 'Quina edat tens?'

@cb.step(next='inici')
def altra_ciutat(answer):
    return 'Quina bona idea anar a ' + unicode(answer)

@cb.step(next='inici')
def edat(answer):
    return 'Sembles jove per tenir ' + unicode(answer)

@cb.step(next='inici')
def bcn_jove(answer):
    return 'Pots anar a Razzmataz'


@cb.step(next='inici')
def bcn_adult(answer):
    return 'Pots anar a la sagrada familia'


@cb.step(next='inici')
def madrid(answer):
    return 'No tinc idees per Madrid!'


step = cb.start_conversation()

a = ''


while True:
    response = step.response(a)

    print response
    print 'Possible Answers:'
    if step.has_answers():
        for answer in step.available_answers():
            print answer


    a = raw_input('Your Answer: ')

    step = cb.next_step(step, a)

