
import view, model


def start():
    a = view.inputData('первое')
    model.set_first(a)
    while True:
        oper = view.inputOperator()
        if oper == '=': break
        b = view.inputData('второе')
        model.set_second(b)
        model.set_result(oper)
        result = model.get_result()
        if result == None:
            view.devision_by_zero()
            break
        first = model.get_first()
        second = model.get_second()
        view.outputResult(first, second, oper, result)
        view.print_window(result)
        model.set_first(result)
        







