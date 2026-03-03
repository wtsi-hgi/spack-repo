# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsclassifr(RPackage):
	"""Automated Classification of Mass Spectra

	Functions to classify mass spectra in known categories, and to determine discriminant mass-over-charge values. It includes easy-to-use functions for pre-processing mass spectra, functions to determine discriminant mass-over-charge values (m/z) from a library of mass spectra corresponding to different categories, and functions to predict the category (species, phenotypes, etc.) associated to a mass spectrum from a list of selected mass-over-charge values. Three vignettes illustrating how to use the functions of this package from real data sets are also available online to help users: <https://agodmer.github.io/MSclassifR_examples/Vignettes/Vignettemsclassifr_Ecrobiav3.html>, <https://agodmer.github.io/MSclassifR_examples/Vignettes/Vignettemsclassifr_Klebsiellav3.html> and <https://agodmer.github.io/MSclassifR_examples/Vignettes/Vignettemsclassifr_DAv3.html>.
	"""
	
	homepage = "https://github.com/agodmer/MSclassifR_examples"
	cran = "MSclassifR" 

	version("0.3.3", md5="705463ef79b7dbb0e5f8286c84a7ec5e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cp4p", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-maldiquant", type=("build", "run"))
	depends_on("r-maldirppa", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-maldiquantforeign", type=("build", "run"))
	depends_on("r-mixomics", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fuzzyjoin", type=("build", "run"))
	depends_on("r-vsurf", type=("build", "run"))
	depends_on("r-metap", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-performanceestimation", type=("build", "run"))
	depends_on("r-mltools", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-ubl", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-vita", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
