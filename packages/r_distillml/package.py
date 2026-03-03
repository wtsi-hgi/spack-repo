# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistillml(RPackage):
	"""Model Distillation and Interpretability Methods for Machine
Learning Models

	Provides several methods for model distillation and interpretability 
    for general black box machine learning models and treatment effect estimation
    methods. For details on the algorithms implemented, see <https://forestry-labs.github.io/distillML/index.html>
    Brian Cho, Theo F. Saarinen, Jasjeet S. Sekhon, Simon Walter.
	"""
	
	homepage = "https://github.com/forestry-labs/distillML"
	cran = "distillML" 

	version("0.1.0.13", md5="c5371722c55dbd8e6f633ca57617759d")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rforestry", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-r6@2:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mltools", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
