# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssignpop(RPackage):
	"""Population Assignment using Genetic, Non-Genetic or Integrated
Data in a Machine Learning Framework

	Use Monte-Carlo and K-fold cross-validation coupled with machine-
    learning classification algorithms to perform population assignment, with
    functionalities of evaluating discriminatory power of independent training
    samples, identifying informative loci, reducing data dimensionality for genomic
    data, integrating genetic and non-genetic data, and visualizing results.
	"""
	
	homepage = "https://github.com/alexkychen/assignPOP"
	cran = "assignPOP" 

	version("1.3.0", md5="39023ab44ba68db1590787442d089d61")

	depends_on("r@2.3.2:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tree", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
