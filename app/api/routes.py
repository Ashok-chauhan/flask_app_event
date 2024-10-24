from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from flask_login import login_user
from app.api import bp
from app.extensions import db
from app.models.event import Events
from app.models.comments import Comments
from app.models.user import Users



@bp.route('/events')
def index():
    events = Events.query.all()
    return_value=[]
    
    for event in events:
        event_dict = {}
       
        event_dict['id'] = event.id
        event_dict['date'] = event.date
        event_dict['session_name'] = event.title
        event_dict['speaker'] = event.speaker
        event_dict['speaker_start'] = event.speaker_start
        event_dict['speaker_end'] = event.speaker_end
        event_dict['speaker_file'] = str(request.url_root) +'static/images/'+ str(event.speaker_file) if event.speaker_file else None #event.speaker_file

        event_dict['keynote'] = event.keynote
        event_dict['keynote_start'] = event.keynote_start
        event_dict['keynote_end'] = event.keynote_end
        event_dict['keynote_file'] = str(request.url_root) +'static/images/'+ str(event.keynote_file) if event.keynote_file else None

        event_dict['comments'] = event.comments
        event_dict['comments_start'] = event.comments_start
        event_dict['comments_end'] = event.comments_end
        event_dict['comments_file'] = str(request.url_root) +'static/images/'+ str(event.comments_file) if event.comments_file else None

        event_dict['breaks'] = event.breaks
        event_dict['breaks_start'] = event.breaks_start
        event_dict['breaks_end'] = event.breaks_end
       
        comment_value=[]
        for comment in event.comment:
            comment_dict = {}
            comment_dict['id'] = comment.id
            comment_dict['content'] = comment.content
            comment_value.append(comment_dict)
            event_dict['comments'] = comment_value
      
        return_value.append(event_dict)

    return jsonify({'events': return_value})
    


@bp.route('/events_by_date/<string:event_date>', methods=['GET'])
def events_by_date(event_date):
    events = Events.query.filter_by(date=event_date)
    return_value=[]
    
    for event in events:
        event_dict = {}
       
        event_dict['id'] = event.id
        event_dict['date'] = event.date
        event_dict['session_name'] = event.title
        event_dict['speaker'] = event.speaker
        event_dict['speaker_start'] = event.speaker_start
        event_dict['speaker_end'] = event.speaker_end
        event_dict['speaker_file'] = str(request.url_root) +'static/images/'+ str(event.speaker_file) if event.speaker_file else None #event.speaker_file

        event_dict['keynote'] = event.keynote
        event_dict['keynote_start'] = event.keynote_start
        event_dict['keynote_end'] = event.keynote_end
        event_dict['keynote_file'] = str(request.url_root) +'static/images/'+ str(event.keynote_file) if event.keynote_file else None

        event_dict['comments'] = event.comments
        event_dict['comments_start'] = event.comments_start
        event_dict['comments_end'] = event.comments_end
        event_dict['comments_file'] = str(request.url_root) +'static/images/'+ str(event.comments_file) if event.comments_file else None

        event_dict['breaks'] = event.breaks
        event_dict['breaks_start'] = event.breaks_start
        event_dict['breaks_end'] = event.breaks_end
       
        comment_value=[]
        for comment in event.comment:
            comment_dict = {}
            comment_dict['id'] = comment.id
            comment_dict['content'] = comment.content
            comment_value.append(comment_dict)
            event_dict['comments'] = comment_value
      
        return_value.append(event_dict)

    return jsonify({'events': return_value})




@bp.route('/event/<int:event_id>', methods=['GET'])
def event_by_id(event_id):
        event_dict = {}
        event = Events.query.get(event_id)
        if event is None:
             return jsonify(event_dict)
       
        event_dict['id'] = event.id
        event_dict['date'] = event.date
        event_dict['session_name'] = event.title
        event_dict['speaker'] = event.speaker
        event_dict['speaker_start'] = event.speaker_start
        event_dict['speaker_end'] = event.speaker_end
        event_dict['speaker_file'] = str(request.url_root) +'static/images/'+ str(event.speaker_file) if event.speaker_file else None #event.speaker_file

        event_dict['keynote'] = event.keynote
        event_dict['keynote_start'] = event.keynote_start
        event_dict['keynote_end'] = event.keynote_end
        event_dict['keynote_file'] = str(request.url_root) +'static/images/'+ str(event.keynote_file) if event.keynote_file else None

        event_dict['comments'] = event.comments
        event_dict['comments_start'] = event.comments_start
        event_dict['comments_end'] = event.comments_end
        event_dict['comments_file'] = str(request.url_root) +'static/images/'+ str(event.comments_file) if event.comments_file else None

        event_dict['breaks'] = event.breaks
        event_dict['breaks_start'] = event.breaks_start
        event_dict['breaks_end'] = event.breaks_end
       
        comment_value=[]
        for comment in event.comment:
            comment_dict = {}
            comment_dict['id'] = comment.id
            comment_dict['content'] = comment.content
            comment_value.append(comment_dict)
            event_dict['comments'] = comment_value
      
        return jsonify({'event': event_dict})





@bp.route('/register', methods=['POST'])
def register():
    result= dict()
    if request.method == 'POST':
            user = request.json 
            try:
                if user['password'] != user['password_confirm']:
                    result['error'] = 'Password must be match'
                    return jsonify(result)
                    
                new_user = Users(email=user['email'], f_name=user['f_name'],l_name=user['l_name'], phone=user['phone'], password=generate_password_hash(user['password']))
                try:
                    db.session.add(new_user)
                    db.session.commit()
                    result['sucess'] = 'true'
                    return jsonify(result)
                except IntegrityError:
                    result['error'] = 'email or phone already taken'
                    return jsonify(result)
            except KeyError:
                result['error'] ='Key Error'
                return jsonify(result)
    else:
        result['error'] = 'Something happen bad.'
        return jsonify(result)

    



@bp.route('/login', methods=['POST'])
def login():
    result = dict()
    user_jaon = request.json      
    user = Users.query.filter_by(phone=user_jaon['phone']).first()
    if user:
        if check_password_hash(user.password, user_jaon['password']):
            login_user(user)
            result['response'] = user.id
            result['role'] = user.role
            return jsonify(result)
        else:
            result['response'] = None
            result['role'] = None
            return jsonify(result)
    else:
        result['response'] = None
        result['role'] = None
        return jsonify(result)
    

@bp.route('/comments/<int:event_id>', methods=['GET'])
def comments(event_id):
    cmt = dict()
    return_comment=[]
    comments = Comments.query.filter_by(events_id=event_id, status=1)
    if comments:
        for comment in comments:
            cmt['id'] = comment.id
            cmt['content'] = comment.content
            cmt['events_id'] = comment.events_id
            return_comment.append(cmt)

        return jsonify({'comments':return_comment})
    

@bp.route('/comments', methods=['POST'])
def post_comment():
    comment = request.json
    result = dict()
    try:
        if comment['events_id'] and comment['content']:
            new_comment = Comments(content=comment['content'], events_id=comment['events_id'])
            db.session.add(new_comment)
            db.session.commit()
            result['sucsess'] = 'true'
            return jsonify(result)
        else:
            result['sucsess'] = 'false'
            return jsonify(result)
    except KeyError:
        result['error'] = 'Key Error'
        return jsonify(result)
    
    
