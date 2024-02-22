# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
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

	version("5.3.2", md5="8d473edbeec4d96cc183ab1baae488cc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-formula@1.2.3:", type=("build", "run"))
	depends_on("r-plotmo@3.6:", type=("build", "run"))
	depends_on("r-teachingdemos@2.10:", type=("build", "run"))
