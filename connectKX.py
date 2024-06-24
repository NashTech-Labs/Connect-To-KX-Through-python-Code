from qpython import qconnection
from qpython.qtype import QException
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Kx connection details
kx_host = 'your_kx_host'
kx_port = 5001  # Replace with your KDB+ port
kx_username = 'your_username'  # If authentication is required
kx_password = 'your_password'  # If authentication is required

def connect_to_kx():
    try:
        # Establish connection to Kx
        with qconnection.QConnection(host=kx_host, port=kx_port, username=kx_username, password=kx_password) as q:
            q.open()
            logger.info("Connected to Kx successfully")

            # Run a sample query
            query = 'count select from kxsSensor where extSmpID like ""'
            result = q(query)
            logger.info(f"Query result: {result}")
            
            return result
    except QException as e:
        logger.error(f"QException occurred: {e}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == '__main__':
    connect_to_kx()
