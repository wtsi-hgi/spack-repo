# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnmeval(RPackage):
	"""Automated Tuning and Evaluations of Ecological Niche Models

	Runs ecological niche models over all combinations of user-defined settings (i.e., tuning), performs cross validation to evaluate models, and returns data tables to aid in selection of optimal model settings that balance goodness-of-fit and model complexity. Also has functions to partition data spatially (or not) for cross validation, to plot multiple visualizations of results, to run null models to estimate significance and effect sizes of performance metrics, and to calculate niche overlap between model predictions, among others. The package was originally built for Maxent models (Phillips et al. 2006, Phillips et al. 2017), but the current version allows possible extensions for any modeling algorithm. The extensive vignette, which guides users through most package functionality but unfortunately has a file size too big for CRAN, can be found here on the package's Github Pages website: <https://jamiemkass.github.io/ENMeval/articles/ENMeval-2.0-vignette.html>.
	"""
	
	homepage = "https://jamiemkass.github.io/ENMeval/"
	cran = "ENMeval" 

	version("2.0.4", md5="d4e4fd7e8c446aa6ef3674c44c9d4d2a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-dismo", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-maxnet", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rangemodelmetadata", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
