# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMosbi(RPackage):
    """Molecular Signature identification using Biclustering

    This package is a implementation of biclustering ensemble method MoSBi (Molecular signature Identification from Biclustering). MoSBi provides standardized interfaces for biclustering results and can combine their results with a multi-algorithm ensemble approach to compute robust ensemble biclusters on molecular omics data. This is done by computing similarity networks of biclusters and filtering for overlaps using a custom error model. After that, the louvain modularity it used to extract bicluster communities from the similarity network, which can then be converted to ensemble biclusters. Additionally, MoSBi includes several network visualization methods to give an intuitive and scalable overview of the results. MoSBi comes with several biclustering algorithms, but can be easily extended to new biclustering algorithms.
    """

    bioc = "mosbi"

    version("1.14.0", commit="536a484edb5efd939527a6f3547bee62751ea5c9")
    version("1.8.0", commit="adf6bad0ea6996f5a9046b495a34814eb10a963a")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-bh", type=("build", "run"))
    depends_on("r-xml2", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-fabia", type=("build", "run"))
    depends_on("r-rcppparallel", type=("build", "run"))
    depends_on("r-biclust", type=("build", "run"))
    depends_on("r-isa2", type=("build", "run"))
    depends_on("r-qubic", type=("build", "run"))
    depends_on("r-akmbiclust", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
