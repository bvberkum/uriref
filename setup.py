from distutils.core import setup
setup(
    name = "uriref",
    packages = ["uriref"],
    version = "0.0.3-dev-20170106", # uriref
    description = "Regex Based URI reference parsing",
    author = "Berend (mpe)",
    author_email = "berend@dotmpe.com",
    url = "http://github.com/dotmpe/uriref",
#    bug?_url = "https://github.com/dotmpe/uriref/issues",
#    download_url = "",
    keywords = ["url", "uri"],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description = """\
URL and URN parser written in regular expressions.
Based on RFC 2396 BNF terms. No revieto RFC 3986 planned but not started.
""",
    scripts = [
        'bin/uriref-cli.py',
    ],
)
