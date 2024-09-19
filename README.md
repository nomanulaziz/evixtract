# EvixTract

EvixTract is a modular digital forensics tool designed to assist investigators in acquiring, imaging, and analyzing storage devices. It supports additional functions like metadata extraction, network traffic capture, and log analysis to streamline digital forensic investigations.

## Features
- **Data Acquisition**: Capture raw data from a storage device using the `dd` command.
- **Disk Imaging**: Create an exact forensic image of a storage device.
- **Filesystem Analysis**: List and recover files from the disk image.
- **Metadata Extraction**: Extract file metadata (e.g., creation, modification, and access times).
- **Network Packet Capture**: Capture network traffic and analyze suspicious packets.
- **Log Analysis**: Scan system logs for suspicious activities based on predefined patterns.

## Installation

### Step 1: Install Python
Make sure you have Python 3.x installed on your system.
`sudo apt update`
`sudo apt install python3`

### Step 2: Install Dependencies
1.	Clone this repository:
  - `git clone https://github.com/nomanulaziz/email_sage.git`
  - `cd email_sage`
2.	Install the required dependencies:
  - `pip install -r requirements.txt`

### Step 3: Run the Application
You can run the main application using the following command:
`python evixtract.py –help`


## Commands
To use different features of EvixTract, refer to the following commands:
-	**Acquire Data From a Device:**
  `python evixtract.py --acquire --device mydisk.dd --output test.img`
-	**Create a Disk Image:**
  `python evixtract.py --imaging --device mydisk.dd --output forensic.img`

-	**Analyze the Filesystem:**
  `python evixtract.py --analyze --input output.img`

-	**Extract Metadata:**
  `python evixtract.py --extract-metadata --input output.img`

-	**Capture Network Packets:**
  `python evixtract.py --capture --packet-count 10 --packet-output capture.pcap`

-	**Analyze System Logs:**
  `python evixtract.py --log-analysis --log-file syslog.log --output suspicious_logs.txt`

-	**Full Workflow:**
  `python evixtract.py --acquire --device mydisk.dd --output test.img --imaging --analyze --extract-metadata`
