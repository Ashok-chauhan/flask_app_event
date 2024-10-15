from flask import render_template, url_for, redirect, request
from app.posts import bp
from app.extensions import db
from app.models.post import Post, Comment
from app.posts.postform import PostForm


@bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts = posts)


@bp.route('/create', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, content=form.content.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('posts.index'))

    return render_template('posts/create.html', form=form)
    
    
@bp.route('/<int:post_id>/', methods=('GET', 'POST'))
def post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        comment = Comment(content=request.form['content'], post=post)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('posts.post', post_id=post.id))
    
    return render_template('posts/post.html', post= post)
