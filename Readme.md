# Python Fast API rest-api-test-backend-minimum-time-to-remove-all-cars-containing-illegal-goods

## Description

Problem
You are given a **0-indexed** binary string s which represents a sequence of train cars. s[i] = '0' denotes that the ith car does **not** contain illegal goods and s[i] = '1' denotes that the ith car does contain illegal goods.
As the train conductor, you would like to get rid of all the cars containing illegal goods. You can do any of the following three operations any number of times:

1. Remove a train car from the **left** end (i.e., remove s[0]) which takes 1 unit of time.
2. Remove a train car from the **right** end (i.e., remove s[s.length - 1]) which takes 1 unit of time.
3. Remove a train car from **anywhere** in the sequence which takes 2 units of time.
   Return the **minimum** time to remove all the cars containing illegal goods.
   Note that an empty sequence of cars is considered to have no cars containing illegal goods.
   Examples:

### 1

INPUT: s = "1100101"
OUTPUT: 5
EXPLANATION:
One way to remove all the cars containing illegal goods from the sequence is to
● removeacarfromtheleftend2times.Timetakenis2*1=2.
● remove a car from the right end. Time taken is 1.
● remove the car containing illegal goods found in the middle. Time taken is 2.
This obtains a total time of 2 + 1 + 2 = 5.
An alternative way is to
● removeacarfromtheleftend2times.Timetakenis2*1=2.
● removeacarfromtherightend3times.Timetakenis3\*1=3.
This also obtains a total time of 2 + 3 = 5.
5 is the minimum time taken to remove all the cars containing illegal goods. There are no other ways to remove them with less time.

### 2

INPUT: s = "0010"
OUTPUT: 2
EXPLANATION:
One way to remove all the cars containing illegal goods from the sequence is to

● removeacarfromtheleftend3times.Timetakenis3\*1=3. This obtains a total time of 3.

Another way to remove all the cars containing illegal goods from the sequence is to
● remove the car containing illegal goods found in the middle. Time taken is 2.

This obtains a total time of 2.

Another way to remove all the cars containing illegal goods from the sequence is to
● removeacarfromtherightend2times.Timetakenis2\*1=2.

This obtains a total time of 2.

2 is the minimum time taken to remove all the cars containing illegal goods. There are no other ways to remove them with less time.

### Solutions

```python
import os
from fastapi import Body, FastAPI
import ptvsd

"""
Enable remote debugging
"""
if os.getenv('ENVIRONMENT') != 'PROD':
  ptvsd.enable_attach()

app = FastAPI()


@app.get("/")
def read_root():
  return "API for Getting minimum time to remove all cars containing illegal goods"

@app.post("/test/")
async def test(request: str = Body(...)):
	s: str = request.split("=",2)[1]
	n = len(s)
	if n <= 0:
		return "Error: String can't be empty"
	if n > (200000 - (n-1)):
		return "Error: String length can't be greater than 200000 bits"
	ans = n
	left = 0  # Min time to remove illegal cars so far

	for i, c in enumerate(s):
		if c != '1' and c != '0':
			return "Error: String can only contain 1's and 0's"
		left = min(left + (ord(c) - ord('0')) * 2, i + 1)
		ans = min(ans, left + n - 1 - i)

	return ans

```

### Constraints

-   1 <= s.length <= 2 \* (10^5)
-   s[i] is either '0' or '1'.

## Running the code

You should have docker and docker compose installed. When starting the application will search for a `.env` file. If you don't have one you can copy the `development.env` as a base.

To start you development environment just run :

```sh
  docker-compose up
```

Or if you want to run the container in detached mode:

```sh
  docker-compose up -d
```

To stop it:

```sh
  docker-compose down
```
