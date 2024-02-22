# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScar(RPackage):
	"""Shape-Constrained Additive Regression: a Maximum Likelihood
Approach

	Computes the maximum likelihood estimator of the generalised additive and index regression with shape constraints. Each additive component function is assumed to obey one of the nine possible shape restrictions: linear, increasing, decreasing, convex, convex increasing, convex decreasing, concave, concave increasing, or concave decreasing. For details, see Chen and Samworth (2016) <doi:10.1111/rssb.12137>.
	"""
	
	cran = "scar" 

	version("0.2-2", md5="a83aff70efce016d0f56e57dce5a6e2f")

	depends_on("r@3:", type=("build", "run"))
