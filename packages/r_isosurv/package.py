# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsosurv(RPackage):
	"""Isotonic Regression on Survival Analysis

	Nonparametric estimation on survival analysis under order-restrictions.
	"""
	
	cran = "isoSurv" 

	version("0.3.0", md5="c9cdd4182a674a664e98fcd11a2a1839")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-iso", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
