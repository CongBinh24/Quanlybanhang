from flask_admin.contrib.geoa import ModelView
from flask_admin import BaseView, expose
from flask_login import logout_user, current_user
from flask import redirect, request
from sqlalchemy.sql import extract
from app import admin, db, utils
from app.models import Phong, User, PhieuThuePhong, HoaDon, UserRole, QuiDinh
from flask_admin.contrib.sqla import ModelView
from datetime import datetime

class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN

class AuthenticatedModelView2(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.USER

class QuiDinhModelView(ModelView):
    can_delete = False
    can_create = False
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN

class PhongView(AuthenticatedModelView):
    column_display_pk = True

class LogOutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated

class StatsView(BaseView):
    @expose('/')
    def index(self):
        kw = request.args.get('kw')
        from_date = request.args.get('from_date')
        to_date = request.args.get('to_date')
        year = request.args.get('year', datetime.now().year)
        return self.render('admin/stats.html',
                           month_stats = utils.month_stats(year=year),
                           stats=utils.stats(kw = kw, from_date = from_date, to_date = to_date))

    def is_accessible(self):
        return current_user.is_authenticated



admin.add_views(AuthenticatedModelView(Phong, db.session, name='Phòng'))
admin.add_views(AuthenticatedModelView(User, db.session, name ='Người dùng'))
admin.add_views(AuthenticatedModelView(PhieuThuePhong, db.session, name="Phiếu thuê phòng"))
admin.add_views(AuthenticatedModelView(HoaDon, db.session, name="Hóa đơn"))
admin.add_views(QuiDinhModelView(QuiDinh, db.session, name="Quy định"))
admin.add_views(StatsView(name='Thống kê'))
admin.add_views(LogOutView(name='Đăng xuất'))