# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REix(RPackage):
	"""Explain Interactions in 'XGBoost'

	Structure mining from 'XGBoost' and 'LightGBM' models.
    Key functionalities of this package cover: visualisation of tree-based ensembles models,
    identification of interactions, measuring of variable importance,
    measuring of interaction importance, explanation of single prediction 
    with break down plots (based on 'xgboostExplainer' and 'iBreakDown' packages). 
    To download the 'LightGBM' use the following link: <https://github.com/Microsoft/LightGBM>.
    'EIX' is a part of the 'DrWhy.AI' universe.
	"""
	
	homepage = "https://github.com/ModelOriented/EIX"
	cran = "EIX" 

	version("1.2.0", md5="f0cb52383f7539da01f6132a460ddb7f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-dalex", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggiraphextra", type=("build", "run"))
	depends_on("r-ibreakdown", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
