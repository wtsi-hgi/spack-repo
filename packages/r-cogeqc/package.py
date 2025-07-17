# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCogeqc(RPackage):
    """Systematic quality checks on comparative genomics analyses

    cogeqc aims to facilitate systematic quality checks on standard comparative genomics analyses to help researchers detect issues and select the most suitable parameters for each data set. cogeqc can be used to asses: i. genome assembly and annotation quality with BUSCOs and comparisons of statistics with publicly available genomes on the NCBI; ii. orthogroup inference using a protein domain-based approach and; iii. synteny detection using synteny network properties. There are also data visualization functions to explore QC summary statistics.
    """

    homepage = "https://github.com/almeidasilvaf/cogeqc"
    bioc = "cogeqc"

    version("1.12.0", commit="3865eea8a57cddecf5331d6994c02b6bfe31bad6")
    version("1.6.2", commit="173a2b46dff1832cfdf1eae6f9db898e1b6f5fc8")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-ggtree", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-ggbeeswarm", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("busco@5.1.3:", type=("build", "link", "run"))
