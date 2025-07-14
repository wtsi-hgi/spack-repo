# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnifter(RPackage):
	"""R wrapper for the python openTSNE library

	Provides an R wrapper for the implementation of FI-tSNE from the python package openTNSE. See Poličar et al. (2019) <doi:10.1101/731877> and the algorithm described by Linderman et al. (2018) <doi:10.1038/s41592-018-0308-4>.
	"""
	
	homepage = "https://bioconductor.org/packages/snifter"
	bioc = "snifter"

	version("1.18.1", commit="c681c200b2ad0fc49238745c9a1c41d20163a999")
	version("1.12.0", commit="fcd4e62060c4971330df8ec5d15e4f2711d31810")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-basilisk", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
