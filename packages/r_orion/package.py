# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrion(RPackage):
	"""Ordinal Relations

	Functions to handle ordinal relations reflected within the feature space. Those function allow to search for ordinal relations in multi-class datasets. One can check whether proposed relations are reflected in a specific feature representation. Furthermore, it provides functions to filter, organize and further analyze those ordinal relations. 
	"""
	
	cran = "ORION" 

	version("1.0.3", md5="caa56f9913b18576cd5de2a988daa9ad")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tunepareto", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
