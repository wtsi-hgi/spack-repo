# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowbeads(RPackage):
	"""flowBeads: Analysis of flow bead data

	This package extends flowCore to provide functionality specific to bead data. One of the goals of this package is to automate analysis of bead data for the purpose of normalisation.
	"""
	
	bioc = "flowBeads" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/flowBeads_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/flowBeads/flowBeads_1.40.0.tar.gz"]

	version("1.40.0", md5="3c9aa4f78c8b1b2397d6004773311174")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
