from flask import Flask , request,render_template,url_for,redirect
from statistics import mean 

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

res=""
@app.route("/results",methods=["POST"])
def test():
    science=int(request.form["Science"])
    Math=int(request.form["Math"])
    C=int(request.form["C"])
    datascience=int(request.form["DataScience"])
    sub=[science, Math,C,datascience]
    add=request.form.get('add',None)
    print(add)
    avg=request.form.get('avg',None)
    print(avg)
    
    if add:
        print(request.form['add'])
        result=science+Math+C+datascience
    elif avg:
        print(request.form['avg'])
        result=mean(sub)
    return redirect(url_for('Final_result',score=result))

res=""
@app.route('/outcome/<int:score>')
def Final_result(score):
    if score>=70:
        res=(f"You pass with First class distintion and your score is {score}")
    elif score>=60:
        res=(f"You pass with First class and your score is {score}")
    elif score>=30:
        res=(f"You pass with second class and your score is {score}")
    else:
        res=(f"You failed and your score is {score}")
    return render_template('score.html',result=res)
        
if __name__=='__main__':
    app.run(debug=True)