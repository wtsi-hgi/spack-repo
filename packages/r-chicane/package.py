# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChicane(RPackage):
	"""Capture Hi-C Analysis Engine

	Toolkit for processing and calling interactions in capture Hi-C data. Converts BAM files into counts of reads linking restriction fragments, and identifies pairs of fragments that interact more than expected by chance. Significant interactions are identified by comparing the observed read count to the expected background rate from a count regression model.
	"""
	
	cran = "chicane" 

	version("0.1.8", md5="ccc12fc2cb4b5a3e2c733a36d1dc1660")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gamlss-tr", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-bedr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("bedtools2", type=("build", "link", "run"))
