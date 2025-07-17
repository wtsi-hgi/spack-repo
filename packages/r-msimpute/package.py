# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsimpute(RPackage):
    """Imputation of label-free mass spectrometry peptides

    MsImpute is a package for imputation of peptide intensity in proteomics experiments. It additionally contains tools for MAR/MNAR diagnosis and assessment of distortions to the probability distribution of the data post imputation.  The missing values are imputed by low-rank approximation of the underlying data matrix if they are MAR (method = "v2"), by Barycenter approach if missingness is MNAR ("v2-mnar"), or by Peptide Identity Propagation (PIP).
    """

    bioc = "msImpute"

    version("1.18.0", commit="c088efa2e4b2c0b65670c2440a5d6c69ee982cba")
    version("1.12.0", commit="01032d5dffa951191fa3bf34b958eee1474975dd")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-softimpute", type=("build", "run"))
    depends_on("r-pdist", type=("build", "run"))
    depends_on("r-reticulate", type=("build", "run"))
    depends_on("r-scran", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-fnn", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-mvtnorm", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("python", type=("build", "link", "run"))
