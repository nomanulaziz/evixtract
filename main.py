import argparse
import os
import sys

from acquire import acquire_data
from imaging import create_image
from analysis import analyze_filesystem
from metadata_xtract import extract_metadata
from log_analyzer import analyze_logs 
from capture_packets import capture_packets, analyze_packets, save_packets_to_file

def parse_arguments():
    parser = argparse.ArgumentParser(description="Data Acquisition and Imaging Tool")
    parser.add_argument('--acquire', action='store_true', help="Acquire data from device")
    parser.add_argument('--imaging', action='store_true', help="Create a disk image of device")
    parser.add_argument('--analyze', action='store_true', help="Analyze file system of a disk image")
    parser.add_argument('--extract-metadata', action='store_true', help="Extract metadata from files within the device")
    parser.add_argument('--log-analysis', action='store_true', help="Perform log analysis")
    parser.add_argument('--log-file', type=str, help="Path to the log file to analyze")
    parser.add_argument('--device', type=str, nargs='?', help="Device path (e.g., /dev/sda)")  # Optional argument
    parser.add_argument('--output', type=str, help="Output file (e.g., image.dd)")
    parser.add_argument('--input', type=str, help="Input file (e.g., syslogs.logs)")
    parser.add_argument('--capture', action='store_true', help="Capture network packets")
    parser.add_argument('--packet-count', type=int, default=50, help="Number of packets to capture")
    parser.add_argument('--packet-output', type=str, default="capture.pcap", help="File to save captured packets")
    
    
    return parser.parse_args()

def main():
    args = parse_arguments()

    if args.acquire:
        if not args.device:
            print("Error: Device path must be specified with --acquire.")
            sys.exit(1)
        acquire_data(args.device, args.output)
    elif args.imaging:
        if not args.device:
            print("Error: Device path must be specified with --imaging.")
            sys.exit(1)
        create_image(args.device, args.output)
    elif args.analyze:
        # Analyze filesystem using the image file path
        analyze_filesystem(args.input)
    elif args.extract_metadata:
        # Extract metadata using the image file path
        file_paths = analyze_filesystem(args.input)  # You may need to modify this to match your actual usage
        for file_path in file_paths:
            metadata = extract_metadata(args.input)
            print(f"Metadata for {file_path}:")
            print(f"            {metadata}")
            print("")
    elif args.log_analysis:
        if not args.log_file or not args.output:
            print("Error: Both --log-file and --output must be specified with --log-analysis.")
            sys.exit(1)
        log_analysis_result = analyze_logs(args.log_file, args.output)
        print(log_analysis_result)
        
    elif args.capture:
        packets = capture_packets(filter_rule="tcp", packet_count=args.packet_count)
        save_packets_to_file(packets, filename=args.packet_output)
        analyze_packets(packets)
        
        
    else:
        print("Please specify one of the following options: --acquire, --imaging, --analyze, --extract-metadata, --log-analysis or --capture.")

if __name__ == '__main__':
    main()
