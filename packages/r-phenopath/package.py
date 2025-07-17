# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenopath(RPackage):
    """Genomic trajectories with heterogeneous genetic and environmental backgrounds

    PhenoPath infers genomic trajectories (pseudotimes) in the presence of heterogeneous genetic and environmental backgrounds and tests for interactions between them.
    """

    bioc = "phenopath"

    version("1.32.0", commit="fc4b5ba4540ce7c8658aa74d00d6792d1e7085e3")
    version("1.26.0", commit="2f8379027f0cd6bed12f226f84697518cd74f1c6")

    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
