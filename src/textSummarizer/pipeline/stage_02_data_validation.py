from textSummarizer.components.data_validation import DataValidation
from textSummarizer.config.configuration import ConfigurationManager


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):

        try:
            config_manager = ConfigurationManager()
            data_validation_config = config_manager.get_config('data_validation')

            # data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.all_files_exist()

        except Exception as e:
            raise e
