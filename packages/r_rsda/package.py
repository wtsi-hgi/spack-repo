# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsda(RPackage):
	"""R to Symbolic Data Analysis

	Symbolic Data Analysis (SDA) was proposed by professor Edwin Diday in 1987, the main purpose of SDA is to substitute the set of rows (cases) in the data table for  a concept (second order statistical unit). This package implements, to the symbolic case, certain techniques of automatic classification, as well as some linear models.
	"""
	
	homepage = "https://oldemarrodriguez.com/"
	cran = "RSDA" 

	version("3.2.1", md5="a99546ee2147ab9566104c1231e23c3c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-vctrs@0.2.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang@0.4.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpolypath", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-princurve", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-randomcolor", type=("build", "run"))
	depends_on("r-kknn", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-neuralnet", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
