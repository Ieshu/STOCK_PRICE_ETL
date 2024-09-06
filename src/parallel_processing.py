from multiprocessing import Pool
from src.extract import extract_stock_data

def parallel_extract(api_list):
    with Pool(len(api_list)) as pool:
        results = pool.map(extract_stock_data, api_list)
    return results

if __name__ == "__main__":
    parallel_extract(["AAPL", "GOOGL", "AMZN"])  # Example stock symbols
