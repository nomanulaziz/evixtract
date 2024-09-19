import re
import argparse

def analyze_logs(log_file, output_file):
    """
    Analyze a log file to find lines that match suspicious patterns and save them to an output file.
    
    :param log_file: Path to the log file
    :param output_file: Path to save the suspicious log entries
    """
    # Define regex patterns for suspicious activities
    search_patterns = [
        r'failed',         # Detect 'failed' (e.g., failed login)
        r'error',          # Detect error messages
        r'CRITICAL',       # Detect critical issues
        r'unexpected',     # Detect unexpected activities
        r'authentication failure',  # Authentication failure messages
        r'Failed password',  # Specific to SSH failed login attempts
        r'Denied',  # Permission denied messages
        r'Bad protocol',  # Protocol errors (often network-related)
        r'iptables denied',  # Unauthorized firewall access
        r'Connection refused',  # Connection refusal due to unauthorized access
        r'connection attempt',  # Attempts to connect to a service
        r'DDOS',  # Denial of Service attack attempts
        r'SYN flood',  # SYN flood attack (common DDoS attack)
        r'port scan',  # Indications of port scanning
        r'deleted',  # Files deleted unexpectedly
        r'renamed',  # File renaming (could indicate tampering)
        r'Permission denied',  # Unauthorized file access
        r'File changed',  # Detect file modification or changes
        r'changed permissions',  # Suspicious changes to file permissions
        r'unexpected file creation',  # Files being created without user knowledge
        r'suspected malware',  # If logs report malware detection
        r'system compromised',  # Indicators of system compromise
        r'sshd: \[preauth\]',  # Pre-authentication stage in SSH
        r'too many authentication failures',  # Multiple failed login attempts (possible brute force)
        r'Accepted password',  # SSH login success (useful for monitoring)
        r'key too large',  # Indicates an attack using large SSH keys
    ]

    try:
        with open(log_file, 'r') as file:
            logs = file.readlines()

        suspicious_logs = []
        for line in logs:
            for pattern in search_patterns:
                if re.search(pattern, line):
                    suspicious_logs.append(line)
                    break  # Move to the next line once a match is found

        if suspicious_logs:
            with open(output_file, 'w') as out_file:
                out_file.write(f"Suspicious activities found in {log_file}:\n")
                for log in suspicious_logs:
                    out_file.write(log)

            return(f"Suspicious activities found and saved to {output_file}.")
        else:
            return(f"No suspicious activities found in {log_file}.")

    except FileNotFoundError:
        return(f"Error: The log file {log_file} does not exist.")
    except Exception as e:
        return(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Analyze logs for suspicious activities.")
    parser.add_argument("log_file", help="Path to the log file to analyze")
    parser.add_argument("output_file", help="Path to the output file to save suspicious logs")

    # Parse arguments
    args = parser.parse_args()

    # Call the log analysis function
    analyze_logs(args.log_file, args.output_file)

