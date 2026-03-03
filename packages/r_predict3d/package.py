# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredict3d(RPackage):
	"""Draw Three Dimensional Predict Plot Using Package 'rgl'

	Draw 2 dimensional and three dimensional plot for multiple regression models using package 'ggplot2' and 'rgl'.
   Supports linear models (lm), generalized linear models (glm) and local polynomial regression fittings (loess).  
	"""
	
	homepage = "https://github.com/cardiomoon/predict3d"
	cran = "predict3d" 

	version("0.1.4", md5="285e5c9402e7752c952c72f8b1353144")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-rgl@1.0.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggiraphextra", type=("build", "run"))
	depends_on("r-modelr", type=("build", "run"))
	depends_on("r-prediction", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
