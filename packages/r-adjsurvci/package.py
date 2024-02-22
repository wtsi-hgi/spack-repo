# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdjsurvci(RPackage):
	"""Parameter and Adjusted Probability Estimation for Right-Censored
Data

	Functions in this package fit a stratified Cox proportional hazards and a proportional subdistribution hazards model by extending Zhang et al., (2007) <doi: 10.1016/j.cmpb.2007.07.010> 
  and Zhang et al., (2011) <doi: 10.1016/j.cmpb.2010.07.005> respectively to clustered right-censored data. The functions also provide the estimates of the cumulative baseline hazard along with their standard errors. Furthermore, the adjusted survival and cumulative incidence probabilities are also provided along with their standard errors. Finally, the estimate of cumulative incidence and survival probabilities given a vector of covariates along with their standard errors are also provided.
	"""
	
	cran = "adjSURVCI" 

	version("1.0", md5="2992cf6603cba72c7f9c1318b5730422")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
