from flask import render_template, redirect, url_for, current_app, request, send_from_directory, jsonify, send_file
from werkzeug.utils import secure_filename
from flask_login import current_user
# from wergzeug.exceptions import RequestEntityTooLarge
import os
from app.admin.eventform import EventForm
from app.admin.commentform import CommentForm
from app.admin.menuform import MenuForm
from app.admin.facultyform import FacultyForm
from app.admin import bp
from app.models.event import Events
from app.models.comments import Comments
from app.models.menu import Menu, Faculty
from app.models.user import Users

from app.extensions import db
from app.auth import role_required
from app.admin.uploadform import UploadForm



def upload_file(file):
    try:
        extension = os.path.splitext(file.filename)[1].lower()
        if file:
                if extension not in current_app.config['ALLOWED_EXTENTIONS']:
                    return 'File is not allowed.'
                file.save(os.path.join(current_app.config['UPLOAD_DIRECTORY'], secure_filename(file.filename)))
               #  file.save(os.path.join(current_app.config['UPLOAD_DIRECTORY'], file.filename))

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
     user_id = current_user.get_id()
     user = Users.query.get(user_id)
     full_name = user.f_name + ' '+user.l_name

     if form.validate_on_submit():
          comment = Comments(content=form.content.data, user_name=full_name, events=event)
          db.session.add(comment)
          db.session.commit()
          return redirect(url_for('admin.event', id=event.id))
          
     return render_template('admin/event.html', event=event, form=form)

@bp.route('/modrate_comment/<int:id>', methods=['GET'])
def modrate_comment(id):
     comment = Comments.query.get_or_404(id)
     if comment:
          comment.status = 1
          db.session.add(comment)
          db.session.commit()
          return redirect(url_for('admin.event', id=comment.events_id))
     

@bp.route('/delete_comment/<int:id>', methods=['GET'])
def delete_comment(id):
     comment = Comments.query.get_or_404(id)
     db.session.delete(comment)
     db.session.commit()
     return redirect(url_for('admin.event', id=comment.events_id))


@bp.route('/menu', methods=['GET', 'POST'])
@role_required('admin')
def menu():
     menus = Menu.query.all()
     form = MenuForm()
     if form.validate_on_submit():
          newMenu = Menu(title=form.title.data)
          db.session.add(newMenu)
          db.session.commit()
          return redirect(url_for('admin.menu'))

     return render_template('admin/menu.html', menus=menus, form=form)

@bp.route('/editmenu/<int:id>', methods=['GET', 'POST'])
def editmenu(id):
     menu = Menu.query.get_or_404(id)
     form = MenuForm()
     if form.validate_on_submit():
          menu.title = form.title.data
          db.session.add(menu)
          db.session.commit()
          return redirect(url_for('admin.menu'))
     form.title.data = menu.title
     return render_template('admin/edit_menu.html', form=form)

@bp.route('/delete_menu/<int:id>', methods=['GET', 'POST'])
def delete_menu(id):
     menu = db.get_or_404(Menu, id)
     db.session.delete(menu)
     db.session.commit()
     return redirect(url_for('admin.menu'))


     




@bp.route('/faculty', methods=['GET', 'POST'])
@role_required('admin')
def faculty():
     form = FacultyForm()
     optionList =[]
     faculty_list = []
     options = Menu.query.all()
     for option in options:
          op = option.id, option.title,
          optionList.append(op)

     form.menu.choices = optionList
     if form.validate_on_submit():
          picture = upload_file(form.picture.data)
          new_faculty = Faculty(title=form.title.data, content=form.content.data, picture=picture, menu_id=form.menu.data, faculty_type=form.faculty_type.data)
          db.session.add(new_faculty)
          db.session.commit()
          return redirect(url_for('admin.faculty'))
     return render_template('admin/faculty.html', form=form)

@bp.route('/faculties', methods=['GET'])
def faculties():
     faculties = Faculty.query.all()
     return render_template('admin/faculties.html', faculties=faculties)




@bp.route('/upload', methods=['POST'])
def upload():
     # form = UploadForm()
     # if form.validate_on_submit():
       
     #    speaker_file = upload_file(form.speaker_file.data)
     #    return redirect(url_for('admin.index'))
     # return render_template('admin/upload.html', form=form)
     if 'file' not in request.files:
        return 'No file part'
     file = request.files['file']
     if file.filename == '':
        return 'No selected file'
     if file and file.filename:
        filename = file.filename
        file.save(os.path.join(current_app.config['UPLOAD_DIRECTORY'], filename))
        return redirect(url_for('admin.uploaded_file', filename=filename))
       
     return 'File not allowed'
     

@bp.route('/uploadfile', methods=['GET'])
def uploadfile():
    return render_template('admin/upload.html')



@bp.route('/uploads/<filename>')
def uploaded_file(filename):
    
    return f"File {filename} uploaded successfully."



@bp.route('/download/<filename>', methods=['GET'])
def download(filename):
     # return 'got ittt' + filename
     # filename = 'me.jpg'
     file_path = os.path.join(current_app.config['UPLOAD_DIRECTORY'], filename)
     # return send_file(file_path, as_attachment=False)
     return send_from_directory(current_app.config['UPLOAD_DIRECTORY'], filename, as_attachment=False)

     # file_path = os.path.join(current_app.config['UPLOAD_DIRECTORY'], filename)
     # if os.path.exists(file_path):
     #      # If file exists, serve the file
     #      return send_from_directory(current_app.config['UPLOAD_DIRECTORY'], filename, as_attachment=True)
     # else:
     #      # Log the error for debugging
     #      print(f"File not found: {file_path}")
     #      return jsonify({"error": "File not found"}), 404
          