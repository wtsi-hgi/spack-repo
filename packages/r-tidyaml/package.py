# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyaml(RPackage):
	"""Automatic Machine Learning with 'tidymodels'

	The goal of this package will be to provide a simple interface for automatic machine learning that fits the 'tidymodels' framework. The intention is to work for regression and classification problems with a simple verb framework.
	"""
	
	homepage = "https://github.com/spsanderson/tidyAML"
	cran = "tidyAML" 

	version("0.0.4", md5="ef987f739f292a818e9b384d2bc07005")

	depends_on("r-parsnip", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-purrr@0.3.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-rsample@1.1:", type=("build", "run"))
	depends_on("r-workflows@1.1.2:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-workflowsets", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
