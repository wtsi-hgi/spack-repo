# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFoldgo(RPackage):
	"""Package for Fold-specific GO Terms Recognition

	FoldGO is a package designed to annotate gene sets derived from expression experiments and identify fold-change-specific GO terms.
	"""
	
	bioc = "FoldGO" 

	version("1.20.0", commit="7de37628e9df2b32a6c181ca56b16a42d1891af7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-topgo@2.30.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-tidyr@0.8:", type=("build", "run"))
