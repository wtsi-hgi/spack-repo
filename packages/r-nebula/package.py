# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNebula(RPackage):
	"""Negative Binomial Mixed Models Using Large-Sample Approximation
for Differential Expression Analysis of ScRNA-Seq Data

	A fast negative binomial mixed model for conducting association analysis of multi-subject single-cell data. It can be used for identifying marker genes, differential expression and co-expression analyses. The model includes subject-level random effects to account for the hierarchical structure in multi-subject single-cell data. See He et al. (2021) <doi:10.1038/s42003-021-02146-6>.  
	"""
	
	homepage = "https://github.com/lhe17/nebula"
	cran = "nebula" 

	version("1.5.3", md5="78a249fec5e4ebf4b9a151baa2117c90")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
	depends_on("r-parallelly@1.34:", type=("build", "run"))
	depends_on("r-dofuture@0.12.2:", type=("build", "run"))
	depends_on("r-future@1.32:", type=("build", "run"))
	depends_on("r-foreach@1.5.2:", type=("build", "run"))
	depends_on("r-dorng@1.8.6:", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
