import timeit
from rabin_karp_search import rabin_karp_search
from kmp_search import kmp_search
from boyer_moore_search import boyer_moore_search

def search_in_file(file_path, pattern, search_algorithm):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        chunk_size = 1024 * 1024
        offset = 0
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            search_algorithm(chunk, pattern)

            offset += len(chunk)

def main():

    first_article_file_path = './task_3/data/article_1.txt'
    first_article_exist_pattern = 'це бібліотека, що доступна в усіх реалізаціях'
    first_article_not_exist_pattern = 'цього тексту не існує і ніколи не буде існувати'

    second_article_file_path = './task_3/data/article_2.txt'
    second_article_exist_pattern = 'публікацій. У наш час існує багато різних'
    second_article_not_exist_pattern = 'цього тексту не існує і ніколи не буде існувати'

    print("First article performance tests >>>")
    rabin_karp_search_execution_time = timeit.timeit(lambda: search_in_file(first_article_file_path, first_article_exist_pattern, rabin_karp_search), number=10)
    print(f"Execution time for Rabin-Karp algorithm: {rabin_karp_search_execution_time:.6f} seconds in first article. With exists search pattern.")

    kmp_search_execution_time = timeit.timeit(lambda: search_in_file(first_article_file_path, first_article_exist_pattern, kmp_search), number=10)
    print(f"Execution time for Knuth-Morris-Pratt algorithm: {kmp_search_execution_time:.6f} seconds in first article. With exists search pattern.")

    boyer_moore_search_execution_time = timeit.timeit(lambda: search_in_file(first_article_file_path, first_article_exist_pattern, boyer_moore_search), number=10)
    print(f"Execution time for Boyer-Moore algorithm: {boyer_moore_search_execution_time:.6f} seconds in first article. With exists search pattern.")

    print("*"*100)

    rabin_karp_search_execution_time = timeit.timeit(lambda: search_in_file(first_article_file_path, first_article_not_exist_pattern, rabin_karp_search), number=10)
    print(f"Execution time for Rabin-Karp algorithm: {rabin_karp_search_execution_time:.6f} seconds in first article. With not exists search pattern.")

    kmp_search_execution_time = timeit.timeit(lambda: search_in_file(first_article_file_path, first_article_not_exist_pattern, kmp_search), number=10)
    print(f"Execution time for Knuth-Morris-Pratt algorithm: {kmp_search_execution_time:.6f} seconds in first article. With not exists search pattern.")

    boyer_moore_search_execution_time = timeit.timeit(lambda: search_in_file(first_article_file_path, first_article_not_exist_pattern, boyer_moore_search), number=10)
    print(f"Execution time for Boyer-Moore algorithm: {boyer_moore_search_execution_time:.6f} seconds in first article. With not exists search pattern.")



    print("\nSecond article performance tests >>>")
    rabin_karp_search_execution_time = timeit.timeit(lambda: search_in_file(second_article_file_path, second_article_exist_pattern, rabin_karp_search), number=10)
    print(f"Execution time for Rabin-Karp algorithm: {rabin_karp_search_execution_time:.6f} seconds in first article. With exists search pattern.")

    kmp_search_execution_time = timeit.timeit(lambda: search_in_file(second_article_file_path, second_article_exist_pattern, kmp_search), number=10)
    print(f"Execution time for Knuth-Morris-Pratt algorithm: {kmp_search_execution_time:.6f} seconds in first article. With exists search pattern.")

    boyer_moore_search_execution_time = timeit.timeit(lambda: search_in_file(second_article_file_path, second_article_exist_pattern, boyer_moore_search), number=10)
    print(f"Execution time for Boyer-Moore algorithm: {boyer_moore_search_execution_time:.6f} seconds in first article. With exists search pattern.")

    print("*"*100)

    rabin_karp_search_execution_time = timeit.timeit(lambda: search_in_file(second_article_file_path, second_article_not_exist_pattern, rabin_karp_search), number=10)
    print(f"Execution time for Rabin-Karp algorithm: {rabin_karp_search_execution_time:.6f} seconds in first article. With not exists search pattern.")

    kmp_search_execution_time = timeit.timeit(lambda: search_in_file(second_article_file_path, second_article_not_exist_pattern, kmp_search), number=10)
    print(f"Execution time for Knuth-Morris-Pratt algorithm: {kmp_search_execution_time:.6f} seconds in first article. With not exists search pattern.")

    boyer_moore_search_execution_time = timeit.timeit(lambda: search_in_file(second_article_file_path, second_article_not_exist_pattern, boyer_moore_search), number=10)
    print(f"Execution time for Boyer-Moore algorithm: {boyer_moore_search_execution_time:.6f} seconds in first article. With not exists search pattern.")

if __name__ == "__main__":
    main()