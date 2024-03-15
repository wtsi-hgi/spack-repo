# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecipes(RPackage):
	"""Preprocessing Tools to Create Design Matrices.

	An extensible framework to create and preprocess design matrices.  Recipes
	consist of one or more data manipulation and analysis "steps".  Statistical
	parameters for the steps can be estimated from an initial data set and then
	applied to other data sets. The resulting design matrices can then be used
	as inputs into statistical or machine learning models."""

	cran = "recipes"

	license("MIT")

	version("1.0.10", md5="678b530e6c97ca93445dc99cf69fe7b5")

	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-clock@0.6.1:", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-generics@0.1.2:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-gower", type=("build", "run"))
	depends_on("r-hardhat@1.3:", type=("build", "run"))
	depends_on("r-ipred@0.9.12:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-lubridate@1.8:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-vctrs@0.5:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
