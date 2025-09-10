#!/usr/bin/python3

import re
import os

name_trim_pattern = re.compile(r"^(##?|\*) ")
name_sub_pattern = re.compile(
    r"\[(?P<title>.*)\]\((?:(?P<path>.*)/)?(?P<filename>.*.md)\)")

#FIXME: For som reason all subchapters aren't added to base node's list

def parse(yml_dict: dict[str, list[str]], lines: list[str], current_line: int, current_indent: int):
    current_title = name_trim_pattern.sub("", lines[current_line].strip())

    title_data = name_sub_pattern.match(current_title)
    if (title_data != None and title_data.group('path') != None):
        current_title = title_data.group('path') + "/.nav.yml"

    # print(f"  Starting the '{current_title}' section")
    yml_dict[current_title] = []
    if title_data != None:
      if title_data.group('filename') == "README.md":
        yml_dict[current_title].append("README.md")
    current_line += 1

    while current_line < len(lines):
        line = lines[current_line].rstrip()

        if len(line.strip()) == 0:
            current_line += 1
            continue

        line_trimmed = name_trim_pattern.sub("", line.strip())
        line_indent = int(1 + (len(line) - len(line.strip())) / 2)
        line_data = name_sub_pattern.match(line_trimmed)

        # Is this the start of a new ## section?
        if (line.startswith("## ") and current_indent == 0):
            yml_dict[current_title].append(line_trimmed)
            (yml_dict, current_line, current_indent) = parse(
                yml_dict, lines, current_line, current_indent + 1)

        elif ((line.startswith("## ") or line.startswith("***")) and current_indent > 0):
            # print(f"  Ending the '{current_title}' section")
            current_indent = 1
            return (yml_dict, current_line-1, current_indent-1)

        if (line.lstrip().startswith("* ")):
            if (line_indent > current_indent and current_indent > 0):
                current_indent = line_indent
                # print(f"  Increased indent to {current_indent}")

                (yml_dict, current_line, current_indent) = parse(
                    yml_dict, lines, current_line-1, current_indent)
                continue

            if (line_indent < current_indent and current_indent > 0):
                current_indent = line_indent
                # print(f"  Decreased indent to {current_indent}")
                return (yml_dict, current_line, current_indent)

            
            if (line_data != None and line_data.group('filename') != None):
                if (line_data.group('filename') == "README.md" and line_data.group('path') != None):
                    last_segment = line_data.group('path').split('/')[-1]
                    yml_dict[current_title].append(last_segment)
                else:
                    yml_dict[current_title].append(line_data.group('filename'))
            else:
                yml_dict[current_title].append(line_trimmed)

        current_line += 1

    return (yml_dict, current_line, current_indent-1)


def make_navyml(summary_filename):

    if not os.path.isfile(summary_filename):
        print("... SUMMARY.md not found")
        return None

    with open(summary_filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

        yml_dict = {}

        (yml_dict, current_line, current_indent) = parse(yml_dict, lines, 0, 0)

        for key in yml_dict.keys():
          print("# " + key)
          for line in yml_dict[key]:
            print("     > " + line);

        # for line in lines:
        # For each line
        # If indent is same, just add it to current yml
        # If increased indent; the previous line was a directory


make_navyml('_csharp_ref_old/SUMMARY.md')
