# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnmcb(RPackage):
    """Predicting Disease Progression Based on Methylation Correlated Blocks using Ensemble Models

    Creation of the correlated blocks using DNA methylation profiles. Machine learning models can be constructed to predict differentially methylated blocks and disease progression.
    """

    bioc = "EnMCB"

    version("1.20.0", commit="318fb87d4406d74c84cdce984138156093970c8c")
    version("1.14.0", commit="124b1759d29e047f8111b8f107acfccbcedf6099")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-survivalroc", type=("build", "run"))
    depends_on("r-glmnet", type=("build", "run"))
    depends_on("r-rms", type=("build", "run"))
    depends_on("r-mboost", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-survivalsvm", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-boot", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
