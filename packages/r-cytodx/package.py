# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytodx(RPackage):
    """Robust prediction of clinical outcomes using cytometry data without cell gating

    This package provides functions that predict clinical outcomes using single cell data (such as flow cytometry data, RNA single cell sequencing data) without the requirement of cell gating or clustering.
    """

    bioc = "CytoDx"

    version("1.28.0", commit="589ff8726b4f30f59b8335f3c9dc92ca5a29a06b")
    version("1.22.0", commit="72994ad2a690e4b29434ac70295113378113d9f5")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-glmnet", type=("build", "run"))
    depends_on("r-rpart", type=("build", "run"))
    depends_on("r-rpart-plot", type=("build", "run"))
    depends_on("r-flowcore", type=("build", "run"))
