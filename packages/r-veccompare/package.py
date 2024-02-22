# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVeccompare(RPackage):
	"""Perform Set Operations on Vectors, Automatically Generating All
n-Wise Comparisons, and Create Markdown Output

	Automates set operations (i.e., comparisons of overlap) between multiple vectors.
    It also contains a function for automating reporting in 'RMarkdown', by generating markdown output for easy analysis, as well as an 'RMarkdown' template for use with 'RStudio'.
	"""
	
	homepage = "https://github.com/publicus/r-veccompare"
	cran = "veccompare" 

	version("0.1.0", md5="adc0f4537a0a5f6180d709735a1b5b99")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
