import logging

from models.observable import Observable


class CalibrationModel:
    def __init__(self, parent):
        self.parent = parent

        self.calibration_params = Observable({})

    def get_calibration_params(self) -> dict:
        """
        Get calibration paramathers from the settings variable.
        If settings are not avaiable, he set a default dict.
        """
        logging.debug(f"CalibrationModel")
        if not self.calibration_params.get():
            settings = self.parent.get_settings()

            self.calibration_params.set(
                settings['calibration']
                if settings['calibration'] is not None else
                {
                    'UP': 155,
                    'DOWN': 129,
                    'X': 1,
                    'Y': 1
                }
            )

        logging.debug(self.calibration_params.get())
        return self.calibration_params.get()

    def set_calibration_params(self, data: dict) -> dict:
        """
        Set calibration paramethers after being modified by user from View.

        Perform a data validation.
        Raise 'ValueError' if data are out of permitted ranges.
        """
        logging.debug(f"CalibrationModel:{data}")
        if (
            (data['UP'] < 180) and (data['DOWN'] < 180) and
            (data['UP'] > 0) and (data['DOWN'] > 0)
        ):
            data['X'] = (
                1
                if data['X'] == self.parent.locale.get()['direction_'][0] else
                -1
            )
            data['Y'] = (
                1
                if data['Y'] == self.parent.locale.get()['direction_'][0] else
                -1
            )
            settings = self.parent.settings.get()
            settings['calibration'] = data
            self.parent.settings.set(settings)
            self.calibration_params.set(data)

        else:
            raise ValueError("Errore nei dati inseriti")
        return self.calibration_params.get()
