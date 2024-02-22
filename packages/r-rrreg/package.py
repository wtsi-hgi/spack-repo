# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrreg(RPackage):
	"""Correlation and Regression Analyses for Randomized Response Data

	
    Univariate and multivariate methods to analyze randomized response 
    (RR) survey designs (e.g., Warner, S. L. (1965). Randomized response: A 
    survey technique for eliminating evasive answer bias. Journal of the 
    American Statistical Association, 60, 63–69, <doi:10.2307/2283137>). 
    Besides univariate estimates of true proportions, RR variables can be used 
    for correlations, as dependent variable in a logistic regression (with or 
    without random effects), or as predictors in a linear regression
    (Heck, D. W., & Moshagen, M. (2018). RRreg: An R package for correlation and 
    regression analyses of randomized response data. Journal of Statistical 
    Software, 85(2), 1–29, <doi:10.18637/jss.v085.i02>). For simulations and 
    the estimation of statistical power, RR data can be generated according to 
    several models. The implemented methods also allow to test the link between 
    continuous covariates and dishonesty in cheating paradigms such as the 
    coin-toss or dice-roll task (Moshagen, M., & Hilbig, B. E. (2017). 
    The statistical analysis of cheating paradigms. Behavior Research Methods, 
    49, 724–732, <doi:10.3758/s13428-016-0729-x>).
	"""
	
	homepage = "https://github.com/danheck/RRreg"
	cran = "RRreg" 

	version("0.7.5", md5="ce52cbe36774b0b7e45fcdad5628f048")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
