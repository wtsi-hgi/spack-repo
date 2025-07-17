# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimbu(RPackage):
    """Simulate Bulk RNA-seq Datasets from Single-Cell Datasets

    SimBu can be used to simulate bulk RNA-seq datasets with known cell type fractions. You can either use your own single-cell study for the simulation or the sfaira database. Different pre-defined simulation scenarios exist, as are options to run custom simulations. Additionally, expression values can be adapted by adding an mRNA bias, which produces more biologically relevant simulations.
    """

    homepage = "https://github.com/omnideconv/SimBu"
    bioc = "SimBu"

    version("1.10.0", commit="f3e56811ea6d9d09b4a2a55ccf40e55aa8f112eb")
    version("1.4.3", commit="0c37a0dd31f6e57e8e394ad408e1426f15a235e9")

    depends_on("r-basilisk", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-matrix@1.3.3:", type=("build", "run"))
    depends_on("r-phyloseq", type=("build", "run"))
    depends_on("r-proxyc", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))
    depends_on("r-reticulate", type=("build", "run"))
    depends_on("r-sparsematrixstats", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
