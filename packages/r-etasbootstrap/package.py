# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REtasbootstrap(RPackage):
	"""Bootstrap Confidence Interval Estimation for 'ETAS' Model
Parameters

	The 2-D spatial and temporal Epidemic Type Aftershock Sequence ('ETAS') Model is widely used to 'decluster' earthquake data catalogs. Usually, the calculation of standard errors of the 'ETAS' model parameter estimates is based on the Hessian matrix derived from the log-likelihood function of the fitted model. However, when an 'ETAS' model is fitted to a local data set over a time period that is limited or short, the standard errors based on the Hessian matrix may be inaccurate. It follows that the asymptotic confidence intervals for parameters may not always be reliable. As an alternative, this package allows the building of bootstrap confidence intervals based on empirical quantiles for the parameters of the 2-D spatial and temporal 'ETAS' model.
	"""
	
	cran = "ETASbootstrap" 

	version("0.1.0", md5="f4a5fbc541acd51c2efd8733c05079d3")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-etas@0.5.1:", type=("build", "run"))
	depends_on("r-mass@7.3.58.2:", type=("build", "run"))
