class Sach:
    def __init__(self, ten_sach, tac_gia, gia):
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.gia = gia

    def __str__(self):
        return f"{self.ten_sach} | Tác giả: {self.tac_gia} | Giá: {self.gia} VND"


class ThuVien:
    def __init__(self):
        self.danh_sach_sach = []

    def them_sach(self, sach):
        self.danh_sach_sach.append(sach)

    def tim_kiem(self, tu_khoa):
        ket_qua = [sach for sach in self.danh_sach_sach if tu_khoa.lower() in sach.ten_sach.lower()]
        return ket_qua

    def hien_thi_sach(self):
        if not self.danh_sach_sach:
            print(" Thư viện hiện chưa có sách.")
        else:
            print("\n=== Danh sách sách trong thư viện ===")
            for i, sach in enumerate(self.danh_sach_sach, 1):
                print(f"{i}. {sach}")


def main():
    thu_vien = ThuVien()

    while True:
        print("\n===== MENU THƯ VIỆN =====")
        print("1. Thêm sách")
        print("2. Hiển thị tất cả sách")
        print("3. Tìm kiếm sách theo tên")
        print("0. Thoát")
        chon = input(" Nhập lựa chọn: ")

        if chon == "1":
            ten = input("Nhập tên sách: ")
            tac_gia = input("Nhập tác giả: ")
            gia = int(input("Nhập giá: "))
            thu_vien.them_sach(Sach(ten, tac_gia, gia))
            print("✅ Đã thêm sách vào thư viện.")

        elif chon == "2":
            thu_vien.hien_thi_sach()

        elif chon == "3":
            tu_khoa = input("Nhập từ khóa tìm kiếm: ")
            ket_qua = thu_vien.tim_kiem(tu_khoa)
            if ket_qua:
                print("\n=== Kết quả tìm kiếm ===")
                for sach in ket_qua:
                    print(sach)
            else:
                print(" Không tìm thấy sách nào.")

        elif chon == "0":
            print(" Thoát chương trình.")
            break

        else:
            print("⚠️ Lựa chọn không hợp lệ, vui lòng nhập lại.")


if __name__ == "__main__":
    main()
