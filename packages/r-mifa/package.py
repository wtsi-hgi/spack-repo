# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMifa(RPackage):
	"""Multiple Imputation for Exploratory Factor Analysis

	Impute the covariance matrix of incomplete data so that factor 
  analysis can be performed. Imputations are made using multiple imputation 
  by Multivariate Imputation with Chained Equations (MICE) and combined with 
  Rubin's rules. Parametric Fieller confidence intervals and nonparametric
  bootstrap confidence intervals can be obtained for the variance explained by 
  different numbers of principal components. The method is described in 
  Nassiri et al. (2018) <doi:10.3758/s13428-017-1013-4>.
	"""
	
	homepage = "https://github.com/teebusch/mifa"
	cran = "mifa" 

	version("0.2.0", md5="217eb1811e2cb2e16fc13db454164381")

	depends_on("r-mice", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
