# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScreencounter(RPackage):
    """Counting Reads in High-Throughput Sequencing Screens

    Provides functions for counting reads from high-throughput sequencing screen data (e.g., CRISPR, shRNA) to quantify barcode abundance. Currently supports single barcodes in single- or paired-end data, and combinatorial barcodes in paired-end data.
    """

    homepage = "https://github.com/crisprVerse/screenCounter"
    bioc = "screenCounter"

    version("1.8.0", commit="e53f46b42ca0c2581b6d89b48f7c2d6661a9a1c0")
    version("1.2.0", commit="59350ef9155bea240c1729da4457e45757b4a5da")

    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-zlibbioc", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("zlib-api", type=("build", "run", "link"))
