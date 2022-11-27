import iris_analysis
import iris_analysis.io
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("output_file")

args = parser.parse_args()

if __name__ == "__main__":
    col_names, data = iris_analysis.io.load_csv(args.input_file)
    stats= iris_analysis.calculate_stats(data)
    iris_analysis.io.save_csv(args.output_file, [col_names]+stats)
