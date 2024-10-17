from flask import render_template, redirect, url_for, current_app, request, send_from_directory
from werkzeug.utils import secure_filename
# from wergzeug.exceptions import RequestEntityTooLarge
import os
from app.admin.eventform import EventForm
from app.admin.commentform import CommentForm
from app.admin import bp
from app.models.event import Events
from app.models.comments import Comments
from app.extensions import db
from app.auth import role_required


def upload_file(file):
    try:
        extension = os.path.splitext(file.filename)[1].lower()
        if file:
                if extension not in current_app.config['ALLOWED_EXTENTIONS']:
                    return 'File is not allowed.'
                file.save(os.path.join(current_app.config['UPLOAD_DIRECTORY'], secure_filename(file.filename)))
                return secure_filename(file.filename)
    except:
            return 'File is larger than 16 MB'
     
@bp.route('/')
def index():
    events = Events.query.all() 
    return render_template('admin/index.html', events=events)



@bp.route('/events', methods=['GET', 'POST'])
@role_required('admin')
def create_event():
    form = EventForm()
    
    if form.validate_on_submit():
       
        speaker_file = upload_file(form.speaker_file.data)
        keynote_file = upload_file(form.keynote_file.data)
        comments_file = upload_file(form.comments_file.data)
        
        event = Events(date=form.date.data, title=form.title.data, speaker=form.speaker.data, speaker_start=form.speaker_start.data, speaker_end=form.speaker_end.data, speaker_file=speaker_file,  keynote=form.keynote.data, keynote_start=form.keynote_start.data, keynote_end=form.keynote_end.data, keynote_file=keynote_file,  comments=form.comments.data, comments_start=form.comments_start.data, comments_end=form.comments_end.data, comments_file=comments_file,  breaks=form.breaks.data, breaks_start=form.breaks_start.data, breaks_end=form.breaks_end.data)
        db.session.add(event)
        db.session.commit()
        return redirect(url_for('admin.index'))

    return render_template('admin/create_event.html', form=form)




@bp.route('/event/<int:id>', methods=['GET', 'POST'])
@role_required('admin')
def event(id):
     
     event = Events.query.get_or_404(id)
     form = CommentForm()
     if form.validate_on_submit():
          comment = Comments(content=form.content.data, events=event)
          db.session.add(comment)
          db.session.commit()
          return redirect(url_for('admin.event', id=event.id))
          
     return render_template('admin/event.html', event=event, form=form)


