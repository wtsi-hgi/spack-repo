# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarsellcm(RPackage):
	"""Variable Selection for Model-Based Clustering of Mixed-Type Data
Set with Missing Values

	Full model selection (detection of the relevant features and estimation of the number of clusters) for model-based clustering (see reference here <doi:10.1007/s11222-016-9670-1>). Data to analyze can be continuous, categorical, integer or mixed. Moreover, missing values can occur and do not necessitate any pre-processing. Shiny application permits an easy interpretation of the results.
	"""
	
	homepage = "http://varsellcm.r-forge.r-project.org/"
	cran = "VarSelLCM" 

	version("2.1.3.1", md5="32d330321dea2533523cbdf4cb68fa6c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
