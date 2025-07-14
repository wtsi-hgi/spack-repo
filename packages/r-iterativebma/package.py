# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIterativebma(RPackage):
	"""The Iterative Bayesian Model Averaging (BMA) algorithm

	The iterative Bayesian Model Averaging (BMA) algorithm is a variable selection and classification algorithm with an application of classifying 2-class microarray samples, as described in Yeung, Bumgarner and Raftery (Bioinformatics 2005, 21: 2394-2402).
	"""
	
	homepage = "http://faculty.washington.edu/kayee/research.html"
	bioc = "iterativeBMA"

	version("1.66.0", commit="ef3a9ec9486f07d49b9f55b7a06206830123663a")
	version("1.60.0", commit="54234d370e35bbb7144f256ca5c700751c945fbd")

	depends_on("r-bma", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
