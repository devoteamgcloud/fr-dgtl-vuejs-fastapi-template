import os
import re


def removeReferenceFromProject(pattern):
    """
    Iterate on all files to find a matching
    pattern & remove all lines containing it
    """
    for root, subdirs, files in os.walk("."):
        # print("--\nroot = " + root)
        # for subdir in subdirs:
        # print("\t- subdirectory " + subdir)
        for filename in files:
            file_path = os.path.join(root, filename)
            # print("\t- file %s (full path: %s)" % (filename, file_path))
            with open(file_path, "rb") as f:
                f_content = f.read()
                if re.search(bytes(pattern, encoding="utf-8"), f_content):
                    # print(f"Found {pattern} in file: " + file_path)
                    # print("Removing...")
                    with open(file_path, "w") as f:
                        f.write(
                            re.sub(
                                f"\r?\n.*{pattern}.*",
                                "",
                                f_content.decode("utf-8", errors="ignore"),
                            )
                        )
