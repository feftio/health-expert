from experta import *
import sys


class Personne(Fact):
    """Info about the patient"""
    pass


def SUMFIELDS(p, *fields):
    return sum([p.get(x, 0) for x in fields])


class InreferenceEngine(KnowledgeEngine):


    @Rule(
        Personne(age=P(lambda x: x <= 5))
        )
    def concerned_person(self):
        self.declare(Fact(concerned=True))


    @Rule(
        Fact(concerned=True),
        Personne(glycemie=MATCH.glycemie)
        )
    def hyper_glycemy(self, glycemie):
        if glycemie > 10:
            self.declare(Fact(hyperglycemic_risk=True))
            print("Warning! High blood sugar.")
        else:
            self.declare(Fact(hyperglycemic_risk=False))


    @Rule(
        Fact(concerned=True),
        Personne(glycemie=MATCH.glycemie)
        )
    def hypo_glycemy(self, glycemie):
        if glycemie < 4:
            print("Warning! Low blood sugar.")
            self.declare(Fact(hypoglycemic_risk=True))
        else:
            self.declare(Fact(hypoglycemic_risk=False))


    @Rule(
        Fact(concerned=True),
        AS.p << Personne(),
        TEST(lambda p: SUMFIELDS(p, 'shakiness', 'hunger', 'sweating', 'headach', 'pale') > 2)
        )
    def has_signs_low_sugar(self, p):
        self.declare(Fact(has_signs_low_sugar=True))


    @Rule(
        Fact(concerned=True),
        Fact(has_diabetic_parents=True),
        Fact(has_signs_low_sugar=True)
        )
    def protocole_risk_low(self):
        print("Warning! Child could be diabetic.")


    @Rule(
        Fact(concerned=True),
        Fact(hypoglycemic_risk=True),
        Fact(has_signs_low_sugar=True)
        )
    def protocole_alert_low(self):
        print("Alert! High risk of diabetes, you must see a doctor.")


    @Rule(
        Fact(concerned=True),
        Personne(diabetic_parents=True)
        )
    def has_diabetic_parents(self):
        self.declare(Fact(has_diabetic_parents=True))


    @Rule(
        Fact(concerned=True),
        AS.p << Personne(),
        TEST(lambda p: SUMFIELDS(p, 'urination', 'thirst', 'blurred_vision', 'headach', 'dry_mouth', 'smelling_breath', 'shortness_of_breath') > 2)
        )
    def has_signs_high_sugar(self, **_):
        self.declare(Fact(has_signs_high_sugar=True))


    @Rule(
        Fact(concerned=True),
        Fact(has_diabetic_parents=True),
        Fact(has_signs_high_sugar=True)
        )
    def protocole_risk_high(self):
        print("Warning! Child could be diabetic.")


    @Rule(
        Fact(concerned=True),
        Fact(hyperglycemic_risk=True),
        Fact(has_signs_high_sugar=True)
        )
    def protocole_alert_high(self):
        print("Alert! High risk of diabetes, you must see a doctor.")


engine = InreferenceEngine()
engine.reset()
engine.declare(Personne(age=2,
                        glycemie=11,
                        shakiness= False,
                        hunger= False,
                        sweating= False,
                        headach= False,
                        diabetic_parents = True,
                        pale= False,
                        urination = True,
                        thirst = True,
                        blurred_vision = False,
                        dry_mouth = True,
                        smelling_breath = False,
                        shortness_of_breath = False,
                        ))
engine.run()