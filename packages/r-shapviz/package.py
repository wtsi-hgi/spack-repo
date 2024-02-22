# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShapviz(RPackage):
	"""SHAP Visualizations

	Visualizations for SHAP (SHapley Additive exPlanations), such
    as waterfall plots, force plots, various types of importance plots,
    dependence plots, and interaction plots.  These plots act on a
    'shapviz' object created from a matrix of SHAP values and a
    corresponding feature dataset. Wrappers for the R packages 'xgboost',
    'lightgbm', 'fastshap', 'shapr', 'h2o', 'treeshap', 'DALEX', and
    'kernelshap' are added for convenience.  By separating visualization
    and computation, it is possible to display factor variables in graphs,
    even if the SHAP values are calculated by a model that requires
    numerical features. The plots are inspired by those provided by the
    'shap' package in Python, but there is no dependency on it.
	"""
	
	homepage = "https://github.com/ModelOriented/shapviz"
	cran = "shapviz" 

	version("0.9.3", md5="cb5fbfff9bd81957b1c057efea37a9de")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggfittext@0.8:", type=("build", "run"))
	depends_on("r-gggenes", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
