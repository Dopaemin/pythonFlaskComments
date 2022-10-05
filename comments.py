from flask import Flask , render_template, request, redirect



@app.route('/comments')
def comments():
    all_comments = ""

    try:
        f = open('comments.txt', 'r')
        all_comments = f.readlines()
        f.close()
    except:
        f = open('comments.txt', 'x')
        f.close()

    return render_template('comments.html', comments=all_comments)

@app.route('/comments', methods=['POST'])
def comments_post():
    f = open("comments.txt", 'a')
    f.writelines(request.form.get('txt') + "\n")
    f.close()
    return redirect('/comments')