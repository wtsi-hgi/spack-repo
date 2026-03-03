# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmbed(RPackage):
	"""Extra Recipes for Encoding Predictors

	Predictors can be converted to one or more numeric
    representations using a variety of methods. Effect encodings using
    simple generalized linear models <arXiv:1611.09477> or nonlinear
    models <arXiv:1604.06737> can be used.  There are also functions for
    dimension reduction and other approaches.
	"""
	
	homepage = "https://embed.tidymodels.org"
	cran = "embed" 

	version("1.1.4", md5="0d44354dfc66f7eb8cb54ec09a6aabdf")
	version("1.1.3", md5="9ccb4cd6bf92b83c14fc8859e7b9dd90")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-recipes@1.0.7:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-generics@0.1:", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
