import logging
logging.basicConfig(
    filename="script.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_script_execution():
    try:
        logging.info("Script execution started.")
        logging.info("Performing task...")
        result = 10 / 2  
        logging.info(f"Task completed successfully. Result: {result}")
    except Exception as e:
        logging.error(f"Error occurred: {e}")
    finally:
        logging.info("Script execution finished.")

log_script_execution()