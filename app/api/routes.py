from flask import jsonify, request
from app.api import bp
from app.extensions import db
from app.models.post import Post
from app.models.event import Events
from app.models.comments import Comments


@bp.route('/')
def index():
    events = Events.query.all()
    return_value=[]
    comment_value=[]
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
        
        for comment in event.comment:
            comment_dict = {}
            comment_dict['id'] = comment.id
            comment_dict['content'] = comment.content
            comment_value.append(comment_dict)
            event_dict['comments'] = comment_value
           
            
        
        return_value.append(event_dict)
        


    return jsonify({'events': return_value})
    