from src.Text_Summarizer.logging import logger
from src.Text_Summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} competed <<<<<<<<\n\nx=================x")

except Exception as e:
    logger.exception(e)
    raise e