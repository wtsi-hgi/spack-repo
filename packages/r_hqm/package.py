# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHqm(RPackage):
	"""Superefficient Estimation of Future Conditional Hazards Based on
Marker Information

	Provides a nonparametric smoothed kernel density estimator for the future conditional hazard when time-dependent covariates are present. It also provides pointwise and uniform confidence bands and a bandwidth selection.
	"""
	
	cran = "HQM" 

	version("0.1.0", md5="f14039a92c02d530039b5234b70cb932")

	depends_on("r@3.5:", type=("build", "run"))
