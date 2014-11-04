"""Command file to execute greengraph"""

from argparse import ArgumentParser
from greengraph import greengraph

def process():
   parser = ArgumentParser(description = "Run Greengraph between given cities")

   parser.add_argument('start_city')
   parser.add_argument('end_city')
   parser.add_argument('steps')

   arguments= parser.parse_args()
   
   greengraph(arguments.start_city, arguments.end_city, arguments.steps)


if __name__ == "__main__":
    process()

