# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConcordancetest(RPackage):
	"""An Alternative to the Kruskal-Wallis Based on the Kendall Tau
Distance

	The Concordance Test is a non-parametric method for testing whether two o more samples originate from the same distribution. It extends the Kendall Tau correlation coefficient when there are only two groups. For details, see Alcaraz J., Anton-Sanchez L., Monge J.F. (2022) The Concordance Test, an Alternative to Kruskal-Wallis Based on the Kendall-tau Distance: An R Package. The R Journal 14, 26–53 <doi:10.32614/RJ-2022-039>.
	"""
	
	cran = "ConcordanceTest" 

	version("1.0.3", md5="5d40309fe8625583d2403b0cf6e74b0d")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
