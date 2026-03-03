# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHealthyverse(RPackage):
	"""Easily Install and Load the 'healthyverse'

	The 'healthyverse' is a set of packages that work in
    harmony because they share common data representations and 'API'
    design. This package is designed to make it easy to install and load
    multiple 'healthyverse' packages in a single step.
	"""
	
	homepage = "https://github.com/spsanderson/healthyverse"
	cran = "healthyverse" 

	version("1.0.4", md5="bb033121211bceea80594b88e26850dd")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-healthyr", type=("build", "run"))
	depends_on("r-healthyr-data", type=("build", "run"))
	depends_on("r-healthyr-ts", type=("build", "run"))
	depends_on("r-healthyr-ai", type=("build", "run"))
	depends_on("r-tidydensity", type=("build", "run"))
	depends_on("r-tidyaml", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
