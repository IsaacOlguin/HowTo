import evaluate

print(evaluate.load('exact_match').compute(references=['hello'], predictions=['hello']))
