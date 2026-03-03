# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdmtune(RPackage):
	"""Species Distribution Model Selection

	User-friendly framework that enables the training and the
    evaluation of species distribution models (SDMs). The package implements
    functions for data driven variable selection and model tuning and includes
    numerous utilities to display the results. All the functions used to select
    variables or to tune model hyperparameters have an interactive real-time
    chart displayed in the 'RStudio' viewer pane during their execution.
	"""
	
	homepage = "https://consbiol-unibern.github.io/SDMtune/"
	cran = "SDMtune" 

	version("1.3.1", md5="b8f528ad97b967f0947a5c791baba3b0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli@3.4.1:", type=("build", "run"))
	depends_on("r-dismo@1.3.9:", type=("build", "run"))
	depends_on("r-gbm@2.1.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-maxnet@0.1.4:", type=("build", "run"))
	depends_on("r-nnet@7.3.12:", type=("build", "run"))
	depends_on("r-randomforest@4.6.14:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang@0.4.5:", type=("build", "run"))
	depends_on("r-rstudioapi@0.10:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-terra@1.6.47:", type=("build", "run"))
	depends_on("r-whisker@0.3.2:", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
