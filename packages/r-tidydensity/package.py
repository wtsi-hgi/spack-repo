# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidydensity(RPackage):
	"""Functions for Tidy Analysis and Generation of Random Data

	
    To make it easy to generate random numbers based upon the underlying stats 
    distribution functions. All data is returned in a tidy and structured
    format making working with the data simple and straight forward. Given that the
    data is returned in a tidy 'tibble' it lends itself to working with the rest of the
    'tidyverse'.
	"""
	
	homepage = "https://github.com/spsanderson/TidyDensity"
	cran = "TidyDensity" 

	version("1.3.0", md5="37fbfa4b697d54f1cc7975943b44d6c8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
