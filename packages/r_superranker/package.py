# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuperranker(RPackage):
	"""Sequential Rank Agreement

	Tools for analysing the agreement of two or more rankings of the same items. Examples are importance rankings of predictor variables and risk predictions of subjects. Benchmarks for agreement are computed based on random permutation and bootstrap. See Ekstrøm CT, Gerds TA, Jensen, AK (2018). "Sequential rank agreement methods for comparison of ranked lists." _Biostatistics_, *20*(4), 582-598 <doi:10.1093/biostatistics/kxy017> for more information.
	"""
	
	cran = "SuperRanker" 

	version("1.2.1", md5="2b92898a57fb29f9d3bed7356bdcc686")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-prodlim@1.5.7:", type=("build", "run"))
