# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContibait(RPackage):
    """Improves Early Build Genome Assemblies using Strand-Seq Data

    Using strand inheritance data from multiple single cells from the organism whose genome is to be assembled, contiBAIT can cluster unbridged contigs together into putative chromosomes, and order the contigs within those chromosomes.
    """

    bioc = "contiBAIT"

    version("1.30.0", commit="4d4e432f17f219835594cd3b4f498fcf9b1004d2")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-bh", type=("build", "run"))
    depends_on("r-rsamtools@1.21:", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-clue", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-biocgenerics@0.31.6:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-tsp", type=("build", "run"))
    depends_on("r-genomicfiles", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-dnacopy", type=("build", "run"))
    depends_on("r-colorspace", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-exomecopy", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-diagram", type=("build", "run"))
