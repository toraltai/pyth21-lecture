# def func():
#     a = "func"
#     def inner_func():
#         a = "inner_func"
#         print(locals())
#     inner_func()
#     print(locals())
# func()
# print(globals())

# def foo():
#     var = 'переменная foo'
  
#     def bar():
#         global var
#         var = 'переменная bar'
 
#     bar()
#     print('переменная в foo: ', var)    
# foo()
# print('переменная в foo: ', var)

# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}

# def age_control():
#     global a
#     a = [f"{k}, Вы можете войти в клуб" if v >= 17 else f'{k}, извините, Вы не проходите по age-control' for k,v in list(a.items())]
#     for i in a:
#         print(i)
#     # for k,v in a.items():
    #     if v < 17:
    #         print(f'{k}, извините, Вы не проходите по age-control')
    #     else:
    #         print(f'{k}, Вы можете войти в клуб')

# age_control()
dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
 'Nik': {'history': 84, 'math': 85, 'literature': 87}}
dict_ = {key: in_k for key,value in dict_.items() for in_k, in_v in value.items() if in_v == max(value.values())}
# for k,v in dict_.items():
#     for in_k, in_v in v.items():
#         if in_v == max(v.values()):
#             print(k,in_v)
print(dict_)