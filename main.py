from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformaion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig,DataTransformationConfig
import sys

if __name__ == '__main__':
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info('Initiate data ingestion')
        
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info('Data initiation completed')
        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(data_ingestion_artifact,data_validation_config)
        logging.info('initiate data validation')
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info('Data validation completed')
        print(data_validation_artifact)
        logging.info('data transformation started')
        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        data_transformation = DataTransformaion(data_validation_artifact, data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_validation_artifact)
        logging.info('data transformation completed')
    except Exception as e:
        raise NetworkSecurityException(e,sys)
