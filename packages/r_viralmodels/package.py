# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViralmodels(RPackage):
	"""Viral Load and CD4 Lymphocytes Regression Models

	Provides a comprehensive framework for building, evaluating, and visualizing regression models for analyzing viral load and CD4 (Cluster of Differentiation 4) lymphocytes data. It leverages the principles of the tidymodels ecosystem of Max Kuhn and Hadley Wickham (2020) <https://www.tidymodels.org> to offer a user-friendly experience in model development. This package includes functions for data preprocessing, feature engineering, model training, tuning, and evaluation, along with visualization tools to enhance the interpretation of model results. It is specifically designed for researchers in biostatistics, computational biology, and HIV research who aim to perform reproducible and rigorous analyses to gain insights into disease dynamics. The main focus is on improving the understanding of the relationships between viral load, CD4 lymphocytes, and other relevant covariates to contribute to HIV research and the visibility of vulnerable seropositive populations.
	"""
	
	cran = "viralmodels" 

	version("1.2.0", md5="eaf066f2270d7d92c9d2659c77f4a9a0")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
	depends_on("r-kknn", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-parsnip", type=("build", "run"))
	depends_on("r-recipes", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tune", type=("build", "run"))
	depends_on("r-vdiffr", type=("build", "run"))
	depends_on("r-workflows", type=("build", "run"))
	depends_on("r-workflowsets", type=("build", "run"))
