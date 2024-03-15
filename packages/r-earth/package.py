# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REarth(RPackage):
	"""Multivariate Adaptive Regression Splines.

	Build regression models using the techniques in Friedman's papers
	"Fast MARS" and "Multivariate Adaptive Regression Splines"
	<doi:10.1214/aos/1176347963>."""

	cran = "earth"

	license("GPL-3.0-only")

	version("5.3.3", md5="1b55085d1823511946e6e1c2b8ebfa9e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-formula@1.2.3:", type=("build", "run"))
	depends_on("r-plotmo@3.6:", type=("build", "run"))
