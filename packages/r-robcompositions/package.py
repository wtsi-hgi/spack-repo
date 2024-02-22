# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobcompositions(RPackage):
	"""Compositional Data Analysis

	Methods for analysis of compositional data including robust
    methods  (<doi:10.1007/978-3-319-96422-5>), imputation of missing values (<doi:10.1016/j.csda.2009.11.023>), methods to replace 
    rounded zeros (<doi:10.1080/02664763.2017.1410524>, <doi:10.1016/j.chemolab.2016.04.011>, <doi:10.1016/j.csda.2012.02.012>), 
    count zeros (<doi:10.1177/1471082X14535524>), 
    methods to deal with essential zeros (<doi:10.1080/02664763.2016.1182135>), (robust) outlier
    detection for compositional data, (robust) principal component analysis for
    compositional data, (robust) factor analysis for compositional data, (robust)
    discriminant analysis for compositional data (Fisher rule), robust regression
    with compositional predictors, functional data analysis (<doi:10.1016/j.csda.2015.07.007>) and p-splines (<doi:10.1016/j.csda.2015.07.007>), 
    contingency (<doi:10.1080/03610926.2013.824980>) 
    and compositional tables (<doi:10.1111/sjos.12326>, <doi:10.1111/sjos.12223>, <doi:10.1080/02664763.2013.856871>) 
    and (robust) Anderson-Darling normality tests for
    compositional data as well as popular log-ratio transformations (addLR, cenLR,
    isomLR, and their inverse transformations). In addition, visualisation and
    diagnostic tools are implemented as well as high and low-level plot functions
    for the ternary diagram.
	"""
	
	cran = "robCompositions" 

	version("2.4.1", md5="875c5151c5d624f0a6e7a208a0292565")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-cvtools", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggfortify", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-robusthd", type=("build", "run"))
	depends_on("r-vim", type=("build", "run"))
	depends_on("r-zcompositions", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
