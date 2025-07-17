# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeuca(RPackage):
    """NEUral network-based single-Cell Annotation tool

    NeuCA is is a neural-network based method for scRNA-seq data annotation. It can automatically adjust its classification strategy depending on cell type correlations, to accurately annotate cell. NeuCA can automatically utilize the structure information of the cell types through a hierarchical tree to improve the annotation accuracy. It is especially helpful when the data contain closely correlated cell types.
    """

    bioc = "NeuCA"

    version("1.14.0", commit="5784270fdf340761ab7734a777ed5fceaff25b58")
    version("1.8.1", commit="4eb0e42bc895757d3e047231e8f8865fc0549cb9")
    version("1.8.0", commit="053e2f93a026cc1048ba2dce418f9890d2572815")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-keras", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-kableextra", type=("build", "run"))
