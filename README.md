# vPlates-Number-Plate-Checker

### Automatically check the availability of vehicle plate combinations on vplates.com.au. It utilizes `cloudscraper` to bypass web scraping restrictions and makes concurrent requests to efficiently handle large numbers of plate combinations. The script reads proxies and combinations from two text files (`proxies.txt` and `combinations.txt`), checks each combination using a unique proxy, and stores successful results in a `success.txt` file.

## Features
- Proxy Rotation: Utilizes a list of proxies to randomize and assign a proxy for each request, minimizing detection and avoiding rate limits.
- Concurrency: Leverages Python’s ThreadPoolExecutor to check multiple plate combinations in parallel, significantly improving performance.\
- Customizable: Allows easy modification of proxy lists, combinations, and request intervals through external text files and configuration changes.

## Prerequisites
Before running the project, ensure you have the following installed:
- Python 3.x
- cloudscraper

## Installation
1. Clone the repository
```bash
git clone https://github.com/christiancheng15/vPlates-Number-Plate-Checker.git
cd vPlates-Number-Plate-Checker
```

2. Install the necessary prerequisites
```bash
pip install -r requirements.txt
```

## Usage
1. Add proxies in `proxies.txt`. Ensure proxies are in the format: `ip:port:username:password`.
2. Add combinations to check for in `combinations.txt`. Ensure combinations have a max length of 6 alphanumeric (both numbers and digits are allowed) characters.
3. Running the script
```bash
python main.py
```

## Output
The script will load the proxy and combinations data from `proxies.txt` and `combinations.txt`, respectively. It will then proceed to check the availability of each combination against the vPlates API, using a unique proxy for each request to avoid rate limiting and detection. Proxies are rotated by randomly selecting one from the list for each request. If the proxy is not working, a new one will be selected until a working one is found.

The output will be logged in the terminal, and successful combinations will be appended to `success.txt`. Below is an example of how this output might look:
```
[INFO] Loaded 100 proxies from proxies.txt
[INFO] Loaded 1000 combinations from combinations.txt
[SUCCESS] ABC123
[SUCCESS] OIASJS
[SUCCESS] AIHUSD
[SUCCESS] 981238
[SUCCESS] 128387
```

## Troubleshooting
- Proxy Timeouts: Ensure that the proxies in `proxies.txt` are active and valid. It is preferred to use residential proxies.

## Contributing
Contributions are welcome! If you have ideas for new features or improvements, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact
For any questions or inquires, please contact [christiancheng15](https://github.com/christiancheng15/).