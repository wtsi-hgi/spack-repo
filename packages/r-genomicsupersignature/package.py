# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicsupersignature(RPackage):
    """Interpretation of RNA-seq experiments through robust, efficient comparison to public databases

    This package provides a novel method for interpreting new transcriptomic datasets through near-instantaneous comparison to public archives without high-performance computing requirements. Through the pre-computed index, users can identify public resources associated with their dataset such as gene sets, MeSH term, and publication. Functions to identify interpretable annotations and intuitive visualization options are implemented in this package.
    """

    homepage = "https://github.com/shbrief/GenomicSuperSignature"
    bioc = "GenomicSuperSignature"

    version("1.16.1", commit="08fd55fc2ba1f088f9fa61d00008b55986cfd5d3")
    version("1.10.0", commit="4f4ff12bcaaf76aa51fd05ddeb02ab3fa1e9e57e")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-ggpubr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-flextable", type=("build", "run"))
    depends_on("r-irlba", type=("build", "run"))
