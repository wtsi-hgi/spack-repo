# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFarms(RPackage):
	"""FARMS - Factor Analysis for Robust Microarray Summarization

	The package provides the summarization algorithm called Factor Analysis for Robust Microarray Summarization (FARMS) and a novel unsupervised feature selection criterion called "I/NI-calls"
	"""
	
	homepage = "http://www.bioinf.jku.at/software/farms/farms.html"
	bioc = "farms" 

	version("1.54.0", commit="90b6bd584a99a910ec1061edaa924ec06310b507")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-biobase@1.13.41:", type=("build", "run"))
