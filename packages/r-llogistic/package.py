# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLlogistic(RPackage):
	"""The L-Logistic Distribution

	Density, distribution function, quantile function and random generation for the L-Logistic distribution with parameters m and phi. The parameter m is the median of the distribution.
	"""
	
	cran = "llogistic" 

	version("1.0.3", md5="39e855c456c1ada890de97ab5809b2d0")

	depends_on("r@3.3:", type=("build", "run"))
