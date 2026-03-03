# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRendo(RPackage):
	"""Fitting Linear Models with Endogenous Regressors using Latent
Instrumental Variables

	Fits linear models with endogenous regressor using latent instrumental variable approaches. 
    The methods included in the package are Lewbel's (1997) <doi:10.2307/2171884> higher moments approach as well as 
    Lewbel's (2012) <doi:10.1080/07350015.2012.643126> heteroscedasticity approach, Park and Gupta's (2012) <doi:10.1287/mksc.1120.0718> joint estimation method 
    that uses Gaussian copula and Kim and Frees's (2007) <doi:10.1007/s11336-007-9008-1> multilevel generalized
    method of moment approach that deals with endogeneity in a multilevel setting.
    These are statistical techniques to address the endogeneity problem where no external instrumental variables are needed.
    See the publication related to this package in the Journal of Statistical Software for more details: <doi:10.18637/jss.v107.i03>.
    Note that with version 2.0.0 sweeping changes were introduced which greatly improve functionality and usability but break backwards compatibility.
	"""
	
	homepage = "https://github.com/mmeierer/REndo"
	cran = "REndo" 

	version("2.4.9", md5="e69786ef61a95b5e7c357ffa902d7764")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-formula@1.2:", type=("build", "run"))
	depends_on("r-optimx@2013.8.7:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.8:", type=("build", "run"))
	depends_on("r-aer@1.2.5:", type=("build", "run"))
	depends_on("r-matrix@1.2.14:", type=("build", "run"))
	depends_on("r-lme4@1.1.18.1:", type=("build", "run"))
	depends_on("r-data-table@1.11.8:", type=("build", "run"))
	depends_on("r-corpcor@1.6.9:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lmtest@0.9.35:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
