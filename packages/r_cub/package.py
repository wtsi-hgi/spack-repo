# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCub(RPackage):
	"""A Class of Mixture Models for Ordinal Data

	For ordinal rating data, estimate and test models within the family of CUB models and their extensions (where CUB stands for Combination of a discrete Uniform and a shifted Binomial distributions); Simulation routines, plotting facilities and fitting measures are also provided.
	"""
	
	cran = "CUB" 

	version("1.1.5", md5="94e80eca6bfd4cdb0bbe32bcae5a996e")
	version("1.1.4", md5="b5acfbfc9dba8dfe9d7b0fba9c3e5104")

	depends_on("r@2.15.2:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
