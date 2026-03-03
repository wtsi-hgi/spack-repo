# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPresiduals(RPackage):
	"""Probability-Scale Residuals and Residual Correlations

	Computes probability-scale residuals and residual correlations
    for continuous, ordinal, binary, count, and time-to-event data <doi:10.18637/jss.v094.i12>.
	"""
	
	cran = "PResiduals" 

	version("1.0-1", md5="f5e4fdd0e5ecc5ed2cf0e526b150cb48")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
