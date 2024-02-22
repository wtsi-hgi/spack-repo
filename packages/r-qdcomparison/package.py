# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQdcomparison(RPackage):
	"""Modern Nonparametric Tools for Two-Sample Quantile and
Distribution Comparisons

	Allows practitioners to determine (i) if two univariate distributions (which can be continuous, discrete, or even mixed) are equal, (ii) how two distributions differ (shape differences, e.g., location, scale, etc.), and (iii) where two distributions differ (at which quantiles), all using nonparametric LP statistics. The primary reference is Jungreis, D. (2019, Technical Report).
	"""
	
	cran = "QDComparison" 

	version("3.0", md5="40e7039b59a8b34b9dd5a7020568d519")

	depends_on("r@3.5:", type=("build", "run"))
