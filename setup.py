from setuptools import setup, find_packages

setup(
        name="sample-http-api",
        version="0.1"
        packages=find_packages(),
        scripts=["api.py", "raw.py"],

        package_data={
            # include yaml config file and json data file
            "": ["config.yml", "data.json"]
        }

        # metadata 
        # (not necessary here: I do not intend to upload this package anywhere)
        # (still I put it here just to remember about it)
        author="Trofogol",
        author_email="nickb.ufeim@gmail.com",
        description="Sample http api application that gets data from mysql server and some internal files. Made for self-educational purposes.",
        keywords="api http mysql sample trofogol",
        url="https://github.com/Trofogol/sample-http-api"
)
