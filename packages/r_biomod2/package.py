# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiomod2(RPackage):
	"""Ensemble Platform for Species Distribution Modeling

	Functions for species distribution modeling, calibration and evaluation, 
  ensemble of models, ensemble forecasting and visualization. The package permits to run
  consistently up to 10 single models on a presence/absences (resp presences/pseudo-absences)
  dataset and to combine them in ensemble models and ensemble projections. Some bench of other 
  evaluation and visualisation tools are also available within the package.
	"""
	
	cran = "biomod2" 

	version("4.2-4", md5="870c557585291ef914db6ea792fb0d00", url="https://cran.r-project.org/src/contrib/biomod2_4.2-4.tar.gz")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-terra@1.6.33:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-gbm@2.1.3:", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-mda", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-maxnet", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-proc@1.15:", type=("build", "run"))
	depends_on("r-presenceabsence", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
