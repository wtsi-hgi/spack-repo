# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactorassumptions(RPackage):
	"""Set of Assumptions for Factor and Principal Component Analysis

	Tests for Kaiser-Meyer-Olkin (KMO) and
    communalities in a dataset. It provides a final sample by removing
    variables in a iterable manner while keeping account of the variables
    that were removed in each step. It follows the best practices and assumptions according to
    Hair, Black, Babin & Anderson (2018, ISBN:9781473756540).
	"""
	
	homepage = "https://github.com/storopoli/FactorAssumptions"
	cran = "FactorAssumptions" 

	version("2.0.1", md5="5ba22cbd144aae58a3c34260dbbd54c1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
