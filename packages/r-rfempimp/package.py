# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfempimp(RPackage):
	"""Multiple Imputation using Chained Random Forests

	An R package for multiple imputation using chained random forests.
    Implemented methods can handle missing data in mixed types of variables by
    using prediction-based or node-based conditional distributions constructed
    using random forests. For prediction-based imputation, the method based on
    the empirical distribution of out-of-bag prediction errors of random forests
    and the method based on normality assumption for prediction errors of random
    forests are provided for imputing continuous variables. And the method based
    on predicted probabilities is provided for imputing categorical variables.
    For node-based imputation, the method based on the conditional distribution
    formed by the predicting nodes of random forests, and the method based on
    proximity measures of random forests are provided. More details of the
    statistical methods can be found in Hong et al. (2020) <arXiv:2004.14823>.
	"""
	
	homepage = "https://github.com/shangzhi-hong/RfEmpImp"
	cran = "RfEmpImp" 

	version("2.1.8", md5="003c89489b66c4a7677fe1fecb0025cc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mice@3.9:", type=("build", "run"))
	depends_on("r-ranger@0.12.1:", type=("build", "run"))
