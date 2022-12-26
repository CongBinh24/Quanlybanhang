from sqlalchemy import String, Integer, Column, Float, ForeignKey, Boolean, DateTime, Enum
from sqlalchemy.orm import relationship
from app import db, admin
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
from enum import Enum as UserEnum
from flask_login import UserMixin

class UserRole(UserEnum):
    ADMIN = 1
    USER = 2
    NHANVIEN = 3

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)
    joined_date = Column(DateTime, default=datetime.now())
    avatar = Column(String(150))
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    gmail = Column(String(50))
    phone = Column(String(20))
    address = Column(String(150))
    #hoaDon = relationship('HoaDon', uselist=False, backref='Phong', lazy=False)
    #phieuThuePhong = relationship('PhieuThuePhong', uselist=False, backref='Phong', lazy=False)

    def __str__(self):
        return self.name

class PhongType(UserEnum):
    TRONG = 1
    DA_DAT = 2

class Phong(db.Model):
    __tablename__ = 'Phong'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tenPhong = Column(String(50), nullable=False)
    loaiPhong = Column(String(50), nullable=False)
    donGia = Column(Float, nullable=False)
    tinhTrang = Column(Enum(PhongType), nullable=False)
    #phieuThuePhong1 = relationship('PhieuThuePhong', uselist=False, backref='Phong', lazy=False)

    def __str__(self):
        return self.tenPhong

class KhachType(UserEnum):
    NOI_DIA = 1
    NUOC_NGOAI = 2

class ThanhToanType(UserEnum):
    CHUA_THANH_TOAN = 1
    DA_THANH_TOAN = 2

class PhieuThuePhong(db.Model):
    __tablename__ = 'phieuthuephong'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tenKhach = Column(String(100), nullable=False)
    loaiKhach = Column(String(100), nullable=False)
    CMND =  Column(String(20), nullable=False)
    diaChi = Column(String(100), nullable=False)
    ngayNhanPhong = Column(DateTime, default=datetime.now())
    ngayTraPhong = Column(DateTime)
    soLuongKhach = Column(Integer, nullable=False)
    active = Column(Boolean, default=True)
    tinhTrang = Column(Enum(ThanhToanType), default=ThanhToanType.CHUA_THANH_TOAN)
    phong_id = Column(Integer, ForeignKey(Phong.id), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)

    def __str__(self):
        return self.tenKhach

class HoaDon(db.Model):
    __tablename__ = 'hoadon'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tongTien = Column(Float, nullable=False)
    phuThu = Column(Float)
    phieuThuePhong_id = Column(Integer, ForeignKey(PhieuThuePhong.id), nullable=False)
    ngayTao = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)

class QuiDinh(db.Model):
    __tablename__ = 'quidinh'
    id = Column(Integer, primary_key=True, autoincrement=True)
    soLuong = Column(Integer)
    tiLePhuThu = Column(Float)

if __name__=="__main__":
    db.create_all()