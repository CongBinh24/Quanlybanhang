from sqlalchemy import func

from app.models import User, Phong, PhieuThuePhong, PhongType, ThanhToanType, HoaDon, QuiDinh
from app import db
from sqlalchemy.sql import extract
import hashlib

def get_Qui_Dinh(id):
    return QuiDinh.query.get(id)

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_phong_by_id(id):
    return Phong.query.get(id)

def get_phieu_thue_phong_by_id(id):
    return PhieuThuePhong.query.get(id)

def check_login(username, password):
    if username and password:
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        return User.query.filter(User.username.__eq__(username.strip()),
                                 User.password.__eq__(password)).first()
    return None

def get_all_phong(name):
    if name == None:
        name = ""
    return Phong.query.filter(Phong.tenPhong.contains(name),
                              Phong.tinhTrang == PhongType.TRONG).all()

def get_phong_da_dat(name):
    if name == None:
        name = ""
    return PhieuThuePhong.query.filter(PhieuThuePhong.tenKhach.contains(name),
                                       PhieuThuePhong.tinhTrang == ThanhToanType.CHUA_THANH_TOAN,
                                       PhieuThuePhong.active==True).all()

def get_all_phieu_thue_phong(name):
    return PhieuThuePhong.query.filter(PhieuThuePhong.tenKhach.contains(name) ).all()

def add_phieu_thue_phong(phieu):
    try:
        db.session.add(phieu)
        db.session.commit()
        p = Phong.query.get(phieu.phong_id)
        p.tinhTrang = PhongType.DA_DAT
        db.session.add(p)
        db.session.commit()
        return True
    except:
        print("ERROR")
    return False

def add_hoa_don(hoadon, id_phong):
    try:
        db.session.add(hoadon)
        db.session.commit()

        p = Phong.query.get(id_phong)
        p.tinhTrang = PhongType.TRONG
        db.session.add(p)
        db.session.commit()

        ptp = PhieuThuePhong.query.get(hoadon.phieuThuePhong_id)
        ptp.tinhTrang = ThanhToanType.DA_THANH_TOAN
        db.session.add(ptp)
        db.session.commit()


        return True
    except:
        print("ERROR")
    return False


def stats(kw, from_date= None, to_date = None):
    p = db.session.query(Phong.id, Phong.tenPhong, func.sum(HoaDon.tongTien))\
        .join(PhieuThuePhong, PhieuThuePhong.phong_id.__eq__(Phong.id), isouter=True)\
        .join(HoaDon, HoaDon.phieuThuePhong_id.__eq__(PhieuThuePhong.id), isouter=True)\
        .group_by(Phong.id, Phong.tenPhong)

    if kw:
        p = p.filter(Phong.tenPhong.contains(kw))

    if from_date:
        p = p.filter(HoaDon.ngayTao.__ge__(from_date))

    if to_date:
        p = p.filter(HoaDon.ngayTao.__le__(to_date))

    return p.all()

def month_stats(year):
    return db.session.query(extract('month', HoaDon.ngayTao), func.sum(HoaDon.tongTien))\
                .filter(extract('year', HoaDon.ngayTao) == year).group_by(extract('month', HoaDon.ngayTao))\
                .order_by(extract('month', HoaDon.ngayTao)).all()

def add_user(user):
    try:
        db.session.add(user)
        db.session.commit()
        return True
    except:
        print("ERROR")
    return False