# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmc(RPackage):
	"""Multivariate Measurement Error Correction

	Provides routines for multivariate measurement error correction. Includes procedures for linear, logistic and Cox regression models. Bootstrapped standard errors and confidence intervals can be obtained for corrected estimates.
	"""
	
	cran = "mmc" 

	version("0.0.3", md5="64ab4fe9f4bc7230686a9c68327662b0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival@2.38.1:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
