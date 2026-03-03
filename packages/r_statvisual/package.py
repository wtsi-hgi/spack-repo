# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatvisual(RPackage):
	"""Statistical Visualization Tools

	Visualization functions in the applications of translational medicine (TM) and biomarker (BM) development to compare groups by statistically visualizing data and/or results of analyses, such as visualizing data by displaying in one figure different groups' histograms, boxplots, densities, scatter plots, error-bar plots, or trajectory plots, by displaying scatter plots of top principal components or dendrograms with data points colored based on group information, or visualizing volcano plots to check the results of whole genome analyses for gene differential expression. 
	"""
	
	cran = "statVisual" 

	version("1.2.1", md5="932e1f4bc204e9f1b84e6400fae3994e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggfortify", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-forestplot", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-pvca", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
