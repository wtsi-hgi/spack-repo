# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLgpr(RPackage):
    """Longitudinal Gaussian Process Regression

        Interpretable nonparametric modeling of longitudinal data
    using additive Gaussian process regression. Contains functionality
    for inferring covariate effects and assessing covariate relevances.
    Models are specified using a convenient formula syntax, and can include
    shared, group-specific, non-stationary, heterogeneous and temporally
    uncertain effects. Bayesian inference for model parameters is performed
    using 'Stan'. The modeling approach and methods are described in detail in
    Timonen et al. (2021) <doi:10.1093/bioinformatics/btab021>.
    """

    homepage = "https://github.com/jtimonen/lgpr"
    cran = "lgpr"

    version("1.2.4", md5="3b748d5a32d6d7a6f1fbec34468c3ed1")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-rcpp@1.0.6:", type=("build", "run"))
    depends_on("r-rcppparallel@5.0.2:", type=("build", "run"))
    depends_on("r-rcurl@1.98:", type=("build", "run"))
    depends_on("r-rstan@2.26:", type=("build", "run"))
    depends_on("r-rstantools@2.3.1:", type=("build", "run"))
    depends_on("r-bayesplot@1.7:", type=("build", "run"))
    depends_on("r-mass@7.3.50:", type=("build", "run"))
    depends_on("r-ggplot2@3.1:", type=("build", "run"))
    depends_on("r-gridextra@0.3:", type=("build", "run"))
    depends_on("r-bh@1.75.0.0:", type=("build", "run"))
    depends_on("r-rcppeigen@0.3.3.9.1:", type=("build", "run"))
    depends_on("r-stanheaders@2.26:", type=("build", "run", "link"))

    def patch(self):
        filter_file(
            "#include <stan/math/prim/mat/fun/Eigen.hpp>",
            "#include <stan/math/prim/fun/Eigen.hpp>",
            "src/lgpr_types.h",
            string=True,
        )
