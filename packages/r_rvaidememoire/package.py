# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRvaidememoire(RPackage):
	"""Testing and Plotting Procedures for Biostatistics

	Contains miscellaneous functions useful in biostatistics, mostly univariate and multivariate testing procedures with a special emphasis on permutation tests. Many functions intend to simplify user's life by shortening existing procedures or by implementing plotting functions that can be used with as many methods from different packages as possible.
	"""
	
	cran = "RVAideMemoire" 

	version("0.9-83-7", md5="1f7d1eb113ac018b384493cdf0a7f284")

	depends_on("r-ade4@1.7.8:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-lme4@1.0.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-pspearman", type=("build", "run"))
	depends_on("r-vegan@2.4.3:", type=("build", "run"))
