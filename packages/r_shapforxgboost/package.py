# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShapforxgboost(RPackage):
	"""SHAP Plots for 'XGBoost'

	Aid in visual data investigations
 using SHAP (SHapley Additive exPlanation) visualization plots for 'XGBoost' and 'LightGBM'. 
 It provides summary plot, dependence plot, interaction plot, and force plot and relies on
 the SHAP implementation provided by 'XGBoost' and 'LightGBM'.
 Please refer to 'slundberg/shap' for the original implementation of SHAP in 'Python'. 
	"""
	
	homepage = "https://github.com/liuyanguu/SHAPforxgboost"
	cran = "SHAPforxgboost" 

	version("0.1.3", md5="295188c420d067017a9c40388890f931")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-xgboost@0.81:", type=("build", "run"))
	depends_on("r-data-table@1.12:", type=("build", "run"))
	depends_on("r-ggforce@0.2.1.9000:", type=("build", "run"))
	depends_on("r-ggextra@0.8:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
