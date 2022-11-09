from _old.languages import *
import json

locale = {}

for index, target in enumerate(['it', 'en', 'fr']):
    for i in dictionary_.keys():
        locale[i] = dictionary_[i][index]

    locale['align_o'] = align_o[index]
    locale['direction_'] = direction_[index]
    locale['set_COM_port'] = set_COM_port[index]
    locale['save_arduino_code'] = save_arduino_code[index]
    locale['set_calibration_params_'] = set_calibration_params_[index]
    locale['openImg_'] = openImg_[index]
    locale['saveCanvas_'] = saveCanvas_[index]
    locale['menu_'] = menu_[index]
    locale['windows_'] = windows_[index]
    locale['loading_'] = loading_[index]
    locale['error_msg'] = error_msg[index]
    locale['sub_windows_'] = sub_windows_[index]

    with open(fr'assets/locale/{target}.json', 'w') as outfile:
        json.dump(locale,
                  outfile,
                  sort_keys=False,
                  indent=4
                  )
