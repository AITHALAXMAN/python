# multi path to cross check whether the student is elig for acadamics or not

class student:
    def name(self):
        print("name...")
class ap(student):
    def ac(self):
        print("acadamic score 90% and above")
class ece(student):
    def eces(self):
        print("ece score 60% and above")
class result(ap, ece):
    def e(self):
        print('*****minimum eligibility to apply****')
        self.ac()
        self.eces()



r= result()
r.e()