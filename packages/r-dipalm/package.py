# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDipalm(RPackage):
	"""Differential Pattern Analysis via Linear Modeling

	Individual gene expression patterns are encoded into a series of eigenvector patterns ('WGCNA' package). Using the framework of linear model-based differential expression comparisons ('limma' package), time-course expression patterns for genes in different conditions are compared and analyzed for significant pattern changes. For reference, see: Greenham K, Sartor RC, Zorich S, Lou P, Mockler TC and McClung CR. eLife. 2020 Sep 30;9(4). <doi:10.7554/eLife.58993>.
	"""
	
	cran = "DiPALM" 

	version("1.2", md5="9e5dfd7075ad0be6ca828317b2db3f7e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
