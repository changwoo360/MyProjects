from django.utils.deprecation import MiddlewareMixin

from django.shortcuts import render, redirect
import re
class CheckMiddleware(MiddlewareMixin):
    def process_request(self, request):
        current_path = request.path_info
        # 检查是否在白名单
        valid_url_list = ['/login/', '/admin/.*', '/register/']
        for valid_url in valid_url_list:
            ret = re.match(valid_url, current_path)
            if ret:
                return None

        # 校验是否登陆
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('/login/')