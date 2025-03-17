import sys

# 加入 Notebook 資料夾到模組搜尋路徑
sys.path.append(r"C:\Users\p10368226\Documents\Python\side_project\Notebook")

# 匯入 mtn_notebook 模組
import mtn_notebook as mtn

def main():

    mtn.main()

    # while True:
    #     print("\n=== 📝 簡易記事本 ===")
    #     print("1️⃣ 新增記事")
    #     print("2️⃣ 查看記事")
    #     print("3️⃣ 刪除記事")
    #     print("4️⃣ 離開")
    #     choice = input("請選擇操作: ")

    #     if choice == "1":
    #         mtn.add_note()
    #     elif choice == "2":
    #         mtn.view_notes()
    #     elif choice == "3":
    #         mtn.delete_note()
    #     elif choice == "4":
    #         break
    #     else:
    #         print("❌ 請輸入有效的選項！")

    # print("📚 結束記事本！")

if __name__ == "__main__":
    main()

    