class Contacts:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def print_info(self):
        print("=============")
        print("이름 : ", self.name)
        print("전화번호 : ", self.phone)
        print("이메일 : ", self.email)
        print("주소 : ", self.address)
        print("=============")

    @staticmethod
    def set_contact():
        name = input("이름 : ")
        phone = input("전화번호 : ")
        email = input("이메일 : ")
        address = input("주소 : ")
        contact = Contacts(name, phone, email, address)
        return contact

    @staticmethod
    def get_contacts(contacts_list):
        print("==연락처출력==")
        for i in contacts_list:
            i.print_info()

    @staticmethod
    def delete(contact_list, name):
        for i, t in enumerate(contact_list):
            if t.name == name:
                del contact_list[i]

    @staticmethod
    def print_menu():
        print("1. 연락처 입력")
        print("2. 연락처 출력")
        print("3. 연락처 삭제")
        print("4. 종료")
        menu = input("메뉴선택 : ")
        return int(menu)

    @staticmethod
    def run():
        contacts_list = []

        while 1:
            menu = Contacts.print_menu()
            if menu == 1 :
                contacts_list.append(Contacts.set_contact())
            elif menu == 2 :
                print(contacts_list.__len__())
                Contacts.get_contacts(contacts_list)
            elif menu == 3 :
                name = input("삭제할 이름 : ")
                Contacts.delete(contacts_list, name)
            elif menu == 4 :
                break
