# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConcordexr(RPackage):
    """Calculate the concordex coefficient

    Many analysis workflows include approximation of a nearest neighbors graph followed by clustering of the graph structure. The concordex coefficient estimates the concordance between the graph and clustering results. The package 'concordexR' is an R implementation of the original concordex Python-based command line tool.
    """

    homepage = "https://github.com/pachterlab/concordexR"
    bioc = "concordexR"

    version("1.8.0", commit="0f8144d56fb76bbf83b183095a4f5f27f35e7a3d")
    version("1.2.0", commit="adee426af98a433751daed4acf88a6aaacbfbb79")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-cli", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
