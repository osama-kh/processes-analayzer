import requests
from api_key import *

def scan_file(file_path):
    print("start analayzing")
    api_key = get_key()
    url = "https://www.virustotal.com/vtapi/v2/file/scan"

    params = {"apikey": api_key}
    files = {"file": (file_path, open(file_path, "rb"))}

    response = requests.post(url, files=files, params=params)
    scan_json = response.json()

    # Get the file's hash from the scan response
    file_hash = scan_json["md5"]

    # Send a request to VirusTotal to get a report on the file
    report_url = "https://www.virustotal.com/vtapi/v2/file/report"
    report_params = {"apikey": api_key, "resource": file_hash}
    report_response = requests.get(report_url, params=report_params)
    report_json = report_response.json()

    # Check the number of antivirus scanners that detected the file as malicious
    if report_json["positives"] > 0:
        return "Virus"
    else:
        return "Clean"


results = scan_file("cores/core.885")
print(results)
