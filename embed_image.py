#!/usr/bin/env python3
"""
Run this script ONCE from your repo folder.
It will embed jonathan-hale.png as base64 directly into about.html and project-detail.html
so the image works on GitHub Pages without needing a separate image file.

Usage:
    python3 embed_image.py
"""
import base64, os, sys

# Files to update
files_to_update = ["about.html", "project-detail.html"]

# Check jonathan-hale.png exists
if not os.path.exists("jonathan-hale.png"):
    print("ERROR: jonathan-hale.png not found in current directory.")
    print("Please save the Jonathan Hale portrait as jonathan-hale.png in this folder first.")
    sys.exit(1)

# Read and encode the image
with open("jonathan-hale.png", "rb") as f:
    img_data = f.read()

b64 = base64.b64encode(img_data).decode("utf-8")
data_url = f"data:image/png;base64,{b64}"

print(f"Image encoded: {len(img_data):,} bytes -> {len(b64):,} base64 chars")

# Replace in each file
for filename in files_to_update:
    if not os.path.exists(filename):
        print(f"SKIPPED: {filename} not found")
        continue
    
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    count = content.count("jonathan-hale.png")
    content = content.replace("jonathan-hale.png", data_url)
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"UPDATED: {filename} ({count} image reference(s) replaced)")

print("\nDone! You can now delete jonathan-hale.png if you like.")
print("The image is now embedded directly in the HTML files.")
