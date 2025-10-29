"""
Milestone 1 - Complete Pipeline Execution
Data Collection and Preprocessing for AlOCR Project

This script runs the complete Milestone 1 pipeline:
1. Data Collection and Validation
2. Advanced Image Preprocessing  
3. Azure AI Document Intelligence Preparation
"""

import os
import sys
import logging
import argparse
from datetime import datetime

# Add scripts to path
sys.path.append('scripts')

from data_collection import DataCollector
from advanced_preprocessing import ImagePreprocessor
from azure_prep import AzureDocumentPrep

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'logs/milestone1_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def print_header():
    """Print pipeline header."""
    print("\n" + "=" * 80)
    print(" " * 20 + "AlOCR PROJECT - MILESTONE 1")
    print(" " * 15 + "Data Collection and Preprocessing")
    print("=" * 80 + "\n")


def print_separator(title: str):
    """Print section separator."""
    print("\n" + "-" * 80)
    print(f"  {title}")
    print("-" * 80 + "\n")


def run_data_collection():
    """Run data collection module."""
    print_separator("STEP 1: DATA COLLECTION AND VALIDATION")
    try:
        logger.info("Starting data collection...")
        collector = DataCollector()
        catalog_df = collector.collect_documents()
        logger.info(f"Data collection completed. {len(catalog_df)} documents cataloged.")
        return True, catalog_df
    except Exception as e:
        logger.error(f"Data collection failed: {e}")
        return False, None


def run_preprocessing():
    """Run preprocessing module."""
    print_separator("STEP 2: ADVANCED IMAGE PREPROCESSING")
    try:
        logger.info("Starting image preprocessing...")
        preprocessor = ImagePreprocessor()
        results_df = preprocessor.preprocess_batch()
        logger.info(f"Preprocessing completed. {len(results_df)} images processed.")
        return True, results_df
    except Exception as e:
        logger.error(f"Preprocessing failed: {e}")
        return False, None


def run_azure_prep():
    """Run Azure preparation module."""
    print_separator("STEP 3: AZURE AI DOCUMENT INTELLIGENCE PREPARATION")
    try:
        logger.info("Starting Azure preparation...")
        azure_prep = AzureDocumentPrep()
        results_df = azure_prep.prepare_for_azure()
        config_path = azure_prep.generate_azure_batch_config()
        logger.info(f"Azure preparation completed. {len(results_df)} images validated.")
        logger.info(f"Batch config generated: {config_path}")
        return True, results_df
    except Exception as e:
        logger.error(f"Azure preparation failed: {e}")
        return False, None


