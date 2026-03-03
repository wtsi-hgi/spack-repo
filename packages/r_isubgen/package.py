# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsubgen(RPackage):
	"""Integrative Subtype Generation

	Multi-data type subtyping, which is data type agnostic and accepts missing data. Subtyping is performed using intermediary assessments created with autoencoders and similarity calculations.
	"""
	
	cran = "iSubGen" 

	version("1.0.1", md5="ca1c7d122c0a5875e25bb421d32e8e00")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-consensusclusterplus", type=("build", "run"))
	depends_on("r-cluster@1.14.4:", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-philentropy", type=("build", "run"))
