First app using Flask that is experimenting with API calls and accessing data within those structures

Implemented multiprocessing on API calls to speed up response time. Initially I had one call after another which took 25.08 seconds to return all 151 pokemon from generation 1. After implementing multiprocessing the same aPI call took 3.5 seconds. You can test the response spee in the 'time.py' file.

Search function returns a single card with whatever pokemon you searched for