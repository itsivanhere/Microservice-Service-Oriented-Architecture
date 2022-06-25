from flask import Flask
from flask_celery import make_celery

application = Flask(__name__)
application.config['CELERY_BROKER_URL']= 'redis://127.0.0.1'
application.config['CELERY_RESULT_BACKEND'] = 'redis://127.0.0.1'

celery = make_celery(application)

# @application.route('/process/<name>')
# def process(name):
#     # reverse.delay(name)
#     # return 'I sent an async request!'
#     return name

@application.route('/api/prime/<index>', methods=['GET'])
def get_prime(self,index):
    # factor = 0
    # for i in range(1, num + 1):
    #     if num % i == 0:
    #         factor += 1
        
    # return factor == 2
    primes = []

    for i in range(2, 999999):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
            else:
                primes.append(i)

    output={
        'result':primes[index] 
    }
    return output

@application.route('/api/prime/palindrome/<index>', methods=['GET'])
def get_primePal(self,index):
    prime_palindrome=[]

    for i in range(0,99999):
        if(str(i) == str(i)[::-1]):
            if(i>1):
                for a in range(2,i):
                    if(i%a==0):
                        y = False
                        break
            else:
                prime_palindrome.append(i)

    output={
        'result':prime_palindrome[index] 
    }
    return output

@celery.task(name="celery_example.reverse")
def reverse(string):
    return string[::1]

if __name__ == '__main__':
    application.run(debug=True)