# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmap(RPackage):
	"""Logistic Mapping

	Set of tools for mapping of categorical response variables based on principal component analysis (pca) and multidimensional unfolding (mdu).
	"""
	
	cran = "lmap" 

	version("0.1.2", md5="957bfe41c8475cbc93148c9edb7d278c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-fmdu", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
