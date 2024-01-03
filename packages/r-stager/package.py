# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RStager(RPackage):
	"""stageR: stage-wise analysis of high throughput gene expression data in R

	The stageR package allows automated stage-wise analysis of high-throughput gene expression data. The method is published in Genome Biology at https://genomebiology.biomedcentral.com/articles/10.1186/s13059-017-1277-0
	"""
	
	bioc = "stageR" 

	version("1.24.0", commit="c4ff87efeaa83f4aa941bc88e8e4f5bceaee0cb7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
