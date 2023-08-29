from flask import Flask, request, Response
import requests

app = Flask(__name__)

# 跨域API的endpoint
API_URL = 'https://chat.openai.com/api/auth/session'




@app.route('/proxy')
def proxy():
    # 将请求转发到跨域API
    resp = requests.request(
        method=request.method,
        url=API_URL ,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
    )

    # 将响应返回给客户端
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]
    response = Response(resp.content, resp.status_code, headers)
    return response



# @app.route('/proxy/<path:path>')
# def proxy(path):
#     # 将请求转发到跨域API
#     resp = requests.request(
#         method=request.method,
#         url=API_URL + '/' + path,
#         headers={key: value for (key, value) in request.headers if key != 'Host'},
#         data=request.get_data(),
#         cookies=request.cookies,
#     )
#
#     # 将响应返回给客户端
#     excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
#     headers = [(name, value) for (name, value) in resp.raw.headers.items()
#                if name.lower() not in excluded_headers]
#     response = Response(resp.content, resp.status_code, headers)
#     return response


if __name__ == '__main__':
    app.run()