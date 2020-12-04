import re

class PassportChecker:

    def __init__(self, passport):
        self.passport = passport

    def byr(self):
        byr = int(self.passport['byr'])
        if 1920 <= byr <= 2002:
            return True
        return False

    def iyr(self):
        iyr = int(self.passport['iyr'])
        if 2010 <= iyr <= 2020:
            return True
        return False

    def eyr(self):
        eyr = int(self.passport['eyr'])
        if 2020 <= eyr <= 2030:
            return True
        return False

    def hgt(self):
        hgt = self.passport['hgt']
        if hgt[-2:] == 'in':
            if 59 <= int(hgt[:-2]) <= 76:
                return True
        if hgt[-2:] == 'cm':
            if 150 <= int(hgt[:-2]) <= 193:
                return True
        return False
    
    def hcl(self):
        hcl = self.passport['hcl']
        if re.match('^(#[0-9a-fA-F]{6})$', hcl):
            return True
        return False

    def ecl(self):
        ecl = self.passport['ecl']
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if any([sub in ecl for sub in colors]):
            return True
        return False

    def pid(self):
        pid = self.passport['pid']
        if re.match('^([0-9]{9})$', pid):
            return True
        return False

    def testAll(self):
        tests = [self.byr,self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid]
        result = [f() for f in tests]
        return result
