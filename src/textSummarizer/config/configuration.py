from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directory
from textSummarizer.entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig, ModelEvaluationConfig, ModelTrainerConfig

class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        
        # Tüm yapılandırma dosyaları için ortak kök dizini oluştur
        create_directory([self.config.artifacts_root])

    def get_config(self, config_type: str):
        # config_type parametresi ile hangi yapılandırmanın çağrılacağını belirler
        config = getattr(self.config, config_type)
        params=self.params.TrainingArguments
        # Yapılandırmanın root dizinini oluştur
        create_directory([config.root_dir])

        # config_type türüne göre ilgili sınıf örneğini döndür
        if config_type == 'data_ingestion':
            return DataIngestionConfig(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir
            )
        elif config_type == 'data_validation':
            return DataValidationConfig(
                root_dir=config.root_dir,
                STATUS_FILE=config.STATUS_FILE,
                ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
            )
        elif config_type == 'data_transformation':
            return DataTransformationConfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
                tokenizer_name=config.tokenizer_name
            )
        
        elif config_type == 'model_training':

            return  ModelTrainerConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt = config.model_ckpt,
            num_train_epochs = params.num_train_epochs,
            warmup_steps = params.warmup_steps,
            per_device_train_batch_size = params.per_device_train_batch_size,
            weight_decay = params.weight_decay,
            logging_steps = params.logging_steps,
            evaluation_strategy = params.evaluation_strategy,
            eval_steps = params.evaluation_strategy,
            save_steps = params.save_steps,
            gradient_accumulation_steps = params.gradient_accumulation_steps
        )

        elif config_type == 'model_evaluation':


         return  ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path = config.model_path,
            tokenizer_path = config.tokenizer_path,
            metric_file_name = config.metric_file_name
           
        )
        else:
            raise ValueError(f"Unsupported config type: {config_type}")
