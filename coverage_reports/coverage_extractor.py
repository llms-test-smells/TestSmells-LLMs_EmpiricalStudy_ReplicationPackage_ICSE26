import argparse
from modules.extractors.java_extractor import JavaCoverageExtractor
from modules.extractors.python_extractor import PythonCoverageExtractor

def extract_coverage(language, source_path, output_path):
    if language == "java":
        extractor = JavaCoverageExtractor()
    elif language == "python":
        extractor = PythonCoverageExtractor()
    else:
        raise ValueError(f"Unsupported language: {language}")

    extractor.extract(source_path, output_path)

def main():
    parser = argparse.ArgumentParser(description="Extract test coverage reports")
    parser.add_argument("--language", required=True, choices=["java", "python"], help="Programming language")
    parser.add_argument("--source", required=True, help="Path to the source coverage report")
    parser.add_argument("--output", required=True, help="Path to the output CSV folder")

    args = parser.parse_args()
    extract_coverage(args.language, args.source, args.output)

if __name__ == "__main__":
    main()
