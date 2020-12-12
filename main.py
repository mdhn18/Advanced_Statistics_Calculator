from flask import Flask, request
from fractions import Fraction
import statistics
# create app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Usage;\n<Operation>?X=<Value1, value2, value2, .... , valueN>\n'
        
@app.route('/max')
def maximum():
    if request.method == 'POST':
        inputs = request.values.get('X', default=0, type=str)
        values = inputs.split(',')
        
        try:
            values = [Fraction(x) for x in values]
        except ZeroDivisionError as e:
            print(ZeroDivisionError)
        except ValueError as e:
            print(ValueError)
        except:
            print(error)
            
        
    else:
        inputs = request.args.get('X', default=0, type=str)
        values = inputs.split(',')
        try:
            values = [Fraction(x) for x in values]
        except ZeroDivisionError as e:
            print(ZeroDivisionError)
        except ValueError as e:
            print(ValueError)
            
    return str(float(max(values)))+"\n"

# run app
if __name__ == '__main__':
    app.run()