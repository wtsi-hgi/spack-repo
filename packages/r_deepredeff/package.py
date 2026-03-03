# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeepredeff(RPackage):
	"""Deep Learning Prediction of Effectors

	A tool that contains trained deep learning models
    for predicting effector proteins. 'deepredeff' has been trained to
    identify effector proteins using a set of known experimentally
    validated effectors from either bacteria, fungi, or oomycetes.
    Documentation is available via several vignettes, and the paper by
    Kristianingsih and MacLean (2020) <doi:10.1101/2020.07.08.193250>.
	"""
	
	homepage = "https://github.com/ruthkr/deepredeff/"
	cran = "deepredeff" 

	version("0.1.1", md5="9200413a49e824ac1f431fafb4bafa69")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
