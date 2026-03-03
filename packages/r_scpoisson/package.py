# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScpoisson(RPackage):
	"""Single Cell Poisson Probability Paradigm

	Useful to visualize the Poissoneity (an independent Poisson statistical framework, 
  where each RNA measurement for each cell comes from its own independent Poisson distribution) of 
  Unique Molecular Identifier (UMI) based single cell RNA sequencing (scRNA-seq) data, and explore 
  cell clustering based on model departure as a novel data representation. 
	"""
	
	cran = "scpoisson" 

	version("0.0.1", md5="e9f9e4e509e3021d6ce1f1d558d039ff")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmpca", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-seuratobject", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
