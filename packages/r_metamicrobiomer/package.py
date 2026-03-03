# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetamicrobiomer(RPackage):
	"""Microbiome Data Analysis & Meta-Analysis with GAMLSS-BEZI &
Random Effects

	Generalized Additive Model for Location, Scale and Shape (GAMLSS) 
    with zero inflated beta (BEZI) family for analysis of microbiome relative abundance data 
    (with various options for data transformation/normalization to address compositional effects) and 
    random effects meta-analysis models for meta-analysis pooling estimates across microbiome studies 
    are implemented. 
    Random Forest model to predict microbiome age based on relative abundances of  
    shared bacterial genera with the Bangladesh data (Subramanian et al 2014), 
    comparison of multiple diversity indexes using linear/linear mixed effect models 
    and some data display/visualization are also implemented.
    The reference paper is published by 
    Ho NT, Li F, Wang S, Kuhn L (2019) <doi:10.1186/s12859-019-2744-2> . 
	"""
	
	homepage = "https://github.com/nhanhocu/metamicrobiomeR"
	cran = "metamicrobiomeR" 

	version("1.2", md5="f473695cf921eadc3d7a131ce9a87f27")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-meta", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-zcompositions", type=("build", "run"))
	depends_on("r-compositions", type=("build", "run"))
