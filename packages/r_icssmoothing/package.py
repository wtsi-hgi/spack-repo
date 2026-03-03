# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcssmoothing(RPackage):
	"""Data Smoothing by Interpolating Cubic Splines

	We construct the explicit form of clamped cubic interpolating spline (both uniform - knots are equidistant and non-uniform - knots are arbitrary). Using this form, we propose a linear regression model suitable for real data smoothing.
	"""
	
	cran = "ICSsmoothing" 

	version("1.2.8", md5="28c0bf68de66f53a86a54abfac97e86e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
