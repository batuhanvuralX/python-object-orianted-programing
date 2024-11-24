import json 
class Person:

    def __init__(self, name, surname, age, address, nationality):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address
        self.nationality = nationality
        

    def personİnform(self):
        return print(f"İsim: {self.name}, Soyad: {self.surname}, Yaşınız: {self.age}, Adres: {self.address}, Uyruk: {self.nationality}")



class personJob(Person):
    def __init__(self, name, surname, age, address, nationality,jobtitle,company):
        super().__init__(name, surname, age, address, nationality)
        self.jobtitle = jobtitle
        self.company = company
    def jobDiatisel(self):
        return print(f"İşiniz : {self.jobtitle}, Çalıştığınız şirket {self.company}")


class organization(personJob):
    def __init__(self, name, surname, age, address, nationality, jobtitle, company,department,hierarchy):
        super().__init__(name, surname, age, address, nationality, jobtitle, company)
        self.department = department
        self.hierarchy = hierarchy

    def organizasyonDiatiles(self):
        return print(f"Departmanım: {self.department}, Seviye: {self.hierarchy}")
    

    def save_to_json(self, filename = "user_info.json"):
        data = {
            "name" : self.name,
            "surname" : self.surname,
            "age" : self.age,
            "adress" : self.address,
            "nationality" : self.nationality,
            "jobtitel" : self.jobtitle,
            "company" : self.company,
            "department" : self.department,
            "hierarchy" : self.hierarchy
        }
        with open(filename, "a", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False,indent=2)



while True:

    print("Merhaba CV kayıt programına hoşgeldiniz...")


    try:
        userChoice = int(input("""Yeni kayıt girmek veya tekrardan girmek için 1 tuşuna basınız...
    Programdan çıkmak için 2 tuşuna basınız...
                            """))
    except ValueError:
        print("Yanlış değer girdiniz")
        continue

    if userChoice == 1:


        name = input("Adınızı giriniz: ")
        surname = input("Soyadınızı giriniz: ")
        age = input("Yaşınızı giriniz: ")
        address = input("Adresinizi giriniz: ")
        nationality = input("Uyruk bilginizi giriniz: ")

        jobtitle = input("Mesleğinizi giriniz")
        company = input("Çalışıyorsanız şirketinizi giriniz")


        department = input("Şirketinizin hangi departmanında görevlisiniz ? (çalışıyorsanız)")
        hierarchy = input("Mesleki seviyeniz nedir ?")

        person_instance = organization(name,surname,age,address,nationality,jobtitle,company,department,hierarchy)


        person_instance.personİnform()
        person_instance.jobDiatisel()
        person_instance.organizasyonDiatiles()
        person_instance.save_to_json()
        print("dosya kayıt edildi")

    elif userChoice == 2:
        print("Hoşçakalın...")
        break
    else:
        print("Yanlış bir işlem yaptınız tekrar deneyin")
        continue

