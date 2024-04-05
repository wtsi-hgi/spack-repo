# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RTmae(RPackage):
    """Package containing functions to:

    perform a negative binomial test on allele-specific counts
    add gnomAD minor allele frequencies
    MAplot (FC vs total counts) of allele-specific counts and results
    allelic counts (ALT vs REF)"""

    homepage = "https://github.com/gagneurlab/tMAE"
    url = "https://github.com/gagneurlab/tMAE/archive/refs/tags/1.0.4.tar.gz"

    version("1.0.4", sha256="8d11bcf01459dd7f69ecbd22a293b422c218a63d2cf49c1c9bba080bcb58b3aa")
    version("1.0.3", sha256="1fac624947a7c08795cc943106fd78c765b15920ff13f6cb12f25bc9fe5ebbb9")
    version("1.0.2", sha256="5fda2eefb3ee06ac8f9bbe6bcdd847f013fd5576a2069f933d0642010dfbd6f3")

    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-deseq2", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomicscores", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
