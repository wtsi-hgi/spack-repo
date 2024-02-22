# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDslice(RPackage):
	"""Dynamic Slicing

	Dynamic slicing is a method designed for dependency detection between a categorical variable and a continuous variable. It could be applied for non-parametric hypothesis testing and gene set enrichment analysis.
	"""
	
	cran = "dslice" 

	version("1.2.2", md5="73dfe5b41ae0278c9ff0d8434469e38c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2@0.9.3.1:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
