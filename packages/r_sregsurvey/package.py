# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSregsurvey(RPackage):
	"""Semiparametric Model-Assisted Estimation in Finite Populations

	It is a framework to fit semiparametric regression estimators for the total parameter of a finite population when the interest variable is asymmetric distributed. The main references for this package are Sarndal C.E., Swensson B., and Wretman J. (2003,ISBN: 978-0-387-40620-6, "Model Assisted Survey Sampling." Springer-Verlag) 
  Cardozo C.A, Paula G.A. and Vanegas L.H. (2022) "Generalized log-gamma additive partial linear mdoels with P-spline smoothing", Statistical Papers. 
  Cardozo C.A and Alonso-Malaver C.E. (2022). "Semi-parametric model assisted estimation in finite populations." In preparation.    
	"""
	
	cran = "sregsurvey" 

	version("0.1.3", md5="5b585d51c71a0e82189ad3502c092020")

	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-teachingsampling", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
