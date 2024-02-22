# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvival666(RPackage):
	"""Eliminate the Influence of Co-Expression Genes on Target Genes

	Functions can be used for batch survival analysis, 
	but not only for it. Most importantly, it can verify any
 	P-value calculated according to the gene expression level and 
	eliminate the influence of co-expression genes.
	"""
	
	cran = "survival666" 

	version("0.5", md5="407227a106afdf807f9e0c10f111b964", url="https://cran.r-project.org/src/contrib/survival666_0.5.tar.gz")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survminer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
