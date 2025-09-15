# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLisi(RPackage):
    """Local Inverse Simpson Index (LISI) for scRNAseq data.

    This method assesses how well cells with different labels are mixed in
    single-cell RNA-seq data using the Inverse Simpson's Index computed over
    each cell's local neighborhood.
    """

    homepage = "https://github.com/immunogenomics/LISI"
    url = "https://github.com/immunogenomics/LISI/archive/refs/tags/v1.0.tar.gz"
    git = "https://github.com/immunogenomics/LISI.git"

    license("GPL-3.0-only")

    version("1.0", sha256="19cf8bd33b28887f2a63738bcd23d19b2e13db2a0c7a86919d46a20469fe41c4")

    depends_on("r@3.4.0:", type=("build", "run"))

    # Imports + LinkingTo
    with default_args(type=("build", "run")):
        depends_on("r-rcpp")
        depends_on("r-rcpparmadillo")
        depends_on("r-rann")

        # Suggested packages (included for R packages per repo policy)
        depends_on("r-testthat")
        depends_on("r-dplyr")
        depends_on("r-tidyr")
        depends_on("r-magrittr")
        depends_on("r-ggplot2")
