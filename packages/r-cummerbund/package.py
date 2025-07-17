# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCummerbund(RPackage):
    """Analysis, exploration, manipulation, and visualization of Cufflinks high-throughput sequencing data.

    Allows for persistent storage, access, exploration, and manipulation of Cufflinks high-throughput sequencing data.  In addition, provides numerous plotting functions for commonly used visualizations.
    """

    bioc = "cummeRbund"

    version("2.50.0", commit="38d98f6b544fa47d1b3dc8a136b4bfe1171eb1e5")
    version("2.44.0", commit="c4179c6c9ad03e27d3d18de9f9433963e844c9c3")

    depends_on("r@2.7:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-fastcluster", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-gviz", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
