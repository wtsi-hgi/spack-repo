# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinetune(RPackage):
	"""Additional Functions for Model Tuning

	The ability to tune models is important. 'finetune' enhances
    the 'tune' package by providing more specialized methods for finding
    reasonable values of model tuning parameters.  Two racing methods
    described by Kuhn (2014) <arXiv:1405.6974> are included. An iterative
    search method using generalized simulated annealing (Bohachevsky,
    Johnson and Stein, 1986) <doi:10.1080/00401706.1986.10488128> is also
    included.
	"""
	
	homepage = "https://github.com/tidymodels/finetune"
	cran = "finetune" 

	version("1.1.0", md5="d8c9cda86250756d4a210bfd9f50f4b6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tune@1.1.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dials@0.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-parsnip@1.1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-workflows@0.2.6:", type=("build", "run"))
