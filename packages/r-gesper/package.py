# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGesper(RPackage):
    """Gene-Specific Phenotype EstimatoR

    Estimates gene-specific phenotypes from off-target confounded RNAi screens. The phenotype of each siRNA is modeled based on on-targeted and off-targeted genes, using a regularized linear regression model.
    """

    homepage = "http://www.cbg.ethz.ch/software/gespeR"
    bioc = "gespeR"

    version("1.40.0", commit="4db2de8ba4436fc4ee0c47c113467a02cd68e739")
    version("1.34.0", commit="35e604386f959ac453b078f4531260d071eb0e81")

    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-glmnet", type=("build", "run"))
    depends_on("r-cellhts2", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
