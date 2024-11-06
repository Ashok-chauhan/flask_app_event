from flask import render_template, url_for, redirect
from app.main import bp
from flask_login import login_required, current_user
from app.models.event import Events
# from app.models.comments import Comments
from app.main.commentform import CommentForm
from app.extensions import db
from app.auth import role_required


@bp.route('/')
@login_required
@role_required('user')
def index():
    events = Events.query.all()
    return render_template('main/index.html', events=events)

@bp.route('/event/<int:id>', methods=['GET', 'POST'])
@role_required('user')
def event(id):
     
     event = Events.query.get_or_404(id)
     # form = CommentForm()
     # if form.validate_on_submit():
     #      comment = Comments(content=form.content.data, events=event)
     #      db.session.add(comment)
     #      db.session.commit()
     #      return redirect(url_for('main.event', id=event.id))
          
     return render_template('main/event.html', event=event)



