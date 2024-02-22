# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDominanceanalysis(RPackage):
	"""Dominance Analysis

	Dominance analysis is a method that allows to compare the
             relative importance of predictors in multiple regression models:
             ordinary least squares, generalized linear models, 
             hierarchical linear models, beta regression and dynamic linear models. 
             The main principles and methods of 
             dominance analysis are described in
             Budescu, D. V. (1993) <doi:10.1037/0033-2909.114.3.542> and  
             Azen, R., & Budescu, D. V. (2003) <doi:10.1037/1082-989X.8.2.129>
             for ordinary least squares regression. Subsequently, the extensions 
             for multivariate regression, logistic regression and
             hierarchical linear models were described in 
             Azen, R., & Budescu, D. V. (2006) <doi:10.3102/10769986031002157>,
             Azen, R., & Traxel, N. (2009) <doi:10.3102/1076998609332754> and
             Luo, W., & Azen, R. (2013) <doi:10.3102/1076998612458319>,
             respectively.
	"""
	
	cran = "dominanceanalysis" 

	version("2.1.0", md5="8bbdfd24eb7235a9926aa9334b2197e0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
