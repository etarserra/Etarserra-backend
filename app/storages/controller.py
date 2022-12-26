from flask.views import MethodView
from flask import request, send_file
import uuid
import ftplib
from io import BytesIO

from app.config import Config

HOST = Config.HOST_FTP
USER = Config.USER_FTP
PASS = Config.PASS_FTP

mimetypes = {
    'png':'image/png',
    'jpeg':'image/jpeg',
    'jpg':'image/jpg',
    'gif':'image/gif',
    'mp4':'video/mp4',
    'webm':'video/webm',
    'pdf':'application/pdf'
}

# /upload_media
class FileStorage(MethodView):

    ''' Cria um arquivo no storage '''
    def post(self):
        media = request.files.get('media')
        if not media:
            return {'erro' : 'arquivo não enviado'}, 400
        
        name = media.filename

        media_format = request.args.get('media_format')
        if not media_format:
            return {'erro' : 'formato do arquivo não especificado'}, 400

        media_path = f'{uuid.uuid4().hex}_{name}'
        # response = storage.upload_file(file_key=media_path, file=media, file_format=media_format)

        ftp = ftplib.FTP_TLS(HOST, USER, PASS)
        ftp.encoding = "utf-8"

        try:
            response = ftp.storbinary(f"STOR {media_path}", fp=media)
        except:
            ftp.close()
            return {"erro": "não foi possível fazer o upload do arquivo"}, 400
        
        ftp.close()

        if not response:
            return {"erro": "problemas ao enviar o arquivo"}
        
        return {
            "response": response,
            "media_path": media_path
        }, 201


def get_media_format(filename: str):
    divided = filename.split('.')
    return divided[-1]


# /media/<string:file_name>
class MediaStorage(MethodView):
    
    ''' Pega um arquivo do storage '''
    def get(self, file_name):
        file = BytesIO()

        ftp = ftplib.FTP_TLS(HOST, USER, PASS)
        ftp.encoding = "utf-8"

        try:
            response = ftp.retrbinary(f"RETR {file_name}", file.write)
        except:
            ftp.close()
            return {"erro", "arquivo não encontrado"}, 404

        ftp.close()

        file.seek(0)

        if not response:
            return {'erro': 'arquivo não encontrado'}, 404
        
        media_format = get_media_format(file_name)
        if media_format not in mimetypes:
            return {'erro': 'tipo de arquivo não encotrado'}, 400
        
        mimetype = mimetypes[media_format]

        return send_file(file, mimetype=mimetype), 200



    ''' Deleta um arquivo do storage '''
    def delete(self, file_name):
        ftp = ftplib.FTP_TLS(HOST, USER, PASS)
        ftp.encoding = "utf-8"

        try:
            response = ftp.delete(filename=file_name)
        except:
            ftp.close()
            return {"erro": "arquivo não encontrado"}, 404

        ftp.close()
        return {}, 204


# /media/download/<string:file_name>
class MediaDownload(MethodView):
    
    ''' Pega um arquivo do storage para download '''
    # def get(self, file_name): 
        
    #     response = storage.get_download_url(file_key=file_name)
    #     if not response:
    #         return {'erro' : response}, 400
        
    #     return {'URL': response}, 200

    def get(self, file_name):
        file = BytesIO()

        ftp = ftplib.FTP_TLS(HOST, USER, PASS)
        ftp.encoding = "utf-8"

        try:
            response = ftp.retrbinary(f"RETR {file_name}", file.write)
        except:
            ftp.close()
            return {"erro": "arquivo não encontrado"}, 404

        ftp.close()

        file.seek(0)

        if not response:
            return {'erro': 'arquivo não encontrado'}, 404
        
        media_format = get_media_format(file_name)
        if media_format not in mimetypes:
            return {'erro': 'tipo de arquivo não encotrado'}, 400
        
        mimetype = mimetypes[media_format]

        return send_file(file, mimetype=mimetype, as_attachment=True, download_name=file_name), 200
        