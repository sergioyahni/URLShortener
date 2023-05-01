# URLShortener

This app was created with the help of ChatGPT and then it was retouched for redundant code. 

## Endpoints

POST
{
  "original_url": YOUR_URL
}

Returns
{
  "original_url": YOUR_URL,
   "short_url": RANDOM_6_DIGITS_URL
}

GET /RANDOM_6_DIGITS_URL
