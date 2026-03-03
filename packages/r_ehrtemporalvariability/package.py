# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REhrtemporalvariability(RPackage):
	"""Delineating Temporal Dataset Shifts in Electronic Health Records

	Functions to delineate temporal dataset shifts in Electronic Health 
             Records through the projection and visualization of dissimilarities 
             among data temporal batches. This is done through the estimation of 
             data statistical distributions over time and their projection in 
             non-parametric statistical manifolds, uncovering the patterns of the 
             data latent temporal variability. 'EHRtemporalVariability' is 
             particularly suitable for multi-modal data and categorical variables 
             with a high number of values, common features of biomedical data where 
             traditional statistical process control or time-series methods may not 
             be appropriate. 'EHRtemporalVariability' allows you to explore and 
             identify dataset shifts through visual analytics formats such as 
             Data Temporal heatmaps and Information Geometric Temporal (IGT) plots. 
             An additional 'EHRtemporalVariability' Shiny app can be used to load 
             and explore the package results and even to allow the use of these 
             functions to those users non-experienced in R coding. (Sáez et al. 2020)
             <doi:10.1093/gigascience/giaa079>.
	"""
	
	homepage = "https://github.com/hms-dbmi/EHRtemporalVariability"
	cran = "EHRtemporalVariability" 

	version("1.2.1", md5="2787793b83b52d70f98aaac84fc6f7df")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
