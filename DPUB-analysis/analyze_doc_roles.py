
import os

import re

from collections import defaultdict

from pathlib import Path



# Define the base path

base_path = r"c:\Users\kersc\Documents\Git\Hello-World\DPUB-analysis"
folders = ["Bosses", "Emergency", "Essentials", "Minimalism"]

# Data structure to hold results
results = {}

for folder in folders:
    results[folder] = {
        "roles": defaultdict(list),
        "elements": defaultdict(int),
        "total_count": 0
    }

# Regex to extract role attribute and surrounding element
# This will capture the full element tag and the role value
role_pattern = re.compile(r'<(\w+)[^>]*role="(doc-[^"]*)"[^>]*>', re.IGNORECASE)

def get_all_xhtml_files(folder_path):
    """Recursively get all .xhtml files in a folder"""
    xhtml_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.xhtml'):
                xhtml_files.append(os.path.join(root, file))
    return xhtml_files

# Process each folder
for folder in folders:
    folder_path = os.path.join(base_path, folder)
    
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        continue
    
    xhtml_files = get_all_xhtml_files(folder_path)
    
    for file_path in xhtml_files:
        relative_path = os.path.relpath(file_path, folder_path)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            matches = role_pattern.findall(content)
            
            for element, role in matches:
                results[folder]["total_count"] += 1
                results[folder]["elements"][element] += 1
                
                # Store role with file info
                results[folder]["roles"][role].append({
                    "file": relative_path,
                    "element": element
                })
                
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

# Generate markdown report
report = "# DPUB Role Analysis Report\n\n"
report += "Analysis of `role=\"doc-\"` attributes in XHTML files across the DPUB-analysis folders.\n\n"

for folder in folders:
    if results[folder]["total_count"] == 0:
        continue
    
    report += f"## {folder}\n\n"
    report += f"**Total count: {results[folder]['total_count']} occurrences**\n\n"
    
    # Report by elements
    report += "### Elements Used\n\n"
    for element in sorted(results[folder]["elements"].keys()):
        count = results[folder]["elements"][element]
        report += f"- `<{element}>`: {count} occurrences\n"
    
    report += "\n### Role Types\n\n"
    
    # Sort roles by count (descending) then by name
    sorted_roles = sorted(results[folder]["roles"].items(), 
                         key=lambda x: (-len(x[1]), x[0]))
    
    for role, occurrences in sorted_roles:
        count = len(occurrences)
        report += f"#### `role=\"{role}\"`\n"
        report += f"**Count: {count}**\n\n"
        
        # Group by element
        elements_used = {}
        for occ in occurrences:
            elem = occ["element"]
            if elem not in elements_used:
                elements_used[elem] = []
            elements_used[elem].append(occ["file"])
        
        for elem in sorted(elements_used.keys()):
            report += f"- Element: `<{elem}>`\n"
            report += f"  - Files ({len(elements_used[elem])} occurrences):\n"
            for file in sorted(list(set(elements_used[elem]))):
                report += f"    - {file}\n"
        
        report += "\n"
    
    report += "\n---\n\n"

# Write report to file
output_file = os.path.join(base_path, "DOC_ROLES_REPORT.md")
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(report)

print(f"Report generated: {output_file}")
print(f"\nSummary:")
for folder in folders:
    total = results[folder]["total_count"]
    if total > 0:
        print(f"  {folder}: {total} occurrences")
