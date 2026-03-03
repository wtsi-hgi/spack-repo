# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetrica(RPackage):
	"""Prediction Performance Metrics

	A compilation of more than 80 functions designed to quantitatively and visually evaluate prediction performance of regression (continuous variables) and classification (categorical variables) of point-forecast models (e.g. APSIM, DSSAT, DNDC, supervised Machine Learning). For regression, it includes functions to generate plots (scatter, tiles, density, & Bland-Altman plot), and to estimate error metrics (e.g. MBE, MAE, RMSE), error decomposition (e.g. lack of accuracy-precision), model efficiency (e.g. NSE, E1, KGE), indices of agreement (e.g. d, RAC), goodness of fit (e.g. r, R2), adjusted correlation coefficients (e.g. CCC, dcorr), symmetric regression coefficients (intercept, slope), and mean absolute scaled error (MASE) for time series predictions. For classification (binomial and multinomial), it offers functions to generate and plot confusion matrices, and to estimate performance metrics such as accuracy, precision, recall, specificity, F-score, Cohen's Kappa, G-mean, and many more. For more details visit the vignettes <https://adriancorrendo.github.io/metrica/>.
	"""
	
	homepage = "https://adriancorrendo.github.io/metrica/"
	cran = "metrica" 

	version("2.0.3", md5="a243d71b24c096479ffadd407ef0a01d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-ggpp", type=("build", "run"))
	depends_on("r-minerva", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
