# 1. Xây dựng lớp GiangVien
class GiangVien:
    def __init__(self, ho_ten, hoc_vi, email):
        """Khởi tạo thông tin giảng viên"""
        self.ho_ten = ho_ten
        self.hoc_vi = hoc_vi
        self.email = email

    def __str__(self):
        """Hiển thị thông tin giảng viên"""
        return f"Giảng viên: {self.ho_ten} - Học vị: {self.hoc_vi} - Email: {self.email}"


# 2. Xây dựng lớp KhoaHoc
class KhoaHoc:
    def __init__(self, ma_khoa_hoc, ten_khoa_hoc, so_buoi, hoc_phi_moi_buoi, giang_vien):
        """Khởi tạo thông tin khóa học, bao gồm đối tượng giang_vien (quan hệ hợp thành)"""
        self.ma_khoa_hoc = ma_khoa_hoc
        self.ten_khoa_hoc = ten_khoa_hoc
        self.so_buoi = so_buoi
        self.hoc_phi_moi_buoi = hoc_phi_moi_buoi
        self.giang_vien = giang_vien

    def tinh_hoc_phi(self):
        """Tính tổng học phí của khóa học"""
        return self.so_buoi * self.hoc_phi_moi_buoi

    def __str__(self):
        """Hiển thị thông tin khóa học và giảng viên phụ trách"""
        info = (f"Mã KH: {self.ma_khoa_hoc} | Tên KH: {self.ten_khoa_hoc}\n"
                f"Thời lượng: {self.so_buoi} buổi | Học phí/buổi: {self.hoc_phi_moi_buoi:,} VNĐ\n"
                f"Phụ trách: {self.giang_vien}")
        return info

    # 4. Nạp chồng toán tử +
    def __add__(self, other):
        """Thực hiện cộng hai khóa học bất kỳ để tạo thành gói học tập"""
        tong_hoc_phi = self.tinh_hoc_phi() + other.tinh_hoc_phi()
        return (f"Gói học tập: {self.ten_khoa_hoc} + {other.ten_khoa_hoc}\n"
                f"Tổng học phí: {tong_hoc_phi:,} VNĐ")


# 3. Xây dựng lớp kế thừa KhoaHocOnline
class KhoaHocOnline(KhoaHoc):
    def __init__(self, ma_khoa_hoc, ten_khoa_hoc, so_buoi, hoc_phi_moi_buoi, giang_vien, nen_tang_hoc):
        """Khởi tạo lớp con, kế thừa các thuộc tính của lớp cha và thêm nen_tang_hoc"""
        super().__init__(ma_khoa_hoc, ten_khoa_hoc, so_buoi, hoc_phi_moi_buoi, giang_vien)
        self.nen_tang_hoc = nen_tang_hoc

    def __str__(self):
        """Ghi đè phương thức __str__ để bổ sung thêm nền tảng học"""
        base_info = super().__str__()
        return f"{base_info}\nNền tảng học: {self.nen_tang_hoc}"


# 5. Chương trình chính
if __name__ == "__main__":
    # Tạo giảng viên
    gv1 = GiangVien("Nguyễn Văn A", "Tiến sĩ", "nva@haui.edu.vn")
    gv2 = GiangVien("Trần Thị B", "Thạc sĩ", "ttb@haui.edu.vn")

    # Tạo đối tượng KhoaHoc và đối tượng KhoaHocOnline
    # Sử dụng các môn học đặc thù của chuyên ngành công nghệ thông tin
    kh1 = KhoaHoc("IT6130", "Lập trình Python Cơ bản", 15, 200000, gv1)
    kh2 = KhoaHocOnline("SE102", "Thiết kế Kiến trúc Phần mềm", 20, 250000, gv2, "Google Meet")

    # In thông tin các khóa học ra màn hình
    print("="*40)
    print("THÔNG TIN CÁC KHÓA HỌC")
    print("="*40)
    print(kh1)
    print("-" * 40)
    print(kh2)
    print("="*40)

    # In học phí của từng khóa học
    print("\nHỌC PHÍ TỪNG KHÓA HỌC")
    print(f"Học phí khóa '{kh1.ten_khoa_hoc}': {kh1.tinh_hoc_phi():,} VNĐ")
    print(f"Học phí khóa '{kh2.ten_khoa_hoc}': {kh2.tinh_hoc_phi():,} VNĐ")
    print("="*40)

    # Thực hiện phép cộng giữa hai khóa học và in kết quả
    print("\nKẾT QUẢ GÓI HỌC TẬP")
    goi_hoc_tap = kh1 + kh2
    print(goi_hoc_tap)
    print("="*40)