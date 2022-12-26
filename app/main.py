import json
from flask import render_template, request, redirect
from app import app, utils, login_manager
import os
from app.admin import *
from app.models import *
from flask_login import login_user
from flask_login import logout_user, current_user
import hashlib

@app.route("/")
def index():
    return render_template("index.html", UserRole=UserRole)

@app.route("/phong", methods = ['GET'])
def phong():
    kw = request.args.get("kw")
    phongs = utils.get_all_phong(kw)
    return render_template("user/phong.html", phongs=phongs, PhongType=PhongType, UserRole=UserRole)

@app.route("/phong", methods = ['POST'])
def addPhieu():
    phieuThuePhong = PhieuThuePhong()
    phieuThuePhong.tenKhach = request.form["TenKhach"]
    phieuThuePhong.loaiKhach = request.form["LoaiKhach"]
    phieuThuePhong.CMND = request.form["CMND"]
    phieuThuePhong.diaChi = request.form["DiaChi"]
    phieuThuePhong.soLuongKhach = request.form["SoLuongKhach"]
    phieuThuePhong.phong_id = request.form["IDPhong"]
    phieuThuePhong.user_id = current_user.id
    phongs = utils.get_all_phong("")
    if utils.add_phieu_thue_phong(phieuThuePhong) == True:
        phongs = utils.get_all_phong("")
        return render_template("user/phong.html", phongs=phongs, msg="Thêm phiếu đặt phòng thành công", PhongType=PhongType, UserRole=UserRole)
    return render_template("user/phong.html", phongs=phongs, msg="Thêm phiếu đặt phòng thất bại", PhongType=PhongType, UserRole=UserRole)

@app.route("/phieu_thue_phong", methods = ['GET'])
def phieu_thue():
    kw = request.args.get("kw")
    phongs = utils.get_phong_da_dat(kw)
    return render_template(("user/phieu_thue_phong.html"), phongs=phongs, KhachType=KhachType, UserRole=UserRole)

@app.route("/phieu_thue_phong", methods = ['POST'])
def add_hoa_don():
    hoaDon = HoaDon()
    hoaDon.phieuThuePhong_id = request.form["IDPhieuThuePhong"]
    hoaDon.tongTien = request.form["TongTien"]
    hoaDon.user_id = current_user.id
    hoaDon.phuThu = request.form["PhuThu"]
    phong_id = request.form["IDPhong"]
    phongs = utils.get_phong_da_dat("")
    if(utils.add_hoa_don(hoaDon, phong_id)) == True:
        return render_template(("user/phieu_thue_phong.html"), phongs=phongs, msg="Thanh toánh thành công", KhachType=KhachType, UserRole=UserRole)

    return render_template(("user/phieu_thue_phong.html"), phongs=phongs, msg="Thanh toánh thất bại", KhachType=KhachType, UserRole=UserRole)

@app.route('/huyPhong/<phong_id>', methods=['GET'])
def huy_phong(phong_id):
    phong = utils.get_phieu_thue_phong_by_id(phong_id)
    phong.active = False
    db.session.add(phong)
    db.session.commit()
    kw = request.args.get("kw")
    phongs = utils.get_phong_da_dat(kw)
    return render_template(("user/phieu_thue_phong.html"), phongs=phongs, msg="Hủy thành công", KhachType=KhachType, UserRole=UserRole)

@app.route('/getPhongById/<phong_id>', methods=['GET'])
def get_Phong_By_ID(phong_id):
    phong = utils.get_phong_by_id(phong_id)
    quiDinh = utils.get_Qui_Dinh(1)
    data = {
         "donGia": phong.donGia,
        "soLuong": quiDinh.soLuong,
        "phuThu": quiDinh.tiLePhuThu
    }
    return json.dumps(data)

@app.route('/admin-login', methods=['POST', 'GET'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = utils.check_login(username, password)
    if user:
        login_user(user=user)

    return redirect('/admin')

@app.route("/logout", methods=['GET'])
def logout():
    logout_user()
    return redirect('/login')

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = utils.check_login(username, password)
        if user:
            login_user(user=user)
            return redirect('/')

    return render_template("base/login.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = User();
        user.name = request.form.get('name')
        user.username = request.form.get('username')
        user.gmail = request.form.get('gmail')
        user.phone = request.form.get('phone')
        user.address = request.form.get('address')
        password = request.form.get('password')
        if password and user.username:
            user.password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
            if utils.add_user(user) == True:
                return render_template("base/signup.html", msg = "Đăng kí thành công")

        return render_template("base/signup.html", msg = "Đăng kí thất bại")
    else:
        return render_template("base/signup.html")


@login_manager.user_loader
def load_user(user_id):
    try:
        return utils.get_user_by_id(user_id)
    except:
        return None


if __name__ == "__main__":
    app.run(debug=True)