# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHealthyrAi(RPackage):
	"""The Machine Learning and AI Modeling Companion to 'healthyR'

	
    Hospital machine learning and ai data analysis workflow tools, modeling, and automations. 
    This library provides many useful tools to review common administrative 
    hospital data. Some of these include predicting length of stay, and readmits.
    The aim is to provide a simple and consistent verb framework that takes the 
    guesswork out of everything.
	"""
	
	homepage = "https://github.com/spsanderson/healthyR.ai"
	cran = "healthyR.ai" 

	version("0.0.13", md5="5a759e1e9f841faec92c153a1565e5c1")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-yardstick@0.0.8:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-recipes@1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-h2o", type=("build", "run"))
	depends_on("r-dials", type=("build", "run"))
	depends_on("r-parsnip", type=("build", "run"))
	depends_on("r-tune", type=("build", "run"))
	depends_on("r-workflows", type=("build", "run"))
	depends_on("r-modeltime", type=("build", "run"))
