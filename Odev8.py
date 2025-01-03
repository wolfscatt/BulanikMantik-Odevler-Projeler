from simpful import *
FS = FuzzySystem()

S_1 = FuzzySet(points=[[0., 1.],  [1., 1.], [1.5, 0.]], term="low_flow")
S_2 = FuzzySet(points=[[0.5, 0.], [1.5, 1.], [2.5, 1.], [3., 0.]], term="medium_flow")
S_3 = FuzzySet(points=[[2., 0.],  [2.5, 1.], [3., 1.]], term="high_flow")
FS.add_linguistic_variable("OXI", LinguisticVariable([S_1, S_2, S_3], concept="Oksijen"))

FS.plot_variable("OXI",element=0.51)

FS.set_crisp_output_value("LOW_POWER", 0)
FS.set_crisp_output_value("MEDIUM_POWER", 25)
FS.set_output_function("HIGH_FUN", "OXI**2")

print("\n--------------------------------------------")
print("OXI->low_flow member degree:",S_1.get_value(0.51))
print("OXI->medium_flow member degree:",S_2.get_value(0.51))
print("OXI->high_flow member degree:",S_3.get_value(0.51))

R1 = "IF (OXI IS low_flow) THEN (POWER IS LOW_POWER)"  # 0.1 üyelik derecesi gelir, k=0
R2 = "IF (OXI IS medium_flow) THEN (POWER IS MEDIUM_POWER)" # 0.010000000000000009 üyelik derecesi gelir, k=25
R3 = "IF (OXI IS medium_flow) OR (OXI IS high_flow) THEN (POWER IS HIGH_FUN)"  # 0.0 üyelik derecesi gelir, k=OXI**2 = 0.51**2 = 0.2601
FS.add_rules([R1, R2, R3])

FS.set_variable("OXI",0.51)

print(FS.Sugeno_inference(["POWER"]))


# Algoritmanın verdiği sonuç = 0.2476480392156865
# Benim hesap makinesi ile bulduğum sonuç = 0,26