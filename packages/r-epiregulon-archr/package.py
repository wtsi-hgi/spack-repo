# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpiregulonArchr(RPackage):
    """Extended version of epiregulon for ArchR integration.

    Gene regulatory networks model the underlying gene regulation hierarchies
    that drive gene expression and cell states. This package extends epiregulon
    to allow for downstream analysis of single cell data prepared with the ArchR
    package. It utilizes gene expression, chromatin availability and transcription
    factor motif matches data retrieved from the ArchR project to construct
    gene regulatory networks and infer transcription factor activity in single cells."""

    homepage = "https://github.com/xiaosaiyao/epiregulon.archr/"
    git = "https://github.com/xiaosaiyao/epiregulon.archr.git"

    license("MIT")

    version("0.99.5", commit="a02bd18b69944393031e77bb822a29f9afc806a0")

    # Depends
    depends_on("r@4.4:", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))

    # Imports - based on the epiregulon.extra and the repository description
    depends_on("r-epiregulon", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-archr", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))

    # Suggests
    depends_on("r-knitr", type=("build"))
    depends_on("r-rmarkdown", type=("build"))
    depends_on("r-biocstyle", type=("build"))
    depends_on("r-testthat", type=("build"))
    depends_on("r-epiregulon-extra", type=("build"))
    depends_on("r-scmultiome", type=("build"))
