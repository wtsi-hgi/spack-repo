# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArcensreg(RPackage):
	"""Fitting Univariate Censored Linear Regression Model with
Autoregressive Errors

	It fits a univariate left, right, or interval censored linear regression model
    with autoregressive errors, considering the normal or the Student-t distribution for the 
    innovations. It provides estimates and standard errors of the parameters, predicts 
    future observations, and supports missing values on the dependent variable.
    References used for this package:
    Schumacher, F. L., Lachos, V. H., & Dey, D. K. (2017). Censored regression models with 
    autoregressive errors: A likelihood-based perspective. Canadian Journal of Statistics,
    45(4), 375-392 <doi:10.1002/cjs.11338>.
    Schumacher, F. L., Lachos, V. H., Vilca-Labra, F. E., & Castro, L. M. (2018). Influence 
    diagnostics for censored regression models with autoregressive errors. Australian & New 
    Zealand Journal of Statistics, 60(2), 209-229 <doi:10.1111/anzs.12229>.
    Valeriano, K. A., Schumacher, F. L., Galarza, C. E., & Matos, L. A. (2021). Censored 
    autoregressive regression models with Student-t innovations. arXiv preprint 
    <arXiv:2110.00224>.
	"""
	
	cran = "ARCensReg" 

	version("3.0.1", md5="cc060896dd3534fba7d9139146a8f4a6")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-qqplotr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
