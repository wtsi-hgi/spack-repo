# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrisprviz(RPackage):
    """Visualization Functions for CRISPR gRNAs

    Provides functionalities to visualize and contextualize CRISPR guide RNAs (gRNAs) on genomic tracks across nucleases and applications. Works in conjunction with the crisprBase and crisprDesign Bioconductor packages. Plots are produced using the Gviz framework.
    """

    homepage = "https://github.com/crisprVerse/crisprViz"
    bioc = "crisprViz"

    version("1.10.0", commit="66db0277734265516846663cbe63a012d0b72968")
    version("1.4.0", commit="1275317fad8d09a9b75d73cf0e1b5d61f4eee75d")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-crisprbase@0.99.15:", type=("build", "run"))
    depends_on("r-crisprdesign@0.99.77:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-gviz", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
