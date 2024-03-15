# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClassifyr(RPackage):
	"""A framework for cross-validated classification problems, with applications to differential variability and differential distribution testing

	The software formalises a framework for classification and survival model evaluation in R. There are four stages; Data transformation, feature selection, model training, and prediction. The requirements of variable types and variable order are fixed, but specialised variables for functions can also be provided. The framework is wrapped in a driver loop that reproducibly carries out a number of cross-validation schemes. Functions for differential mean, differential variability, and differential distribution are included. Additional functions may be developed by the user, by creating an interface to the framework.
	"""
	
	homepage = "https://sydneybiox.github.io/ClassifyR/"
	bioc = "ClassifyR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ClassifyR_3.6.5.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ClassifyR/ClassifyR_3.6.5.tar.gz"]

	version("3.6.5", md5="3d5bac437fffdc2b44d9ab39d8bb5470")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggupset", type=("build", "run"))
