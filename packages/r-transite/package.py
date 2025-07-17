# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransite(RPackage):
    """RNA-binding protein motif analysis

    transite is a computational method that allows comprehensive analysis of the regulatory role of RNA-binding proteins in various cellular processes by leveraging preexisting gene expression data and current knowledge of binding preferences of RNA-binding proteins.
    """

    homepage = "https://transite.mit.edu"
    bioc = "transite"

    version("1.26.0", commit="9e0cd5482a4fad068fe3670a11ac4c1e39b140a6")
    version("1.20.1", commit="ce194d7924f870dbd7ca26f3432b8f9da7aa2aba")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-biocgenerics@0.26:", type=("build", "run"))
    depends_on("r-biostrings@2.48:", type=("build", "run"))
    depends_on("r-dplyr@0.7.6:", type=("build", "run"))
    depends_on("r-genomicranges@1.32.6:", type=("build", "run"))
    depends_on("r-ggplot2@3:", type=("build", "run"))
    depends_on("r-gridextra@2.3:", type=("build", "run"))
    depends_on("r-rcpp@1.0.4.8:", type=("build", "run"))
    depends_on("r-scales@1:", type=("build", "run"))
    depends_on("r-tfmpvalue@0.0.8:", type=("build", "run"))
    depends_on("r-ggseqlogo", type=("build", "link", "run"))
