websites=["amazon", "flipkart", "paytm"]
extension=("org", "com", "in")
for web in websites:
    for ext in extension:
        print("www."+ web + "." + ext)