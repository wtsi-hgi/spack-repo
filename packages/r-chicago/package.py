# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChicago(RPackage):
	"""CHiCAGO: Capture Hi-C Analysis of Genomic Organization

	A pipeline for analysing Capture Hi-C data.
	"""
	
	bioc = "Chicago"

	version("1.36.0", commit="ad00daa5680093fc40264b38718b8aa6c792fcdd")
	version("1.30.0", commit="febaf7c95cfaedb19f5f958e2da0a6815447c064")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-delaporte", type=("build", "run"))
