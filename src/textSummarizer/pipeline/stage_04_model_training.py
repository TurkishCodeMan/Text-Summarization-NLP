from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.config.configuration import ConfigurationManager


class ModelTrainingPipeline:

    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config_manager = ConfigurationManager()
            data_transformation_config = config_manager.get_config('model_training')
            data_transformation = ModelTrainer(config=data_transformation_config)
            data_transformation.train()

        except Exception as e:
            raise e
