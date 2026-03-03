# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPenphcure(RPackage):
	"""Variable Selection in PH Cure Model with Time-Varying Covariates

	Implementation of the semi-parametric proportional-hazards (PH) of Sy and Taylor (2000) <doi:10.1111/j.0006-341X.2000.00227.x> extended to time-varying covariates. Estimation and variable selection are based on the methodology described in Beretta and Heuchenne (2019) <doi:10.1080/02664763.2018.1554627>; confidence intervals of the parameter estimates may be computed using a bootstrap approach. Moreover, data following the PH cure model may be simulated using a method similar to Hendry (2014) <doi:10.1002/sim.5945>, where the event-times are generated on a continuous scale from a piecewise exponential distribution conditional on time-varying covariates.
	"""
	
	homepage = "https://github.com/a-beretta/penPHcure"
	cran = "penPHcure" 

	version("1.0.2", md5="0726b79b1fd432435103cdc23d0b0206")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
