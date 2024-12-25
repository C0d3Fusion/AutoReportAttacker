
# Proxy Attack Tool

This is a Python-based tool designed for attacking profiles or videos on a platform using proxies. It supports both proxy fetching from the internet or loading them from a local file. The tool is designed for use in Termux (Android's terminal emulator) environment.

## Features:
- **Proxy Management:** Automatically fetch proxies from the internet or load from a file.
- **Profile Reporting:** Attack a user profile by reporting it.
- **Video Reporting:** Attack a video by reporting it.
- **Multithreading:** The tool performs attacks concurrently for faster execution.
- **Automatic Proxy Handling:** Proxies are validated and used for the attack.

## Requirements:
- Python 3.x
- Termux (Android Terminal Emulator)

## Installation Instructions for Termux:

### Step 1: Install Python and Required Packages
Open Termux and run the following commands:

```bash
pkg update
pkg upgrade
pkg install python
pkg install git
pip install requests
pip install colorama
```

### Step 2: Clone the Repository
Clone this repository to your Termux environment using the following command:

```bash
git clone https://github.com/C0d3Fusion/AutoReportAttacker.git
cd AutoReportAttacker
```

### Step 3: Install Dependencies
Install the necessary Python libraries by running:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Script
Run the script with the following command:

```bash
python main.py
```

### Step 5: Follow the Prompts
- The script will ask if you want to use proxies. You can choose to gather proxies from the internet or load them from a file.
- Then, you will be prompted to choose between reporting a profile or a video.
- Provide the necessary information (username for profile attack or video URL for video attack).

The script will then execute and perform the report requests using the proxies.

## Usage Example:

1. **Choose Proxy Option:**
   - **Yes:** Fetch proxies from the internet.
   - **No:** Run without proxies.

2. **Choose Attack Method:**
   - **1 - Report Profile:** Attack a user profile.
   - **2 - Report Video:** Attack a video.

3. **Enter Required Information:**
   - Username (for profile attack) or video URL (for video attack).

The script will execute and perform the report requests using the proxies.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer:
This tool is intended for educational and testing purposes only. Unauthorized use of this tool may be illegal. Please ensure that you have permission to use this tool for testing purposes.
