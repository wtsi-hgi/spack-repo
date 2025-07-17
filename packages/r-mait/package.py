# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMait(RPackage):
    """Statistical Analysis of Metabolomic Data

    The MAIT package contains functions to perform end-to-end statistical analysis of LC/MS Metabolomic Data. Special emphasis is put on peak annotation and in modular function design of the functions.
    """

    bioc = "MAIT"

    version("1.42.0", commit="5dc55b0cc753263d24dbb662c951917cb6951dba")
    version("1.36.0", commit="6387895ce872c818d37bab9ac3b6b5d05f282b58")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-camera", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-pls", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
    depends_on("r-class", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-plsgenomics", type=("build", "run"))
    depends_on("r-agricolae", type=("build", "run"))
    depends_on("r-xcms", type=("build", "run"))
    depends_on("r-caret", type=("build", "run"))
