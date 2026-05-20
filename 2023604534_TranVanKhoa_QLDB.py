# 1. Xây dựng lớp CauThu
class CauThu:
    def __init__(self, ho_ten, vi_tri, quoc_tich):
        """Khởi tạo thông tin cầu thủ"""
        self.ho_ten = ho_ten
        self.vi_tri = vi_tri
        self.quoc_tich = quoc_tich

    def __str__(self):
        """Hiển thị thông tin cầu thủ"""
        return f"{self.ho_ten:<20} | Vị trí: {self.vi_tri:<10} | Quốc tịch: {self.quoc_tich}"


# 2. Xây dựng lớp DoiBong
class DoiBong:
    def __init__(self, ten_doi, huan_luyen_vien):
        """Khởi tạo đội bóng. Danh sách cầu thủ ban đầu là rỗng."""
        self.ten_doi = ten_doi
        self.huan_luyen_vien = huan_luyen_vien
        # Thuộc tính danh_sach_cau_thu chứa các đối tượng CauThu (Quan hệ hợp thành)
        self.danh_sach_cau_thu = []

    def them_cau_thu(self, cau_thu):
        """Thêm một đối tượng CauThu vào danh sách"""
        self.danh_sach_cau_thu.append(cau_thu)

    def __str__(self):
        """Hiển thị thông tin đội bóng và danh sách cầu thủ"""
        thong_tin = f"Tên đội: {self.ten_doi} | HLV: {self.huan_luyen_vien}\n"
        thong_tin += "Danh sách cầu thủ:\n"
        if not self.danh_sach_cau_thu:
            thong_tin += "  (Chưa có cầu thủ nào)\n"
        else:
            for i, ct in enumerate(self.danh_sach_cau_thu, 1):
                thong_tin += f"  {i}. {ct}\n"
        return thong_tin

    # 4. Nạp chồng toán tử +
    def __add__(self, other):
        """
        Nạp chồng toán tử + giữa 2 đội bóng.
        Trả về một đối tượng DoiBong mới, gộp tên, HLV và danh sách cầu thủ của cả 2 đội.
        """
        ten_doi_moi = f"Liên quân {self.ten_doi} & {other.ten_doi}"
        hlv_moi = f"{self.huan_luyen_vien} & {other.huan_luyen_vien}"

        # Tạo đội bóng mới
        doi_moi = DoiBong(ten_doi_moi, hlv_moi)

        # Ghép danh sách cầu thủ từ cả 2 đội
        doi_moi.danh_sach_cau_thu = self.danh_sach_cau_thu + other.danh_sach_cau_thu

        return doi_moi


# 3. Xây dựng lớp kế thừa DoiTuyenQuocGia
class DoiTuyenQuocGia(DoiBong):
    def __init__(self, ten_doi, huan_luyen_vien, quoc_gia):
        """Kế thừa lớp DoiBong và bổ sung thuộc tính quoc_gia"""
        super().__init__(ten_doi, huan_luyen_vien)
        self.quoc_gia = quoc_gia

    def __str__(self):
        """Ghi đè phương thức __str__ để hiển thị thêm thông tin quốc gia"""
        # Tái sử dụng form hiển thị của lớp cha
        thong_tin_co_ban = super().__str__()
        return f"--- ĐỘI TUYỂN QUỐC GIA: {self.quoc_gia.upper()} ---\n{thong_tin_co_ban}"


# 5. Chương trình chính
if __name__ == "__main__":
    # Tạo 2 đội tuyển quốc gia
    dt_vietnam = DoiTuyenQuocGia("Việt Nam", "Kim Sang-sik", "Việt Nam")
    dt_argentina = DoiTuyenQuocGia("Argentina", "Lionel Scaloni", "Argentina")

    # Tạo và thêm các cầu thủ cho đội Việt Nam
    dt_vietnam.them_cau_thu(CauThu("Nguyễn Quang Hải", "Tiền vệ", "Việt Nam"))
    dt_vietnam.them_cau_thu(CauThu("Đặng Văn Lâm", "Thủ môn", "Việt Nam"))
    dt_vietnam.them_cau_thu(CauThu("Bùi Hoàng Việt Anh", "Trung vệ", "Việt Nam"))

    # Tạo và thêm các cầu thủ cho đội Argentina
    dt_argentina.them_cau_thu(CauThu("Lionel Messi", "Tiền đạo", "Argentina"))
    dt_argentina.them_cau_thu(CauThu("Emiliano Martínez", "Thủ môn", "Argentina"))

    # In thông tin đội và danh sách cầu thủ
    print(dt_vietnam)
    print("-" * 50)
    print(dt_argentina)
    print("=" * 60)

    # Thực hiện và hiển thị kết quả phép cộng giữa 2 đội
    print("\n[KẾT QUẢ PHÉP CỘNG HAI ĐỘI BÓNG - TẠO ĐỘI LIÊN QUÂN]")
    doi_lien_quan = dt_vietnam + dt_argentina
    print(doi_lien_quan)