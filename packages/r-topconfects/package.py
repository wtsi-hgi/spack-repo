# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopconfects(RPackage):
	"""Top Confident Effect Sizes

	Rank results by confident effect sizes, while maintaining False Discovery Rate and False Coverage-statement Rate control. Topconfects is an alternative presentation of TREAT results with improved usability, eliminating p-values and instead providing confidence bounds. The main application is differential gene expression analysis, providing genes ranked in order of confident log2 fold change, but it can be applied to any collection of effect sizes with associated standard errors.
	"""
	
	homepage = "https://github.com/pfh/topconfects"
	bioc = "topconfects" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/topconfects_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/topconfects/topconfects_1.18.0.tar.gz"]

	version("1.18.0", sha256="d3d5da5a4127bac933e6daad3670d676b604f05eced49879cc1aabdae04bd90d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
