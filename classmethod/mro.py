# class A:
#     def __init__(self,name):
#         self.name = name
#     def callName(self):
#         print(f"A : {self.name}")

# class B(A):
#     def __init__(self,name):
#         self.name = name
#     def callName(self):
#         print(f"B : {self.name}")

# class C(A):
#     def __init__(self,name):
#         self.name = name
#     def callName(self):
#         print(f"C : {self.name}")

# class D(B,A):
#     pass
    

# print(D.mro())
# # for met in D.mro():
# #     for m in met.mro():
# #         print(m)
# d = D("Tom")
# d.callName()


class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,A):  # ❌ Conflict in MRO
    pass

print(D.mro())  # Will raise an error!
