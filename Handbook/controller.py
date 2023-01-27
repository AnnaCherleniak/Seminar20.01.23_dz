import view
import operation
import log

def button_click():
    some_str = view.inp_mod()
    if some_str == 'импорт':
        surname = view.inp_import()
        result = operation.import_data(surname)
        view.view_import(result)
        log.log_cash(some_str, result)
    elif some_str == 'экспорт':
        some_list = view.inp_export()
        operation.export_data(some_list)
        view.view_export()
        log.log_cash(some_str, some_list)