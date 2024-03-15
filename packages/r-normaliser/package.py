# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNormaliser(RPackage):
	"""Re-Scale Vectors and Time-Series Features

	Provides standardized access to a range of re-scaling methods for numerical vectors
    and time-series features calculated within the 'theft' ecosystem.
	"""
	
	homepage = "https://hendersontrent.github.io/normaliseR/"
	cran = "normaliseR" 

	version("0.1.2", md5="5b0414c8dcda020102afb764865bd41f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
