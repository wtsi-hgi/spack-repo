# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeriodics(RPackage):
	"""Functions for Generating Periodic Curves

	
    Functions for generating variants of curves:
    restricted cubic spline, periodic restricted cubic spline,
    periodic cubic spline. Periodic splines can be used to model data
    that has periodic nature / seasonality.
	"""
	
	cran = "peRiodiCS" 

	version("0.5.0", md5="11231641ff80500434d04ce7f3677a67")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
