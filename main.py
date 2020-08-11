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
                <p><input type="submit" name="operator" value="mean" />
                <input type="submit" name="operator" value="median" />
                <input type="submit" name="operator" value="maximum" />
                <input type="submit" name="operator" value="minimum" />
            </form>
        '''
    elif request.method == 'POST':
# calculate result
        a = request.form.get('operator')
        if a == 'mean':
            X = request.form.get('X')
            return redirect(url_for('mean', X=X,))
            
        if a == 'median':
            X = request.form.get('X')
            return redirect(url_for('median', X=X,))

        if a == 'maximum':
            X = request.form.get('X')
            return redirect(url_for('maximum', X=X,))

        if a == 'minimum':
            X = request.form.get('X')
            return redirect(url_for('minimum', X=X,))

@app.route('/mean')
def mean():
    dict = request.args.to_dict()
    X = eval(dict['X'])
    result = statistics.mean(X)
    return 'result: %s' % result

@app.route('/median')
def median():
    dict = request.args.to_dict()
    X = eval(dict['X'])
    result = statistics.median(X)
    return 'result: %s' % result

@app.route('/maximum')
def maximum():
    dict = request.args.to_dict()
    X = eval(dict['X'])
    result = max(X)
    return 'result: %s' % result

@app.route('/minimum')
def minimum():
    dict = request.args.to_dict()
    X = eval(dict['X'])
    result = min(X)
    return 'result: %s' % result

# run app
if __name__ == '__main__':
    app.run(debug=True)