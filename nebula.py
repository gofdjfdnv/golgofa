def func1(arg1, arg2):
    var27 = func2(arg2, arg1)
    if arg2 < arg1:
        var32 = class6()
    else:
        var32 = class8()
    for var33 in xrange(23):
        var32.func7(arg2, var33)
    var51 = func10(arg1, var27)
    var52 = var27 | var27
    result = arg1 ^ var27
    return result
def func10(arg34, arg35):
    var36 = 688121956 ^ 641 & (-1609770271 - 554)
    var37 = ((arg34 - -208) - 937197089) - var36
    var38 = (860 & var36) & var37
    var39 = ((var38 + var38) | var38) - arg35
    var40 = arg34 ^ var37 & (-99990295 & -995)
    var41 = var38 ^ var36
    var42 = var40 + var38
    var43 = var37 ^ arg35
    if var36 < arg35:
        var44 = arg34 | var37
    else:
        var44 = (arg35 ^ (var38 | var43)) - var43
    var45 = (arg35 + -383852257) ^ (var37 | var42)
    var46 = arg34 | 1591420479
    if var38 < var41:
        var47 = var43 & var36 + var40 | var42
    else:
        var47 = var41 ^ var40 & var36 ^ 1952116323
    var48 = var43 - var39
    if arg35 < var38:
        var49 = arg35 ^ arg34 + var43 | var38
    else:
        var49 = var39 ^ var37
    var50 = arg35 - var42
    result = (var38 & ((var45 & var48 ^ (var46 ^ var37) ^ var37) | 164)) ^ var41 | var50
    return result
class class8(object):
    def func7(self, arg30, arg31):
        return 0
class class6(object):
    def func7(self, arg28, arg29):
        return 0
def func2(arg3, arg4):
    var5 = 0
    for var26 in func3(arg4, var5):
        var5 += -4 | arg4
    return var5
def func4(arg8, arg9):
    var14 = func5(arg9, arg8)
    result = 768236328 - -246764241 ^ var14 + (var14 - -1926861975)
    return result
def func5(arg10, arg11):
    var12 = 0
    for var13 in range(40):
        var12 += (arg10 & arg11) - var12
    return var12
def func3(arg6, arg7):
    var15 = func4(-387, arg6)
    yield var15
    var16 = (954 + (arg7 & arg6)) - -921048717
    yield var16
    var17 = arg6 ^ var16 | arg7 ^ var16
    yield var17
    var18 = -1022584625 | (arg6 & var16 | var17)
    yield var18
    var19 = var16 ^ -641
    yield var19
    var20 = 959 - var16 | arg7
    yield var20
    var21 = var17 - var18 ^ var17 & var17
    yield var21
    var22 = (-943574219 - 421765795) + -1932302469 + var16
    yield var22
    var23 = var16 - (arg7 & 1206356391 & 609)
    yield var23
    var24 = var19 ^ (arg6 | -473 - var20)
    yield var24
    var25 = var19 & (var22 ^ var23) ^ var20
    yield var25
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 53'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
