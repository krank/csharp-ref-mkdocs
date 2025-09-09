# Function to generate the nav.yml file from the SUMMARY.md file
# and return the list of chapters and titles
# param: bool skip_private: skip private pages

# Import the required modules
import re, os

def generate_nav(skip_private=False):

    # Define a regular expression to match the links in the SUMMARY.md file
    # Collect indentation size, title and link
    pattern = re.compile(r"^(\s*)\*\s*\[([^\]]+)\]\(([^\)]+)\)( p)?")

    # Define the nav.yml data structure
    nav = ["nav:"]

    # Check if SUMMARY.md exists
    if not os.path.isfile("SUMMARY.md"):
        print("... SUMMARY.md not found")
        return None

    # Read the lines from SUMMARY.md file
    with open("SUMMARY.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

        # Parse the lines and add the information to the nav.yml data structure
        for line in lines:

            # If lines stat with ##, it is a chapter
            if line.startswith("## "):
                chapter = line[3:].strip()
                nav.append("  - \'{}\':".format(chapter))
                continue

            # If lines start with *, it is a title and link
            match = pattern.match(line)
            if match:
                indent = match.group(1)
                title = match.group(2)
                link = match.group(3)
                private = match.group(4)

                # If private page and skip_private is True, skip this page
                if private and skip_private:
                    continue
                
                # If link ends with READMD.md and next line is more indented, it is a subchapter
                if link.endswith("README.md") and lines[lines.index(line) + 1].startswith(indent + "  "):
                    nav.append("    {}- \'{}\':".format(indent, title))
                    nav.append("      {}- \'{}\': {}".format(indent, title, link))
                    continue
                nav.append("    {}- \'{}\': {}".format(indent, title, link))

    # Return the nav.yml data structure and the list of chapters and titles
    return "\n".join(nav)