def generate_final_report(collection_success, preprocessing_success, azure_success):
    """Generate final milestone report."""
    print_separator("MILESTONE 1 - FINAL SUMMARY")
    
    report_path = "data/validation_reports"
    os.makedirs(report_path, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = os.path.join(report_path, f"milestone1_final_report_{timestamp}.txt")
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("MILESTONE 1 - FINAL EXECUTION REPORT\n")
        f.write("Data Collection and Preprocessing for AlOCR Project\n")
        f.write("=" * 80 + "\n\n")
        
        f.write(f"Execution Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("PIPELINE EXECUTION STATUS\n")
        f.write("-" * 80 + "\n")
        f.write(f"1. Data Collection & Validation:    {'[COMPLETED]' if collection_success else '[FAILED]'}\n")
        f.write(f"2. Advanced Preprocessing:           {'[COMPLETED]' if preprocessing_success else '[FAILED]'}\n")
        f.write(f"3. Azure Preparation:                {'[COMPLETED]' if azure_success else '[FAILED]'}\n\n")
        
        all_success = collection_success and preprocessing_success and azure_success
        f.write(f"Overall Status: {'[MILESTONE 1 COMPLETED]' if all_success else '[PARTIALLY COMPLETED]'}\n\n")
        
        f.write("DELIVERABLES\n")
        f.write("-" * 80 + "\n")
        f.write("[+] Raw data validated and cataloged\n")
        f.write("[+] Document metadata extracted\n")
        f.write("[+] Images preprocessed with quality checks\n")
        f.write("[+] Azure-compatible images prepared\n")
        f.write("[+] Batch configuration generated\n")
        f.write("[+] Comprehensive reports generated\n\n")
        
        f.write("OUTPUT DIRECTORIES\n")
        f.write("-" * 80 + "\n")
        f.write("  data/metadata/             - Document catalogs and metadata\n")
        f.write("  data/preprocessed/         - Preprocessed images\n")
        f.write("  data/azure_ready/          - Azure-compatible images\n")
        f.write("  data/validation_reports/   - Validation and execution reports\n")
        f.write("  logs/                      - Pipeline execution logs\n\n")
        
        f.write("NEXT STEPS (MILESTONE 2)\n")
        f.write("-" * 80 + "\n")
        f.write("1. Set up Azure AI Document Intelligence credentials\n")
        f.write("2. Implement OCR extraction using Azure API\n")
        f.write("3. Implement document verification logic\n")
        f.write("4. Build fraud detection models\n")
        f.write("5. Create API endpoints for document processing\n")
    
    logger.info(f"Final report saved to: {report_file}")
    
    # Print summary to console
    print("\n" + "=" * 80)
    print("MILESTONE 1 EXECUTION SUMMARY")
    print("=" * 80)
    print(f"Data Collection:    {'[+] Success' if collection_success else '[-] Failed'}")
    print(f"Preprocessing:      {'[+] Success' if preprocessing_success else '[-] Failed'}")
    print(f"Azure Preparation:  {'[+] Success' if azure_success else '[-] Failed'}")
    print("-" * 80)
    
    all_success = collection_success and preprocessing_success and azure_success
    if all_success:
        print("[+] MILESTONE 1 COMPLETED SUCCESSFULLY!")
    else:
        print("[!] MILESTONE 1 PARTIALLY COMPLETED - Review logs for details")
    
    print(f"\nFinal Report: {report_file}")
    print("=" * 80 + "\n")
    
    return all_success


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description='Run Milestone 1 Pipeline - Data Collection and Preprocessing'
    )
    parser.add_argument(
        '--skip-collection',
        action='store_true',
        help='Skip data collection step (use existing catalog)'
    )
    parser.add_argument(
        '--skip-preprocessing',
        action='store_true',
        help='Skip preprocessing step (use existing processed images)'
    )
    parser.add_argument(
        '--skip-azure',
        action='store_true',
        help='Skip Azure preparation step'
    )
    
    args = parser.parse_args()
    
    # Create necessary directories
    os.makedirs('logs', exist_ok=True)
    
    # Print header
    print_header()
    
    # Track execution status
    collection_success = True
    preprocessing_success = True
    azure_success = True
    
    try:
        # Step 1: Data Collection
        if not args.skip_collection:
            collection_success, _ = run_data_collection()
            if not collection_success:
                logger.error("Data collection failed. Aborting pipeline.")
                sys.exit(1)
        else:
            logger.info("Skipping data collection (--skip-collection)")
        
        # Step 2: Preprocessing
        if not args.skip_preprocessing:
            preprocessing_success, _ = run_preprocessing()
            if not preprocessing_success:
                logger.error("Preprocessing failed. Continuing with remaining steps...")
        else:
            logger.info("Skipping preprocessing (--skip-preprocessing)")
        
        # Step 3: Azure Preparation
        if not args.skip_azure:
            azure_success, _ = run_azure_prep()
            if not azure_success:
                logger.error("Azure preparation failed.")
        else:
            logger.info("Skipping Azure preparation (--skip-azure)")
        
        # Generate final report
        all_success = generate_final_report(
            collection_success,
            preprocessing_success,
            azure_success
        )
        
        if all_success:
            logger.info("[+] Milestone 1 completed successfully!")
            sys.exit(0)
        else:
            logger.warning("[!] Milestone 1 completed with some failures")
            sys.exit(1)
            
    except KeyboardInterrupt:
        logger.info("\nPipeline interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
