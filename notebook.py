import json
import os

FILENAME = "notes.json"

def load_notes():
    """讀取記事本內容，若檔案不存在則回傳空列表"""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

def save_notes(notes):
    """將記事存入 JSON 檔案"""
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4, ensure_ascii=False)

def add_note():
    """新增記事"""
    notes = load_notes()
    content = input("請輸入記事內容: ")
    notes.append({"id": len(notes) + 1, "content": content})
    save_notes(notes)
    print("✅ 記事已新增！")

def view_notes():
    """顯示所有記事"""
    notes = load_notes()
    if not notes:
        print("📂 記事本是空的！")
    else:
        for note in notes:
            print(f"📌 [{note['id']}] {note['content']}")

def delete_note():
    """刪除指定 ID 的記事"""
    notes = load_notes()
    view_notes()
    try:
        note_id = int(input("請輸入要刪除的記事 ID: "))
        notes = [note for note in notes if note["id"] != note_id]
        save_notes(notes)
        print("🗑️ 記事已刪除！")
    except ValueError:
        print("❌ 請輸入有效的數字 ID！")

def main():
    while True:
        print("\n=== 📝 簡易記事本 ===")
        print("1️⃣ 新增記事")
        print("2️⃣ 查看記事")
        print("3️⃣ 刪除記事")
        print("4️⃣ 離開")
        choice = input("請選擇操作: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("👋 再見！")
            break
        else:
            print("⚠️ 無效選擇，請重新輸入！")

if __name__ == "__main__":
    main()
