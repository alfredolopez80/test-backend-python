
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
