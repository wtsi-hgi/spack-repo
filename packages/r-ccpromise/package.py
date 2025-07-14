# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcpromise(RPackage):
	"""PROMISE analysis with Canonical Correlation for Two Forms of High Dimensional Genetic Data

	Perform Canonical correlation between two forms of high demensional genetic data, and associate the first compoent of each form of data with a specific biologically interesting pattern of associations with multiple endpoints. A probe level analysis is also implemented.
	"""
	
	bioc = "CCPROMISE"

	version("1.34.0", commit="56063e0c4ee518d4d20d0473f6affd05e76c5116")
	version("1.28.0", commit="deb4e6e7eccaef67d9fc9cb67cd4ccc28d1516d6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ccp", type=("build", "run"))
	depends_on("r-promise", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
