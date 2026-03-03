# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProcesspredictr(RPackage):
	"""Process Prediction

	Means to predict process flow, such as process outcome, next activity, next time, remaining time, and remaining trace. Off-the-shelf predictive models based on the concept of Transformers are provided, as well as multiple ways to customize the models. This package is partly based on work described in Zaharah A. Bukhsh, Aaqib Saeed, & Remco M. Dijkman. (2021). "ProcessTransformer: Predictive Business Process Monitoring with Transformer Network" <arXiv:2104.00721>.
	"""
	
	cran = "processpredictR" 

	version("0.1.0", md5="38c3d149aae3b58bd9d8baa2939143d6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bupar", type=("build", "run"))
	depends_on("r-edear", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mltools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
