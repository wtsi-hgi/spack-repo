# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChernoffdist(RPackage):
	"""Chernoff's Distribution

	Computes Chernoff's distribution based on the method in Piet Groeneboom & Jon A Wellner (2001) Computing Chernoff's Distribution, Journal of Computational and Graphical Statistics, 10:2, 388-400, <doi:10.1198/10618600152627997>.    Chernoff's distribution is defined as the distribution of the maximizer of the two-sided Brownian motion minus quadratic drift. That is, Z = argmax (B(t)-t^2).
	"""
	
	cran = "ChernoffDist" 

	version("0.1.0", md5="ab01efb0064586a4ee00b5ff5ec40113")

	depends_on("r-gsl", type=("build", "run"))
