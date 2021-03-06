from datetime import datetime

import bleach
from markdown import markdown
from markdown_nofollow import NofollowExtension
from flask import url_for

from app import db
from ._base_model import BaseModel


class Comment(db.Model, BaseModel):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    disabled = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    # post = db.relationship('Post', backref='comments', lazy='dynamic')

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'code', 'em', 'i',
                        'strong']
        target.body_html = bleach.linkify(bleach.clean(
            markdown(value, output_format='html', extensions=[NofollowExtension()]),
            tags=allowed_tags, strip=True))

    def to_json(self):
        json_comment = {
            'url': url_for('api.get_comment', id=self.id, _external=True),
            'post_id': self.post_id,
            'body': self.body,
            'body_html': self.body_html,
            'created_at': self.created_at,
            'user': {"username": self.user.username, "profile_picture": self.user.profile_picture},
        }
        return json_comment


db.event.listen(Comment.body, 'set', Comment.on_changed_body)
