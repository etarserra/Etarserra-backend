from flask import Blueprint
from app.storages.controller import FileStorage, MediaStorage, MediaDownload

storage_api = Blueprint('storage_api',__name__)

storage_api.add_url_rule('/upload_media', view_func=FileStorage.as_view('upload_media'), methods=['POST'])
storage_api.add_url_rule('/media/<string:file_name>', view_func=MediaStorage.as_view('media'), methods=['DELETE', 'GET'])
storage_api.add_url_rule('/media/download/<string:file_name>', view_func=MediaDownload.as_view('media_download'), methods=['GET'])