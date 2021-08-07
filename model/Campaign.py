# -*- coding: utf-8 -*-
# created by makise, 2021/3/16
from flask_restful import fields


class Campaign:
    def __init__(self, campaign_id, campaign_time, campaign_location, association_id, campaign_note, campaign_image):
        self.campaign_id = campaign_id
        self.campaign_time = campaign_time
        self.campaign_location = campaign_location
        self.association_id = association_id
        self.campaign_note = campaign_note
        self.campaign_image = campaign_image


resource_field_campaign = {
    'campaign_id': fields.String,
    'campaign_time': fields.DateTime,
    'campaign_location': fields.String,
    'association_id': fields.String,
    'campaign_note': fields.String,
    'campaign_image': fields.String
}
