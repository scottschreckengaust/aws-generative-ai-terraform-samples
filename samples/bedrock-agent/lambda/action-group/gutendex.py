#
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance
# with the License. A copy of the License is located at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# or in the 'license' file accompanying this file. This file is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, express or implied. See the License for the specific language governing permissions
# and limitations under the License.
#

import requests

def get_books_from_gutendex(n: int) -> dict:
    """Return the count and first n books from the /books API."""
    api_url = "https://gutendex.com"
    response = requests.get(api_url + "/books", timeout=44) # keep a little less than the Lambda timeout
    response.raise_for_status()
    books = response.json()
    return {"count": books["count"], "books": books["results"][:n]}
