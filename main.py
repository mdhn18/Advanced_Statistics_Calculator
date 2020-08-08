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
                <p><input type="submit" name="operator" value="mini" />
                
            </form>
        '''
    elif request.method == 'POST':
# calculate result
        a = request.form.get('operator')
        if a == 'mini':
            X = request.form.get('X')
            return redirect(url_for('mini', X=X,))


@app.route('/mini')
def mini():
    dict = request.args.to_dict()
    X = eval(dict['X'])
    result = min(X)
    return 'result: %s' % result

# run app
if __name__ == '__main__':
    app.run(debug=True)