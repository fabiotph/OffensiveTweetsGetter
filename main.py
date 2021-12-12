import sys
import twitter_api
import queue
import csv_writer
import log_writer

def generate_message_log(exact):
        if exact:
            return'Query: "{}", Count: {}/{}, Finished: {}\n'
        return 'Query: {}, Count: {}/{}, Finished: {}\n'

'''
    example:
    python main.py "seu viado" 100
'''
if __name__ == "__main__":
    query = sys.argv[1]
    total_results = int(sys.argv[2])
    exact = False if len(sys.argv) > 3 and (sys.argv[3] == 'false' or sys.argv[3] == 'False') else True
    finished = False
    next_token = None
    responses_queue = queue.Queue()
    csv_writer.write_csv_parallel(responses_queue, query)

    while total_results >= 0 and not finished:
        max_results = 100
        if total_results >= 10 and total_results < 100:
            max_results = total_results
        elif total_results < 10:
            max_results = 10
        
        response = twitter_api.get_tweets(query, exact=exact, max_results=max_results, next_token_page=next_token)
        response_meta = response['meta']
        if 'data' in response:
            response = response['data']
        else:
            log_writer.write_log_parallel(generate_message_log(exact).format(query, int(sys.argv[2]) - total_results, sys.argv[2], '{}, OBS: Sem resultados'.format(finished)), console_print=True)
            break
        total_results -= int(response_meta['result_count'])
        if not 'next_token' in response_meta or not total_results > 0:
            finished = True
        else:
            next_token = response_meta['next_token']
        responses_queue.put_nowait(response)
        log_writer.write_log_parallel(generate_message_log(exact).format(query, int(sys.argv[2]) - total_results, sys.argv[2], finished), console_print=True)
    responses_queue.put(None)
