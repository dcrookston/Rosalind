import re

#A class representing a single gene

class gene:

    def __init__(self, name, form="base", species="", notes=""):
        self.name = name
        self.ccount = 0
        self.gcount = 0
        self.acount = 0
        self.tcount = 0
        self.length = 0
        self.bases = ""
        self.species = species
        self.notes = notes

        form = form.lower()
        if(form in {"amino", "base"}):
            self.form = form
        else:
            raise ValueError("'form' argument must be 'base' or 'amino'")

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Gene named " + self.name

    def percent_gc(self):
        if (self.length == 0):
            return 0
        return ((self.ccount + self.gcount) / self.length) * 100

    def percent_at(self):
        if (self.length == 0):
            return 0
        return ((self.acount + self.tcount) / self.length) * 100

    def add_bases(self, bases:str):
        #Strip whitespace
        bases = bases.strip()

        #Make sure 'bases' only contains ACTGs
        if (re.match("^[ACTGURYKMSWBDHVN-]+$", bases) is None):
            raise ValueError("Parameter 'bases' must contain only standard "
                             + "IUB/IUPAC codes.")
        
        self.bases += bases
        self.ccount += bases.count("C")
        self.gcount += bases.count("G")
        self.acount += bases.count("A")
        self.tcount += bases.count("T")
        self.length += len(bases)
