# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbps(RPackage):
	"""Covariate Balancing Propensity Score

	Implements the covariate balancing propensity score (CBPS) proposed
    by Imai and Ratkovic (2014) <DOI:10.1111/rssb.12027>. The propensity score is
    estimated such that it maximizes the resulting covariate balance as well as the
    prediction of treatment assignment. The method, therefore, avoids an iteration
    between model fitting and balance checking.  The package also implements optimal
    CBPS from Fan et al. (in-press) <DOI:10.1080/07350015.2021.2002159>,  
    several extensions of the CBPS beyond the cross-sectional, binary treatment setting.
    They include the CBPS for longitudinal settings so that it can be used in 
    conjunction with marginal structural models from Imai and Ratkovic (2015) 
    <DOI:10.1080/01621459.2014.956872>, treatments with three- and four-valued treatment 
    variables, continuous-valued treatments from Fong, Hazlett, and Imai (2018) 
    <DOI:10.1214/17-AOAS1101>, propensity score estimation with a large number of 
    covariates from Ning, Peng, and Imai (2020) <DOI:10.1093/biomet/asaa020>, and the situation 
    with multiple distinct binary treatments administered simultaneously. In the future 
    it will be extended to other settings including the generalization of experimental 
    and instrumental variable estimates. 
	"""
	
	cran = "CBPS" 

	version("0.23", md5="a81475ddfe38d2f57f7f57b304d64f93")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matchit", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
