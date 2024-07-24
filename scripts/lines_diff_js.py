xml_file_1 = "bench/xml/run-2-grammarinator+mutations-fast-xml-parser/coverage/clover.xml"
xml_file_2 = "bench/xml/run-2-gmutator-fast-xml-parser/coverage/clover.xml"

import xml.etree.ElementTree as ET

def parse_coverage(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    coverage_data = {}

    # Iterate through each package
    for package in root.findall(".//package"):
        # Iterate through each file in the package
        for file in package.findall("file"):
            file_name = file.get("name")
            covered_lines = set()

            # Iterate through each line in the file
            for line in file.findall("line"):
                line_num = int(line.get("num"))
                count = int(line.get("count"))

                # If the line is covered (count > 0), add it to the set
                if count > 0:
                    covered_lines.add(line_num)

            # Add the file and its covered lines to the dictionary
            if file_name in coverage_data:
                coverage_data[file_name].update(covered_lines)
            else:
                coverage_data[file_name] = covered_lines

    return coverage_data

def find_unique_lines(coverage1, coverage2):
    unique_coverage = {}

    all_files_1 = coverage1.keys()
    all_files_2 = list(coverage2.keys())
    #print("file count 1", len(list(all_files_1)))
    #print("file count 2", len(list(all_files_2)))
    i = 0
    for file in all_files_1:
        lines1 = coverage1.get(file, set())
        lines2 = coverage2.get(all_files_2[i], set())
        i+=1
        #print("lines1", lines1)
        #print("lines2", lines2)
        unique_coverage[file] = lines1 - lines2
        print("file name: ", file)
        print("unique_coverage lines1", unique_coverage[file])

    return unique_coverage

def count_unique_lines(unique_coverage):
    return {file: len(lines) for file, lines in unique_coverage.items()}

# Example usage
#xml_file_1 = "path_to_your_first_xml_file.xml"
#xml_file_2 = "path_to_your_second_xml_file.xml"

coverage_data_1 = parse_coverage(xml_file_1)
coverage_data_2 = parse_coverage(xml_file_2)

#print("\ncoverage_data_1: ", coverage_data_1)
#print("\n\ncoverage_data_2: ", coverage_data_2)

uniq_lines_run_1 = find_unique_lines(coverage_data_1, coverage_data_2)
uniq_lines_run_2 = find_unique_lines(coverage_data_2, coverage_data_1)

unique_counts1 = count_unique_lines(uniq_lines_run_1)
unique_counts2 = count_unique_lines(uniq_lines_run_2)

total_unique_lines_1 = 0
total_unique_lines_2 = 0

print("Unique lines covered by coverage1 but not by coverage2:")
for file, count in unique_counts1.items():
    print(f'{file}: {count} unique lines')
    total_unique_lines_1 += count

print("\nUnique lines covered by coverage2 but not by coverage1:")
for file, count in unique_counts2.items():
    print(f'{file}: {count} unique lines')
    total_unique_lines_2 += count

print()
print("total_unique_lines_1: ", total_unique_lines_1)
print("total_unique_lines_2: ", total_unique_lines_2)