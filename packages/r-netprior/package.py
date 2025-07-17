# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetprior(RPackage):
    """A model for network-based prioritisation of genes

    A model for semi-supervised prioritisation of genes integrating network data, phenotypes and additional prior knowledge about TP and TN gene labels from the literature or experts.
    """

    homepage = "http://bioconductor.org/packages/netprioR"
    bioc = "netprioR"

    version("1.34.0", commit="472209fca240773cb7173b1d726e0d6fa32aa274")
    version("1.28.0", commit="5bc3fbba3887d0884ceb545079ef5adddb29d5ea")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-sparsemvn", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-proc", type=("build", "run"))
