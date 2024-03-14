import argparse

def main():
    parser = argparse.ArgumentParser(description='Collect 5 chunks of data')
    parser.add_argument('data', nargs=5, type=str, help='Enter 5 chunks of data')
    args = parser.parse_args()

    print("Collected data:")
    for chunk in args.data:
        print(chunk)

if __name__ == "__main__":
    main()
