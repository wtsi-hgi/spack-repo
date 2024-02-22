# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCasebase(RPackage):
	"""Fitting Flexible Smooth-in-Time Hazards and Risk Functions via
Logistic and Multinomial Regression

	Fit flexible and fully parametric hazard regression models to survival data with single event type or multiple 
    competing causes via logistic and multinomial regression. Our formulation allows for arbitrary functional forms 
    of time and its interactions with other predictors for time-dependent hazards and hazard ratios. From the 
    fitted hazard model, we provide functions to readily calculate and plot cumulative incidence and survival 
    curves for a given covariate profile. This approach accommodates any log-linear hazard function of 
    prognostic time, treatment, and covariates, and readily allows for non-proportionality. We also provide 
    a plot method for visualizing incidence density via population time plots. Based on the case-base sampling 
    approach of Hanley and Miettinen (2009) <DOI:10.2202/1557-4679.1125>, Saarela and Arjas (2015) <DOI:10.1111/sjos.12125>, 
    and Saarela (2015) <DOI:10.1007/s10985-015-9352-x>.
	"""
	
	homepage = "https://sahirbhatnagar.com/casebase/"
	cran = "casebase" 

	version("0.10.4", md5="14458fe86b0fa2878db2380272b06d6d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
