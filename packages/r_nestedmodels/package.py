# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNestedmodels(RPackage):
	"""Tidy Modelling for Nested Data

	A modelling framework for nested data using the 'tidymodels' 
    ecosystem. Specify how to nest data using the 'recipes' package, create 
    testing and training splits using 'rsample', and fit models to this data
    using the 'parsnip' and 'workflows' packages. Allows any model to be fit
    to nested data.
	"""
	
	homepage = "https://github.com/ashbythorpe/nestedmodels"
	cran = "nestedmodels" 

	version("1.1.0", md5="2b99d74f86d0c821e2d1f7e7eab12673")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-parsnip", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-recipes", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@0.8.99:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
