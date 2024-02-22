# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTspred(RPackage):
	"""Functions for Benchmarking Time Series Prediction

	Functions for defining and conducting a time series prediction process including pre(post)processing, decomposition, modelling, prediction and accuracy assessment. The generated models and its yielded prediction errors can be used for benchmarking other time series prediction methods and for creating a demand for the refinement of such methods. For this purpose, benchmark data from prediction competitions may be used.
	"""
	
	homepage = "https://github.com/RebeccaSalles/TSPred/wiki"
	cran = "TSPred" 

	version("5.1", md5="b4e227146a17f36b752fc7608a8c4389")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-kfas", type=("build", "run"))
	depends_on("r-mumin", type=("build", "run"))
	depends_on("r-emd", type=("build", "run"))
	depends_on("r-wavelets", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
	depends_on("r-modelmetrics", type=("build", "run"))
	depends_on("r-rsnns", type=("build", "run"))
	depends_on("r-rlibeemd", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-elmnnrcpp", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-tfdatasets", type=("build", "run"))
