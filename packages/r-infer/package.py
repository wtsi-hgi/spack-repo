# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfer(RPackage):
	"""Tidy Statistical Inference

	The objective of this package is to perform inference using
    an expressive statistical grammar that coheres with the tidy design
    framework.
	"""
	
	homepage = "https://github.com/tidymodels/infer"
	cran = "infer" 

	version("1.0.6", md5="f3ddce69d77824dda96ed13eca65d053")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
