# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLawstat(RPackage):
	"""Tools for Biostatistics, Public Policy, and Law

	Statistical tests widely utilized in biostatistics, public policy, and law. Along with the well-known tests for equality of means and variances, randomness, and measures of relative variability, the package contains new robust tests of symmetry, omnibus and directional tests of normality, and their graphical counterparts such as robust QQ plot, robust trend tests for variances, etc. All implemented tests and methods are illustrated by simulations and real-life examples from legal statistics, economics, and biostatistics.
	"""
	
	cran = "lawstat" 

	version("3.6", md5="8100eebb364b806b57aa09624d986530")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-kendall", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
