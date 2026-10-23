import logging
import time
from functools import wraps
logger = logging.getLogger("api")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
screen = logging.StreamHandler()
screen.setFormatter(formatter)
file_handler = logging.FileHandler("api.log")
file_handler.setFormatter(formatter)
logger.addHandler(screen)
logger.addHandler(file_handler)
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        logger.info("%s took %.3f seconds", func.__name__, time.time() - start)
        return result
    return wrapper

def log_io(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug("Input: %s %s", args, kwargs)
        result = func(*args, **kwargs)
        logger.debug("Output: %s", result)
        return result
    return wrapper

def need_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user["role"] != role:
                logger.warning("%s is not allowed", user["name"])
                raise PermissionError("Access denied")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@log_io
@timer
@need_role("admin")
def delete_user(user, username):
    return username + " deleted"

admin = {"name": "Ali", "role": "admin"}
guest = {"name": "Sara", "role": "guest"}

print(delete_user(admin, "bilal"))
try:
    delete_user(guest, "zara")
except PermissionError:
    logger.error("Guest request blocked")
print(delete_user.__name__)     
