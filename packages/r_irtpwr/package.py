# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrtpwr(RPackage):
	"""Power Analysis for IRT Models Using the Wald, LR, Score, and
Gradient Statistics

	Implementation of analytical and sampling-based power analyses for
    the Wald, likelihood ratio (LR), score, and gradient tests. Can be applied
    to item response theory (IRT) models that are fitted using marginal maximum
    likelihood estimation. The methods are described in our paper
    (Zimmer et al. (2022) <doi:10.1007/s11336-022-09883-5>).
	"""
	
	homepage = "https://github.com/flxzimmer/irtpwr"
	cran = "irtpwr" 

	version("1.0.3", md5="27b8c3eee7c3a1aa60a524019108e36e")

	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
