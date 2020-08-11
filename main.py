from flask import Flask, request, redirect, url_for
import statistics
# create app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # show html form
        return '''
            <form method="post">
                X: <input type="text" name="X" /
                <p><input type="submit" name="operator" value="maximum" />

            </form>
        '''
    elif request.method == 'POST':
# calculate result
        a = request.form.get('operator')
        if a == 'maximum':
            X = request.form.get('X')
            return redirect(url_for('maximum', X=X,))


@app.route('/maximum')
def maximum():
    dict = request.args.to_dict()
    X = eval(dict['X'])
    result = max(X)
    return 'result: %s' % result


# run app
if __name__ == '__main__':
    app.run(debug=True)