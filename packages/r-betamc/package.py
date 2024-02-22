# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBetamc(RPackage):
	"""Monte Carlo for Regression Effect Sizes

	Generates Monte Carlo confidence intervals
    for standardized regression coefficients (beta) and other effect sizes,
    including multiple correlation, semipartial correlations,
    improvement in R-squared, squared partial correlations,
    and differences in standardized regression coefficients,
    for models fitted by lm().
    'betaMC' combines ideas from Monte Carlo confidence intervals for the indirect effect
    (Pesigan and Cheung, 2023 <doi:10.3758/s13428-023-02114-4>)
    and the sampling covariance matrix of regression coefficients
    (Dudgeon, 2017 <doi:10.1007/s11336-017-9563-z>)
    to generate confidence intervals effect sizes in regression.
	"""
	
	homepage = "https://github.com/jeksterslab/betaMC"
	cran = "betaMC" 

	version("1.3.1", md5="2994b91d4c637b7f92c92226a7639223")

	depends_on("r@3.5:", type=("build", "run"))
