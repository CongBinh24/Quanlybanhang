function getRoom(id){
    document.getElementById("idPhong").value = id;
  };

function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2)
        month = '0' + month;
    if (day.length < 2)
        day = '0' + day;

    return [year, month, day].join('-');
}

function formatDate2(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2)
        month = '0' + month;
    if (day.length < 2)
        day = '0' + day;

    return [month, day, year].join('/');
}

function parseDate(str) {
    var mdy = str.split('/');
    return new Date(mdy[2], mdy[0]-1, mdy[1]);
}

function datediff(first, second) {
    // Take the difference between the dates and divide by milliseconds per day.
    // Round to nearest whole number to deal with DST.
    return Math.round((second-first)/(1000*60*60*24));
}

function getRoomById(id) {
    let fecthDate = {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify()
    }
    return fetch(`/getPhongById/` + id, fecthDate)
            .then(res => res.json())
            .then(data => data)
            .catch(err => err)
}


function getHoaDon(id, name, date, id_phong, soLuongKhach, loaiKhach){
    document.getElementById("TenKhach").value = name;
    let ngayNhanPhong = document.getElementById("NgayNhanPhong");
    ngayNhanPhong.value = formatDate(date);
    let ngayTraPhong = document.getElementById("NgayTraPhong");
    ngayTraPhong.value = formatDate(new Date());
    document.getElementById("idPhieuThuePhong").value = id;
    document.getElementById("idPhong").value = id_phong;

    var future = moment(formatDate2(new Date()));
    var start = moment(formatDate2(date));
    var d = future.diff(start, 'days'); // 9

    getRoomById(id_phong).then(res =>{
        console.log(res);
        let phuThu, tongTien;
        if( soLuongKhach > res.soLuong)
        {
            if (loaiKhach == "NOI_DIA")
            {
                phuThu = (res.donGia * d * 35 / 100);
                console.log(phuThu)
                tongTien = phuThu + res.donGia * d;
            }
            else{
                phuThu = (res.donGia * d * 35 / 100) + (res.donGia * d + (res.donGia * d * 35 / 100)) * res.phuThu / 100;
                tongTien = phuThu + res.donGia * d;
            }
        }
        else
        {
            if(loaiKhach == "NOI_DIA")
            {
                phuThu = 0;
                tongTien = phuThu + res.donGia * d;
            }else
            {
                phuThu = (res.donGia * d * 35 / 100);
                tongTien = phuThu + res.donGia * d;
            }
        }
        document.getElementById("PhuThu").value = phuThu;
        document.getElementById("TongTien").value = tongTien;

    });
};