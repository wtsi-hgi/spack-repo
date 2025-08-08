# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtracklayer(RPackage):
    """R interface to genome annotation files and the UCSC genome browser.

    Extensible framework for interacting with multiple genome browsers
    (currently UCSC built-in) and manipulating annotation tracks in various
    formats (currently GFF, BED, bedGraph, BED15, WIG, BigWig and 2bit
    built-in). The user may export/import tracks to/from the supported
    browsers, as well as query and modify the browser state, such as the
    current viewport."""

    bioc = "rtracklayer"
    version("1.68.0", commit="aa5ace3bafeb3acdd179911c44a439b4b406cf93")
    version("1.62.0", commit="58efbf9c30c6f62e9c432746af75626fc10d2a3f")
    version("1.60.0", commit="de35bc03116fc7ad30f0e425b41715c3cb2e783b")
    version("1.58.0", commit="54a74972c08775fdf1e83e6e22cd0b8fad677fc1")
    version("1.56.1", commit="4c6d2201fcb102d471bd88f4f51cc34317669955")
    version("1.56.0", commit="1d70f7dc464ad87a1fde61588cd9ae0cb86b6e86")
    version("1.54.0", commit="04cdd75521a8364e67a49d7352500dd4a3e83c55")
    version("1.50.0", commit="d2e61f72ff5d5a94c2c487ba108a37f23bfcc1e6")
    version("1.44.4", commit="aec96e85daf53b5c5eb2e89250d2755352be4de3")
    version("1.42.2", commit="76702f671faea736807d54aeecfbadcd152d94c5")
    version("1.40.6", commit="ba9a6e711504a702147383bc7abfcc36eb304df7")
    version("1.38.3", commit="f20db703c09dc7e808c09e9b78c15aec9e546248")
    version("1.36.6", commit="8c0ac7230f94e0c5a981acbb178c8de70e968131")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicranges@1.37.2:", type=("build", "run"))
    depends_on("r-xml@1.98.0:", type=("build", "run"))
    depends_on("r-biocgenerics@0.35.3:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-xvector", type=("build", "run"))
    depends_on("r-genomeinfodb@1.15.2:", type=("build", "run"))
    depends_on("r-biostrings@2.47.6:", type=("build", "run"))
    depends_on("r-zlibbioc", type=("build", "run"))
    depends_on("r-rcurl@1.4.2:", type=("build", "run"))
    depends_on("r-curl", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    # C code includes <curl/curl.h>, requires system libcurl
    depends_on("curl", type=("build", "link", "run"))
    depends_on("r-rsamtools@1.31.2:", type=("build", "run"))
    depends_on("r-genomicalignments@1.15.6:", type=("build", "run"))
    depends_on("r-biocio", type=("build", "run"))
    depends_on("r-restfulr@0.0.13:", type=("build", "run"))
    depends_on("zlib", type=("build", "link", "run"))
