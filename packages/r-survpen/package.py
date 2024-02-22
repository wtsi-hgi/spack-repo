# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvpen(RPackage):
	"""Multidimensional Penalized Splines for Survival and Net Survival
Models

	Fits hazard and excess hazard models with multidimensional penalized splines allowing for 
        time-dependent effects, non-linear effects and interactions between several continuous covariates. In survival and net survival analysis, in addition to modelling the effect of time (via the baseline hazard), one has often to deal with several continuous covariates and model their functional forms, their time-dependent effects, and their interactions. Model specification becomes therefore a complex problem and penalized regression splines represent an appealing solution to that problem as splines offer the required flexibility while penalization limits overfitting issues. Current implementations of penalized survival models can be slow or unstable and sometimes lack some key features like taking into account expected mortality to provide net survival and excess hazard estimates. In contrast, survPen provides an automated, fast, and stable implementation (thanks to explicit calculation of the derivatives of the likelihood) and offers a unified framework for 
        multidimensional penalized hazard and excess hazard models. survPen may be of interest to those who 1) analyse any kind of time-to-event data: mortality, disease relapse, machinery breakdown, unemployment, etc 2) wish to describe the associated hazard and to understand which predictors impact its dynamics. 
	See Fauvernier et al. (2019a) <doi:10.21105/joss.01434> for an overview of the package and Fauvernier et al. (2019b) <doi:10.1111/rssc.12368> for the method.
	"""
	
	homepage = "https://github.com/fauvernierma/survPen"
	cran = "survPen" 

	version("1.6.0", md5="ad38e138be281eadea66046deb195cda")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
