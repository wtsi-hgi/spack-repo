# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLme4(RPackage):
    """Linear Mixed-Effects Models using 'Eigen' and S4.

    Fit linear and generalized linear mixed-effects models. The models and
    their components are represented using S4 classes and methods. The core
    computational algorithms are implemented using the 'Eigen' C++ library for
    numerical linear algebra and 'RcppEigen' "glue"."""

    cran = "lme4"
    version(
        "1.1-35.3",
        sha256="b4875c127c6c3a74d74fd4894817858c482d8bcf72b63e48e84834e0293f4346",
        url="https://cran.r-project.org/src/contrib/Archive/lme4/lme4_1.1-35.3.tar.gz"
    )
    version(
        "1.1-35.2",
        md5="7577eaf538481d62805b330e7e4c5e30",
        url="https://cran.r-project.org/src/contrib/lme4_1.1-35.2.tar.gz",
    )
    version(
        "1.1-35.1",
        md5="b452706beaa895b70d874a8a0154f87d",
        url="https://cran.r-project.org/src/contrib/lme4_1.1-35.1.tar.gz",
    )
    version("1.1-33", sha256="d956a5ed7cbcc016114a836bad89acf6cdafcd0f82a7d85e3805ced936b40910")
    version(
        "1.1-15",
        md5="8fa3b6c7d61e39bc27a334152613eca3",
        url="https://cran.r-project.org/src/contrib/Archive/lme4/lme4_1.1-15.tar.gz",
    )

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-boot", type=("build", "run"))
    depends_on("r-nlme@3.1.123:", type=("build", "run"))
    depends_on("r-minqa@1.1.15:", type=("build", "run"))
    depends_on("r-nloptr@1.0.4:", type=("build", "run"))
    depends_on("r-rcpp@0.10.5:", type=("build", "run"))
    depends_on("r-rcppeigen@:0.3.3.9.3", type=("build", "run"), when="@:1.1-33")
    depends_on("r-rcppeigen@0.3.3.9.4:", type=("build", "run"), when="@1.1-35:")
