from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# from textSummarizer.pipeline.stage_02_data_preprocessing import DataPreprocessingStage
# from textSummarizer.pipeline.stage_03_feature_extraction import FeatureExtractionStage
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

from textSummarizer.logging import logger

STAGE_NAME="Data Validation Stage"

try:
    logger.info(f"Starting {STAGE_NAME}...")
    data_stage=DataValidationTrainingPipeline()
    data_stage.main()
    logger.info(f"{STAGE_NAME} completed successfully.")
except Exception as e:
    logger.exception(f"{STAGE_NAME} failed with error: {e}")
    raise e