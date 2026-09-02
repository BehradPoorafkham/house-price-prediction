def timer(f):
    def wrapper(*args, **kwargs):
        import time
        start =  time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start}")
        return result
    return wrapper

def logging_API(f):
    def wrapper():
        print("call_API started...")
        result = f()
        print("call_APi finished.")
        return result
    return wrapper

def logging_database(f):
    def wrapper():
        result = f()
        print("database divar created.")
        return result
    return wrapper

def logging_ads(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        print("ads generated.")
        return result
    return wrapper

def logging_data(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        print("data inserted into table ads.")
        return result
    return wrapper

def logging_csv(f):
    def wrapper():
        result = f()
        print("csv file created.")
        return result
    return wrapper