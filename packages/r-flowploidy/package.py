# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowploidy(RPackage):
	"""Analyze flow cytometer data to determine sample ploidy

	Determine sample ploidy via flow cytometry histogram analysis. Reads Flow Cytometry Standard (FCS) files via the flowCore bioconductor package, and provides functions for determining the DNA ploidy of samples based on internal standards.
	"""
	
	homepage = "https://github.com/plantarum/flowPloidy"
	bioc = "flowPloidy"

	version("1.34.0", commit="7ba67516cb797af7691fa4724b9e5e915a56a91f")
	version("1.28.0", commit="36f0e2b063d6f78e2f5f812d65ee39089133ffe1")

	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
