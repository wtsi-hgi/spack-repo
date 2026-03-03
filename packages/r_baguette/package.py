# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaguette(RPackage):
	"""Efficient Model Functions for Bagging

	Tree- and rule-based models can be bagged
    (<doi:10.1007/BF00058655>) using this package and their predictions
    equations are stored in an efficient format to reduce the model
    objects size and speed.
	"""
	
	homepage = "https://baguette.tidymodels.org"
	cran = "baguette" 

	version("1.0.2", md5="c9e3f4d9e310b4bc85bffa7ad456298b")

	depends_on("r-parsnip@1:", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-butcher", type=("build", "run"))
	depends_on("r-c50", type=("build", "run"))
	depends_on("r-dials", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-hardhat@1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
