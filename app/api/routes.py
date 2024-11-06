from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from flask_login import login_user
from app.api import bp
from app.extensions import db
from app.models.event import Events, Agenda
from app.models.comments import Comments
from app.models.user import Users
from app.models.devices import Devices
from app.models.menu import Faculty, Welcome, Menu
from app.utility import generate_token, verify_token



@bp.route('/events')
def index():
    events = Events.query.all()
    # events = Events.query.filter_by(agenda_id=1)
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
        event_dict['open_house'] = event.open_house
        event_dict['open_house_start'] = event.open_house_start
        event_dict['open_house_end'] = event.open_house_end
       
        comment_value=[]
        for comment in event.comment:
            comment_dict = {}
            comment_dict['id'] = comment.id
            comment_dict['user'] = comment.user_name + ' at '+ str(comment.created_at)
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

        event_dict['open_house'] = event.open_house
        event_dict['open_house_start'] = event.open_house_start
        event_dict['open_house_end'] = event.open_house_end
       
        comment_value=[]
        for comment in event.comment:
            comment_dict = {}
            comment_dict['id'] = comment.id
            comment_dict['user'] = comment.user_name + ' at '+ str(comment.created_at)
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
        event_dict['open_house'] = event.open_house
        event_dict['open_house_start'] = event.open_house_start
        event_dict['open_house_end'] = event.open_house_end
       
        comment_value=[]
        for comment in event.comment:
            comment_dict = {}
            comment_dict['id'] = comment.id
            comment_dict['user'] = comment.user_name + ' at '+ str(comment.created_at)
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
                    
                new_user = Users(f_name=user['f_name'],l_name=user['l_name'], phone=user['phone'], password=generate_password_hash(user['password']))
                try:
                    db.session.add(new_user)
                    db.session.commit()
                    result['success'] = 'true'
                    return jsonify(result)
                except IntegrityError:
                    result['error'] = 'phone already taken'
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
   
    return_comment=[]
    comments = Comments.query.filter_by(events_id=event_id)
    if comments:
        for comment in comments:
            cmt = dict()
            cmt['id'] = comment.id
            cmt['user'] = comment.user_name + ' at '+ str(comment.created_at)
            cmt['events_id'] = comment.events_id
            return_comment.append(cmt)

        return jsonify({'comments':return_comment})
    

@bp.route('/comments', methods=['POST'])
def post_comment():
    comment = request.json
    result = dict()
    try:
        if comment['user_id']:
            user =Users.query.get(comment['user_id'])
            commenter = user.f_name +' '+ user.l_name

        if comment['events_id'] and comment['content']:
            new_comment = Comments(content=comment['content'], events_id=comment['events_id'], user_name=commenter)
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
    
@bp.route('/checkphone', methods=['POST'])
def checkphone():
    phone = request.json
    result = dict()
    user = Users.query.filter_by(phone=phone['phone']).first()
    if user:
        result['response'] = user.phone
        result['role'] = user.role
        return jsonify(result)
    else:
        result['response'] = None
        result['role'] = None
        return jsonify(result)
    

@bp.route('/faculties', methods=['GET'])
def faculties():
    directors = Faculty.query.filter_by(faculty_type='director')
    us_faculty = Faculty.query.filter_by(faculty_type='us_faculty')
    faculty = Faculty.query.filter_by(faculty_type='faculty')
    director_list = []
    us_faculty_list = []
    faculty_list = []
    response =[]
    for director in directors:
        director_dict = {}
        director_dict['title'] = director.title
        director_dict['content'] = director.content
        director_dict['picture'] = str(request.url_root) +'static/images/'+ str(director.picture) if director.picture else None
        director_list.append(director_dict)

    for usfaculty in us_faculty:
        usfaculty_dict = {}
        usfaculty_dict['title'] = usfaculty.title
        usfaculty_dict['content'] = usfaculty.content
        usfaculty_dict['picture'] = str(request.url_root) +'static/images/'+ str(usfaculty.picture) if usfaculty.picture else None
        us_faculty_list.append(usfaculty_dict)

    for fac in faculty:
        faculty_dict = dict()
        faculty_dict['title'] = fac.title
        faculty_dict['content'] = fac.content
        faculty_dict['picture'] = str(request.url_root) +'static/images/'+ str(fac.picture) if fac.picture else None
        faculty_list.append(faculty_dict)

    response.append({'directors':director_list})
    response.append({'north americal faculty':us_faculty_list})
    response.append({'faculty':faculty_list})
    # return jsonify({'directors':director_list}, {'north americal faculty':us_faculty_list}, {'faculty':faculty_list})
    return jsonify({'response':response})

@bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.get_json()
    phone = data.get('phone')
    # Assume a function find user by phone check the user database
    user = Users.query.filter_by(phone=phone).first()
    if user:
        token = generate_token(user.phone)
        # reset_url = f"{request.url_root}api/reset-password/{token}"
        return jsonify({'response': token}), 200
    else:
        return jsonify({'error': 'Phone not found'}), 404

@bp.route('/reset-password', methods=['POST'])
def reset_password():
    jsondata = request.get_json()
    token = jsondata.get('token')
    phone = verify_token(token)
    if not phone:
        return jsonify({'error': 'Invalid or expired token'}), 400
        
    new_password = jsondata.get('password')
    # Update the user's password in the database
    user = Users.query.filter_by(phone=phone).first()
    if user:
        user.password = generate_password_hash(new_password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'response': 'Password updated successfully'}), 200
    
@bp.route('/welcome', methods=['GET'])
def welcome():
    welcomes = Welcome.query.all()
    welcome_lsit = []
    for welcome in welcomes:

        wel = {}
        wel['id'] = welcome.id
        wel['title'] = welcome.title
        wel['content'] = welcome.content
        wel['picture'] = str(request.url_root) +'static/images/'+ str(welcome.picture) if welcome.picture else None
        wel['picture_title'] = welcome.picture_title
        wel['caption'] = welcome.caption
        welcome_lsit.append(wel)

        return jsonify( welcome_lsit)


@bp.route('/menu', methods=['GET'])
def menu():
    menus = Menu.query.all()
    menu_lsit = []
    for menu in menus:
        menudict = {}
        menudict['id'] = menu.id
        menudict['title'] = menu.title
        menudict['created_at'] = menu.created_at
        menu_lsit.append(menudict)

    return jsonify( menu_lsit)


@bp.route('/devices', methods=['GET'])
def devices():
    devices = Devices.query.all()
    device_list =[]
    for device in devices:
        token = {}
        token['id'] = device.id
        token['role'] = device.role
        token['token'] = device.token
        token['created_at'] = device.created_at
        device_list.append(token)

    return jsonify({'response': device_list})

@bp.route('/devices', methods=['POST'])
def device_token():
    jsontoken = request.get_json()
    token = jsontoken.get('token')
    user_type = jsontoken.get('role')
    token_from_db = Devices.query.filter_by(token=token).first()
    try:
        if token_from_db is None:
            new_token = Devices(token=token, role=user_type)
            db.session.add(new_token)
            db.session.commit()
            return jsonify({'response': 'true'}), 201
        else:
            return jsonify({'response': 'Token alredy taken'}), 200
    except:
        return jsonify({'error':'false'}), 400



@bp.route('/agenda', methods=['GET'])
def agenda():
    agendas = Agenda.query.all()
    agenda_list = []
    for agenda in agendas:
        agendadict = {}
        agendadict['id'] = agenda.id
        agendadict['title'] = agenda.title
        agendadict['date'] = agenda.date
        agendadict['created_at'] = agenda.created_at

        agenda_list.append(agendadict)

    return jsonify( agenda_list)


@bp.route('/delete_account', methods=['POST'])
def delete_account():
     phonedata = request.get_json()
     phone = phonedata.get('phone')
     account = Users.query.filter_by(phone=phone).first()
     if account:
        db.session.delete(account)
        db.session.commit()
        return jsonify({'success': 'true'})
     else:
         return jsonify({'error':'false'})
     


    


    






    
