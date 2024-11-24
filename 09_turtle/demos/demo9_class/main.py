import module1
import module2

#call function in module
module1.sayMyName()

#create class PrintLater of module1
pl = module1.PrintLater("test")
pl.doThePrint()

#create class AnotherExample of module2
ae = module2.AnotherExample(2, 3)
result = ae.magicCalc(5)
print(result)
