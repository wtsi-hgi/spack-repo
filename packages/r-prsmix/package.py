# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrsmix(RPackage):
    """The PRSmix package can be used to benchmark PRSs and compute the linear combination of trait-specific scores (PRSmix) and cross-trait scores (PRSmix+) to improve prediction accuracy."""

    homepage = "https://github.com/buutrg/PRSmix"
    git = "https://github.com/buutrg/PRSmix.git"

    version("2023-10-27", commit="98a93aa8b1d197dd4475fed23bfc7450290cfe47")

    depends_on("r-proc", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-glmnet", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-caret", type=("build", "run"))
    depends_on("r-desctools", type=("build", "run"))
    depends_on("r-rcompanion", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-fastdummies", type=("build", "run"))
