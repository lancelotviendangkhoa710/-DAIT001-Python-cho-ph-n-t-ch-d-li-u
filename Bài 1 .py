class SinhVien:
    def __init__(self, ten, tuoi, diemTB):
        self.ten = ten
        self.tuoi = tuoi
        self.diemTB = diemTB

    def hien_thi(self):
        return f"Tên: {self.ten}, Tuổi: {self.tuoi}, Điểm TB: {self.diemTB:.2f}"

    def xep_loai(self):
        if self.diemTB >= 8:
            return "Giỏi"
        elif self.diemTB >= 6.5:
            return "Khá"
        elif self.diemTB >= 5:
            return "Trung bình"
        else:
            return "Yếu"


def main():
    ds_sinh_vien = []

    n = int(input("Nhập số lượng sinh viên: "))
    for i in range(n):
        print(f"\n--- Sinh viên {i+1} ---")
        ten = input("Nhập tên: ")
        tuoi = int(input("Nhập tuổi: "))
        diem = float(input("Nhập điểm trung bình: "))
        ds_sinh_vien.append(SinhVien(ten, tuoi, diem))

    print("\n=== Danh sách sinh viên và xếp loại ===")
    for sv in ds_sinh_vien:
        print(sv.hien_thi(), "| Xếp loại:", sv.xep_loai())


if __name__ == "__main__":
    main()
