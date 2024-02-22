# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDregar(RPackage):
	"""Regularized Estimation of Dynamic Linear Regression in the
Presence of Autocorrelated Residuals (DREGAR)

	A penalized/non-penalized implementation for dynamic regression in the presence of autocorrelated residuals (DREGAR) using iterative penalized/ordinary least squares. It applies Mallows CP, AIC, BIC and GCV to select the tuning parameters.
	"""
	
	homepage = "http://hamedhaseli.webs.com."
	cran = "DREGAR" 

	version("0.1.3.0", md5="3b23a5cc84f7830d32df77a470c02024")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-msgps", type=("build", "run"))
