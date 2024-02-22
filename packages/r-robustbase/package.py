# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustbase(RPackage):
	"""Basic Robust Statistics.

	"Essential" Robust Statistics. Tools allowing to analyze data with robust
	methods. This includes regression methodology including model selections
	and multivariate statistics where we strive to cover the book "Robust
	Statistics, Theory and Methods" by 'Maronna, Martin and Yohai'; Wiley
	2006."""

	cran = "robustbase"

	version("0.99-2", md5="1b79921bca8334ef03f67f0ca0afd63f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-deoptimr", type=("build", "run"))
