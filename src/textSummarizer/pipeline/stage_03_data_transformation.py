from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.config.configuration import ConfigurationManager


class DataTransformationTrainingPipeline:

    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config_manager = ConfigurationManager()
            data_transformation_config = config_manager.get_config('data_transformation')
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()

        except Exception as e:
            raise e
