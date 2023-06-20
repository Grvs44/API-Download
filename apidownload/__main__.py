from argparse import ArgumentParser
from . import ApiDownload

def main():
    parser = ArgumentParser(
        prog='apidownload',
        description='Read the Pronouns.page file from stdin',
    )
    parser.add_argument('path', default='.', nargs='?',
                        help='Provide an alternative directory or file')
    args = parser.parse_args()
    ApiDownload(args.path).run()

if __name__ == '__main__':
    main()
